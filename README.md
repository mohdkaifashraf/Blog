# Kaif Blog

A Django-based blog with public post browsing, category navigation, search, comments, and a dashboard for managing blog content and users.

## Features

- Browse published posts and featured posts.
- Filter posts by category and search published content.
- Read blog posts and add comments when signed in.
- Register and sign in to an account.
- Manage categories, posts, and users from the dashboard.
- Upload featured images for posts.
- Render a branded, responsive 404 page for missing pages.

## Requirements

- Python 3.12 or newer
- pip

The project uses Django 6.1.1, SQLite, Pillow, and django-crispy-forms with the Bootstrap 5 template pack. See [`requirements.txt`](requirements.txt) for the complete dependency list.

## Setup on Windows

Open PowerShell in the project directory and run:

```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

The deployed site is available at <https://kaif.pythonanywhere.com>.

The virtual environment activation command for Command Prompt is:

```bat
venv\Scripts\activate.bat
```

## Project Layout

- `blog_main/` - Django project settings, URL configuration, and shared views.
- `blogs/` - Blog models, public views, templates support, and migrations.
- `dashboards/` - Dashboard views, forms, models, and migrations.
- `templates/` - Shared, public, authentication, and dashboard templates.
- `static/` - CSS and image assets.
- `media/` - Uploaded post images during local development.
- `db.sqlite3` - SQLite database configured for local development.

## Useful Commands

```powershell
python manage.py check
python manage.py test
python manage.py collectstatic
```

`python manage.py test` currently discovers no tests.

## Deployment Notes

The checked-in settings are for local development (`DEBUG=True` and SQLite). Before deploying:

- Set `DEBUG=False` and configure `ALLOWED_HOSTS` for the deployment domains.
- Provide a new `SECRET_KEY` through a protected environment variable; do not use a development key in production.
- Configure a production database and secure database credentials.
- Run migrations and `python manage.py collectstatic` as part of deployment.
- Serve static assets and uploaded media using an appropriate production web server or storage service. Django's development server is not for production.
- Keep the custom 404 handler enabled and verify missing URLs return HTTP 404 after deployment.
