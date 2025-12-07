from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.responses import JSONResponse, FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import json
from datetime import datetime
from uuid import uuid4

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
USERS_FILE = os.path.join(DATA_DIR, 'users.json')
CONCEPTS_FILE = os.path.join(DATA_DIR, 'concepts.json')
ADMIN_TOKEN = os.environ.get('TA_ADMIN_TOKEN', 'admin123')  # change via environment

# Base directory for static site files (the tutorial_website folder)
BASE_DIR = os.path.dirname(__file__)

app = FastAPI(title='Test Automation Hub - Registration API')

# Allow cross origin from local files
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# Mount static folders so the frontend can load assets and pages directly
# We mount specific prefixes to avoid catching /api routes.
app.mount('/assets', StaticFiles(directory=os.path.join(BASE_DIR, 'assets')), name='assets')
# Do not mount /pages as StaticFiles so we can protect tutorial pages.
# Public pages (registration/admin) will still be served; other pages require an approved user.
app.mount('/data', StaticFiles(directory=DATA_DIR), name='data')

# Ensure data directory and file exist
os.makedirs(DATA_DIR, exist_ok=True)
if not os.path.exists(USERS_FILE):
    with open(USERS_FILE, 'w', encoding='utf-8') as f:
        json.dump([], f, indent=2)
if not os.path.exists(CONCEPTS_FILE):
    with open(CONCEPTS_FILE, 'w', encoding='utf-8') as f:
        json.dump([], f, indent=2)


