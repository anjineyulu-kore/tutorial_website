// Client-side API calls for registration and admin actions
// Used by pages/register.html and pages/admin.html

// API base — updated to use FastAPI server on port 7000
const API_BASE = 'http://127.0.0.1:7000/api';
// Root (without /api) for static or data endpoints
const ROOT = API_BASE.replace(/\/api$/, '');

async function registerStudent(formEl, feedbackEl) {
    const form = new FormData(formEl);
    const payload = {
        name: form.get('name'),
        email: form.get('email'),
        course: form.get('course')
    };

    try {
        const res = await fetch(`${API_BASE}/register`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });
        const data = await res.json();
        if (res.status === 201) {
            feedbackEl.innerText = 'Registration submitted. Please wait for admin approval.';
            formEl.reset();
        } else {
            feedbackEl.innerText = data.error || JSON.stringify(data);
        }
    } catch (err) {
        feedbackEl.innerText = 'Network error: ' + err.message;
    }
}

async function fetchUsers(adminToken) {
    try {
        const res = await fetch(`${API_BASE}/users`, {
            headers: { 'X-Admin-Token': adminToken }
        });
        if (res.status === 200) return await res.json();
        const err = await res.json();
        throw new Error(err.error || 'Unknown error');
    } catch (err) {
        throw err;
    }
}

async function approveUser(adminToken, userId) {
    const res = await fetch(`${API_BASE}/users/${userId}/approve`, {
        method: 'POST',
        headers: { 'X-Admin-Token': adminToken }
    });
    return res;
}

async function rejectUser(adminToken, userId) {
    const res = await fetch(`${API_BASE}/users/${userId}/reject`, {
        method: 'POST',
        headers: { 'X-Admin-Token': adminToken }
    });
    return res;
}


// Bulk approve/reject helper
async function bulkApprove(adminToken, userIds) {
    const calls = userIds.map(id => approveUser(adminToken, id));
    return Promise.all(calls);
}

async function bulkReject(adminToken, userIds) {
    const calls = userIds.map(id => rejectUser(adminToken, id));
    return Promise.all(calls);
}

// Download raw users.json (requires admin token)
async function downloadUsersJson(adminToken) {
    const url = `${ROOT}/data/users.json`;
    const res = await fetch(url, { headers: { 'X-Admin-Token': adminToken } });
    if (!res.ok) {
        const err = await res.json().catch(() => ({}));
        throw new Error(err.detail || 'Failed to download users.json');
    }
    return await res.json();
}


// Concept management (admin)
async function fetchConcepts(adminToken) {
    const res = await fetch(`${API_BASE}/concepts`, { headers: { 'X-Admin-Token': adminToken } });
    if (!res.ok) {
        const err = await res.json().catch(() => ({}));
        throw new Error(err.detail || 'Failed to fetch concepts');
    }
    return await res.json();
}

async function createConcept(adminToken, data) {
    const res = await fetch(`${API_BASE}/concepts`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'X-Admin-Token': adminToken },
        body: JSON.stringify(data)
    });
    if (!res.ok) { const err = await res.json().catch(()=>({})); throw new Error(err.detail || 'Create failed'); }
    return await res.json();
}

