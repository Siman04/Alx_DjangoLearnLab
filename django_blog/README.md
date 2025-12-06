# Django Blog Project

This is a comprehensive Django blog application with the following features:

## Features
1. **User Authentication**: Registration, login, logout, and profile management
2. **Blog Post Management**: CRUD operations for blog posts
3. **Comments System**: Users can comment on posts, edit/delete their comments
4. **Tagging System**: Posts can be tagged and filtered by tags
5. **Search Functionality**: Search posts by title, content, or tags

## Installation

```bash
cd django_blog
pip install django
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## URL Patterns

- `/` - Home/Posts list
- `/login/` - User login
- `/logout/` - User logout
- `/register/` - User registration
- `/profile/` - User profile management
- `/posts/new/` - Create new post
- `/posts/<id>/` - View post detail
- `/posts/<id>/edit/` - Edit post
- `/posts/<id>/delete/` - Delete post
- `/posts/<id>/comments/new/` - Add comment
- `/comments/<id>/edit/` - Edit comment
- `/comments/<id>/delete/` - Delete comment
- `/tags/<tag_name>/` - View posts by tag
