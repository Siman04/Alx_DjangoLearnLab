Social Media API
================

Minimal Django REST Framework-based Social Media API scaffold.

Setup
-----

1. Create and activate a virtual environment (recommended).
2. Install requirements:

```bash
pip install -r requirements.txt
```

3. Run migrations and create a superuser:

```bash
cd social_media_api
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

4. Run the development server:

```bash
python manage.py runserver
```

API Endpoints (initial)
-----------------------
- `POST /api/accounts/register/` — Register a new user. Returns token.
- `POST /api/accounts/login/` — Login with username/password. Returns token.
- `GET/PUT /api/accounts/profile/` — Retrieve/update authenticated user's profile.
- `GET /api/posts/posts/` — List posts.
- `POST /api/posts/posts/` — Create post (authenticated).
- `GET/POST /api/posts/comments/` — Comment CRUD via router.
- `GET /api/notifications/` — List notifications for authenticated user.

Notes
-----
- This scaffold is for development and demonstration. Replace `SECRET_KEY` and set `DEBUG=False` for production.
- You should run `python manage.py makemigrations` after adding apps to create migration files.
