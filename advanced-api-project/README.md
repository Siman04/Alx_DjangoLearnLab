# advanced-api-project

This project demonstrates advanced Django REST Framework usage with custom serializers, nested relationships, generic views, filtering, searching, ordering, and tests.

Structure:
- `api` app contains `models.py`, `serializers.py`, `views.py`, `urls.py`, and `test_views.py`.

Key features:
- `Author` and `Book` models with a ForeignKey relationship (`author` -> `books`).
- `BookSerializer` with custom validation for `publication_year` (cannot be in the future).
- `AuthorSerializer` includes a nested `BookSerializer` for `books`.
- Generic views for list/create and retrieve/update/destroy; filtering/searching/ordering enabled.

Run locally:

```bash
cd advanced-api-project
pip install django djangorestframework django-filter
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Run tests:

```bash
python manage.py test api
```