async function updateConcept(adminToken, id, data) {
    const res = await fetch(`${API_BASE}/concepts/${id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json', 'X-Admin-Token': adminToken },
        body: JSON.stringify(data)
    });
    if (!res.ok) { const err = await res.json().catch(()=>({})); throw new Error(err.detail || 'Update failed'); }
    return await res.json();
}

async function deleteConcept(adminToken, id) {
    const res = await fetch(`${API_BASE}/concepts/${id}`, {
        method: 'DELETE',
        headers: { 'X-Admin-Token': adminToken }
    });
    if (!res.ok) { const err = await res.json().catch(()=>({})); throw new Error(err.detail || 'Delete failed'); }
    return await res.json();
}


// Login an approved user by email. The server will set an HttpOnly cookie (TA_USER_TOKEN).
// Use credentials: 'include' so the browser receives the cookie.
async function loginUser(email) {
    const res = await fetch(`${API_BASE}/login`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email }),
        credentials: 'include'
    });
    if (!res.ok) {
        const err = await res.json().catch(() => ({}));
        throw new Error(err.detail || 'Login failed');
    }
    return await res.json();
}

// Fetch current logged-in user using cookie (credentials included)
async function fetchMe() {
    const res = await fetch(`${API_BASE}/me`, { credentials: 'include' });
    if (!res.ok) {
        const err = await res.json().catch(() => ({}));
        throw new Error(err.detail || 'Not logged in');
    }
    return await res.json();
}


// Logout user: server will clear the cookie
async function logoutUser() {
    const res = await fetch(`${API_BASE}/logout`, {
        method: 'POST',
        credentials: 'include'
    });
    if (!res.ok) {
        const err = await res.json().catch(() => ({}));
        throw new Error(err.detail || 'Logout failed');
    }
    return true;
}

// Helper to render user rows in admin panel
function renderUsersTable(users, containerEl, adminToken) {
    containerEl.innerHTML = '';
    if (!users || !users.length) {
        containerEl.innerHTML = '<p>No users yet.</p>';
        return;
    }

    // table header
    const table = document.createElement('table');
    table.style.width = '100%';
    table.style.borderCollapse = 'collapse';
    table.innerHTML = `
        <thead>
            <tr style="text-align:left;border-bottom:1px solid #ddd">
                <th style="padding:8px"><input id="selectAll" type="checkbox" /></th>
                <th style="padding:8px">Name</th>
                <th style="padding:8px">Email</th>
                <th style="padding:8px">Course</th>
                <th style="padding:8px">Status</th>
                <th style="padding:8px">Progress</th>
                <th style="padding:8px">Registered</th>
                <th style="padding:8px">Approved</th>
                <th style="padding:8px">Token</th>
                <th style="padding:8px">Actions</th>
            </tr>
        </thead>
        <tbody></tbody>
    `;
    const tbody = table.querySelector('tbody');

    users.forEach(u => {
        const tr = document.createElement('tr');
        tr.style.borderBottom = '1px solid #f2f2f2';
        tr.innerHTML = `
            <td style="padding:8px"><input class="sel" data-id="${u.id}" type="checkbox" /></td>
            <td style="padding:8px"><strong>${u.name}</strong></td>
            <td style="padding:8px">${u.email}</td>
            <td style="padding:8px"><em>${u.course}</em></td>
            <td style="padding:8px">${u.status || ''}</td>
            <td style="padding:8px">${u.registered_at || ''}</td>
            <td style="padding:8px">${u.approved_at || ''}</td>
            <td style="padding:8px">${u.access_token ? `<button class=\"btn-copy-token\" data-token=\"${u.access_token}\">Copy</button>` : ''}</td>
            <td style="padding:8px;max-width:140px">
                ${renderProgress(u)}
            </td>
            <td style="padding:8px">${u.access_token ? '' : ''}</td>
            
            <td style="padding:8px">
                <button data-id="${u.id}" class="btn-approve" style="margin-right:6px">Approve</button>
                <button data-id="${u.id}" class="btn-reject">Reject</button>
            </td>
        `;
        tbody.appendChild(tr);
    });

    containerEl.appendChild(table);

    // helper to render progress for a user
    function renderProgress(u) {
        const prog = u && u.progress ? u.progress[u.course] || 0 : 0;
        const pct = Math.max(0, Math.min(100, parseInt(prog) || 0));
        return `
            <div style="display:flex;align-items:center;gap:.5rem">
                <div style="flex:1;background:#f1f5f9;border-radius:6px;height:10px;overflow:hidden">
                    <div style="width:${pct}%;height:10px;background:#60a5fa"></div>
                </div>
                <div style="width:40px;text-align:right;font-size:0.9rem">${pct}%</div>
            </div>
        `;
    }

    // select all
    const selAll = containerEl.querySelector('#selectAll');
    selAll.addEventListener('change', (ev) => {
        const checked = ev.target.checked;
        containerEl.querySelectorAll('.sel').forEach(c => c.checked = checked);
    });

    // Attach handlers
    containerEl.querySelectorAll('.btn-approve').forEach(b => {
        b.addEventListener('click', async (ev) => {
            const id = ev.target.getAttribute('data-id');
            try {
                const res = await approveUser(adminToken, id);
                if (res.status === 200) {
                    alert('User approved');
                    location.reload();
                } else {
                    const err = await res.json().catch(() => ({}));
                    alert('Error: ' + (err.detail || res.statusText));
                }
            } catch (err) {
                alert('Network error: ' + err.message);
            }
        });
    });

    containerEl.querySelectorAll('.btn-reject').forEach(b => {
        b.addEventListener('click', async (ev) => {
            const id = ev.target.getAttribute('data-id');
            try {
                const res = await rejectUser(adminToken, id);
                if (res.status === 200) {
                    alert('User rejected');
                    location.reload();
                } else {
                    const err = await res.json().catch(() => ({}));
                    alert('Error: ' + (err.detail || res.statusText));
                }
            } catch (err) {
                alert('Network error: ' + err.message);
            }
        });
    });

    // copy token handlers
    containerEl.querySelectorAll('.btn-copy-token').forEach(b => {
        b.addEventListener('click', (ev) => {
            const token = ev.target.getAttribute('data-token');
            navigator.clipboard.writeText(token).then(() => {
                alert('Token copied to clipboard');
            }).catch(() => alert('Failed to copy token'));
        });
    });
}