def load_concepts():
    with open(CONCEPTS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_concepts(concepts):
    with open(CONCEPTS_FILE, 'w', encoding='utf-8') as f:
        json.dump(concepts, f, indent=2, ensure_ascii=False)


def slugify(text: str):
    # simple slugify: lowercase, replace spaces with -, keep alphanum and -
    import re
    s = text.lower().strip()
    s = re.sub(r"[^a-z0-9\s-]", '', s)
    s = re.sub(r"[\s_-]+", '-', s)
    s = re.sub(r"^-+|-+$", '', s)
    return s


def load_users():
    with open(USERS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_users(users):
    with open(USERS_FILE, 'w', encoding='utf-8') as f:
        json.dump(users, f, indent=2, ensure_ascii=False)


def require_admin(request: Request):
    token = request.headers.get('X-Admin-Token') or request.query_params.get('token')
    return token == ADMIN_TOKEN


def get_user_from_request(request: Request):
    """Return the approved user dict if request contains a valid user token (cookie/header/query), else None."""
    token = None
    # cookie first
    if request.cookies.get('TA_USER_TOKEN'):
        token = request.cookies.get('TA_USER_TOKEN')
    # header fallback
    if not token:
        token = request.headers.get('X-User-Token')
    # query fallback
    if not token:
        token = request.query_params.get('token')
    if not token:
        return None
    users = load_users()
    for u in users:
        if u.get('access_token') == token and u.get('status') == 'approved':
            return u
    return None


class RegisterModel(BaseModel):
    name: str
    email: str
    course: str = 'general'


@app.post('/api/register')
async def register(payload: RegisterModel):
    if not payload.name or not payload.email:
        raise HTTPException(status_code=400, detail='name and email are required')

    users = load_users()
    user_id = str(uuid4())
    user = {
        'id': user_id,
        'name': payload.name,
        'email': payload.email,
        'course': payload.course,
        'status': 'pending',
        'registered_at': datetime.utcnow().isoformat() + 'Z'
    }
    users.append(user)
    save_users(users)
    return JSONResponse(status_code=201, content={'message':'registered','id': user_id})


@app.get('/api/users')
async def list_users(request: Request):
    if not require_admin(request):
        raise HTTPException(status_code=401, detail='admin token required')
    users = load_users()
    return users


@app.post('/api/users/{user_id}/approve')
async def approve_user(user_id: str, request: Request):
    if not require_admin(request):
        raise HTTPException(status_code=401, detail='admin token required')
    users = load_users()
    for u in users:
        if u['id'] == user_id:
            u['status'] = 'approved'
            u['approved_at'] = datetime.utcnow().isoformat() + 'Z'
            # generate an access token for approved user so they can login
            u['access_token'] = str(uuid4())
            save_users(users)
            return {'message':'approved','id': user_id}
    raise HTTPException(status_code=404, detail='user not found')


@app.post('/api/users/{user_id}/reject')
async def reject_user(user_id: str, request: Request):
    if not require_admin(request):
        raise HTTPException(status_code=401, detail='admin token required')
    users = load_users()
    for u in users:
        if u['id'] == user_id:
            u['status'] = 'rejected'
            u['rejected_at'] = datetime.utcnow().isoformat() + 'Z'
            save_users(users)
            return {'message':'rejected','id': user_id}
    raise HTTPException(status_code=404, detail='user not found')


@app.post('/api/login')
async def login(payload: dict, response: Response):
    """Login with email. Only approved users can get an access token (set as cookie and returned).

    Body: { "email": "user@example.com" }
    Returns: { token, id, name }
    """
    email = payload.get('email')
    if not email:
        raise HTTPException(status_code=400, detail='email required')
    users = load_users()
    for u in users:
        if u.get('email') == email:
            if u.get('status') != 'approved':
                raise HTTPException(status_code=403, detail='user not approved')
            token = u.get('access_token')
            if not token:
                # ensure token exists
                token = str(uuid4())
                u['access_token'] = token
                save_users(users)
            # set cookie for browser-based access
            response.set_cookie(key='TA_USER_TOKEN', value=token, httponly=True)
            return {'token': token, 'id': u['id'], 'name': u.get('name')}
    raise HTTPException(status_code=404, detail='user not found')


@app.post('/api/logout')
async def logout(response: Response):
    """Clear the TA_USER_TOKEN cookie to log the user out."""
    response.delete_cookie('TA_USER_TOKEN')
    return {'message': 'logged out'}


@app.get('/api/me')
async def me(request: Request):
    user = get_user_from_request(request)
    if not user:
        raise HTTPException(status_code=401, detail='not logged in')
    # don't leak access token
    out = {k: v for k, v in user.items() if k != 'access_token'}
    return out


@app.post('/api/me/progress')
async def update_progress(request: Request):
    """Update progress for the logged-in user.

    Request body: { "course": "python", "percent": 42 }
    """
    user = get_user_from_request(request)
    if not user:
        raise HTTPException(status_code=401, detail='not logged in')
    payload = await request.json()
    course = payload.get('course')
    percent = payload.get('percent')
    if not course or percent is None:
        raise HTTPException(status_code=400, detail='course and percent required')
    try:
        percent = int(percent)
    except Exception:
        raise HTTPException(status_code=400, detail='percent must be integer')
    if percent < 0 or percent > 100:
        raise HTTPException(status_code=400, detail='percent must be 0-100')

    users = load_users()
    for u in users:
        if u['id'] == user['id']:
            prog = u.get('progress', {})
            prog[course] = percent
            u['progress'] = prog
            save_users(users)
            return {'message': 'progress updated', 'progress': prog}

    raise HTTPException(status_code=404, detail='user not found')


@app.get('/data/users.json')
async def serve_users_file(request: Request):
    if not require_admin(request):
        raise HTTPException(status_code=401, detail='admin token required')
    return FileResponse(USERS_FILE)


@app.get('/api/concepts')
async def list_concepts(request: Request):
    # admin-only listing for management
    if not require_admin(request):
        raise HTTPException(status_code=401, detail='admin token required')
    return load_concepts()


@app.post('/api/concepts')
async def create_concept(request: Request):
    if not require_admin(request):
        raise HTTPException(status_code=401, detail='admin token required')
    payload = await request.json()
    title = payload.get('title')
    content = payload.get('content', '')
    slug = payload.get('slug') or slugify(title or '')
    if not title:
        raise HTTPException(status_code=400, detail='title required')
    concepts = load_concepts()
    # ensure slug uniqueness
    base = slug
    i = 1
    while any(c['slug'] == slug for c in concepts):
        slug = f"{base}-{i}"
        i += 1
    concept = {
        'id': str(uuid4()),
        'title': title,
        'slug': slug,
        'content': content,
        'created_at': datetime.utcnow().isoformat() + 'Z'
    }
    concepts.append(concept)
    save_concepts(concepts)
    return {'message': 'created', 'id': concept['id'], 'slug': slug}


@app.put('/api/concepts/{concept_id}')
async def update_concept(concept_id: str, request: Request):
    if not require_admin(request):
        raise HTTPException(status_code=401, detail='admin token required')
    payload = await request.json()
    concepts = load_concepts()
    for c in concepts:
        if c['id'] == concept_id:
            c['title'] = payload.get('title', c.get('title'))
            c['content'] = payload.get('content', c.get('content'))
            # optional slug update
            if payload.get('slug'):
                c['slug'] = payload.get('slug')
            c['updated_at'] = datetime.utcnow().isoformat() + 'Z'
            save_concepts(concepts)
            return {'message': 'updated', 'id': concept_id}
    raise HTTPException(status_code=404, detail='concept not found')


@app.delete('/api/concepts/{concept_id}')
async def delete_concept(concept_id: str, request: Request):
    if not require_admin(request):
        raise HTTPException(status_code=401, detail='admin token required')
    concepts = load_concepts()
    new = [c for c in concepts if c['id'] != concept_id]
    if len(new) == len(concepts):
        raise HTTPException(status_code=404, detail='concept not found')
    save_concepts(new)
    return {'message': 'deleted', 'id': concept_id}


@app.get('/')
async def root():
    """Serve the main index.html so visiting the server root shows the website."""
    index_path = os.path.join(BASE_DIR, 'index.html')
    if os.path.exists(index_path):
        return FileResponse(index_path, media_type='text/html')
    return JSONResponse({'message': 'Index file not found'}, status_code=404)


@app.get('/index.html')
async def index_html():
    """Serve index.html when requested explicitly (e.g. clicking Home -> index.html)."""
    index_path = os.path.join(BASE_DIR, 'index.html')
    if os.path.exists(index_path):
        return FileResponse(index_path, media_type='text/html')
    return JSONResponse({'message': 'Index file not found'}, status_code=404)


@app.get('/index')
async def index_redirect():
    """Redirect friendly /index to root."""
    index_path = os.path.join(BASE_DIR, 'index.html')
    if os.path.exists(index_path):
        return FileResponse(index_path, media_type='text/html')
    return JSONResponse({'message': 'Index file not found'}, status_code=404)


# Serve pages with authorization: registration and admin pages are public, other pages
# require an approved user (with a valid access token). If unauthorized, return index.html
# so only home content is visible.
@app.get('/pages/{page_path:path}')
async def serve_page(page_path: str, request: Request):
    page_file = os.path.join(BASE_DIR, 'pages', page_path)
    # Prevent path traversal
    if not os.path.abspath(page_file).startswith(os.path.abspath(os.path.join(BASE_DIR, 'pages'))):
        raise HTTPException(status_code=400, detail='invalid path')
    if not os.path.exists(page_file):
        raise HTTPException(status_code=404, detail='page not found')

    public_pages = ('register.html', 'admin.html', 'login.html')
    if os.path.basename(page_file) in public_pages:
        return FileResponse(page_file, media_type='text/html')

    user = get_user_from_request(request)
    if not user:
        # Not authorized to view inner pages — redirect to login and include next
        next_url = f"/pages/{page_path}"
        login_url = f"/pages/login.html?next={next_url}"
        return RedirectResponse(url=login_url)

    # authorized — serve requested page
    return FileResponse(page_file, media_type='text/html')


@app.get('/concepts/{slug}')
async def serve_concept(slug: str, request: Request):
        """Serve concept content to all users (public access)."""
        # find concept
        concepts = load_concepts()
        match = None
        for c in concepts:
                if c.get('slug') == slug:
                        match = c
                        break
        if not match:
                raise HTTPException(status_code=404, detail='concept not found')

        # render a rich HTML page for the concept with enhanced styling
        html = f"""<!doctype html>
<html>
<head>
    <meta charset='utf-8' />
    <meta name='viewport' content='width=device-width,initial-scale=1' />
    <title>{match.get('title')}</title>
    <link rel='stylesheet' href='/assets/css/style.css'>
    <style>
        .concept-page {{
            max-width: 1000px;
            margin: 0 auto;
            padding: 20px;
        }}
        .concept-header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px 20px;
            border-radius: 8px;
            margin-bottom: 40px;
        }}
        .concept-header h1 {{
            margin: 0;
            font-size: 2.5rem;
        }}
        .concept-content {{
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            line-height: 1.8;
        }}
        .concept-content h2 {{
            color: #667eea;
            margin-top: 40px;
            padding-top: 20px;
            border-top: 2px solid #f0f0f0;
        }}
        .concept-content h3 {{
            color: #764ba2;
            margin-top: 25px;
        }}
        .concept-content pre {{
            background: #f5f5f5;
            padding: 15px;
            border-radius: 6px;
            border-left: 4px solid #667eea;
            overflow-x: auto;
        }}
        .concept-content code {{
            font-family: 'Courier New', monospace;
            font-size: 0.95rem;
        }}
        .concept-content ul {{
            padding-left: 25px;
        }}
        .concept-content li {{
            margin-bottom: 10px;
        }}
        .concept-content a {{
            color: #667eea;
            text-decoration: none;
        }}
        .concept-content a:hover {{
            text-decoration: underline;
        }}
        .breadcrumb {{
            margin-bottom: 20px;
            font-size: 0.9rem;
        }}
        .breadcrumb a {{
            color: #667eea;
            margin-right: 10px;
        }}
        .back-button {{
            display: inline-block;
            background: #667eea;
            color: white;
            padding: 10px 20px;
            border-radius: 6px;
            text-decoration: none;
            margin-bottom: 20px;
        }}
        .back-button:hover {{
            background: #764ba2;
        }}
    </style>
</head>
<body>
    <header>
        <nav>
            <div class='logo'>🚀 Test Automation Hub</div>
            <ul class='nav-menu'>
                <li><a href='/index.html'>Home</a></li>
                <li><a href='/pages/login.html'>Login</a></li>
            </ul>
        </nav>
    </header>

    <div class='concept-page'>
        <a href='/index.html' class='back-button'>← Back to Home</a>
        
        <div class='concept-header'>
            <h1>{match.get('title')}</h1>
            <p style='margin: 10px 0 0 0; font-size: 1.1rem;'>Comprehensive tutorial with examples and best practices</p>
        </div>

        <div class='concept-content'>
            {match.get('content')}
        </div>

        <div style='margin-top: 40px; padding-top: 20px; border-top: 2px solid #f0f0f0; text-align: center; color: #999; font-size: 0.9rem;'>
            <p>Last updated: {match.get('updated_at', 'N/A')}</p>
            <p>© 2025 Test Automation Hub. All rights reserved.</p>
        </div>
    </div>
</body>
</html>
"""
        return Response(content=html, media_type='text/html')
