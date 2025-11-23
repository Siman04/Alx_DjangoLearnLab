# api_project

This project demonstrates a minimal Django + Django REST Framework setup.

- `rest_framework` and `rest_framework.authtoken` are added to `INSTALLED_APPS`.
- `api` app contains a `Book` model, a `BookSerializer`, `BookList` view, and `BookViewSet`.
- Token authentication endpoint is available at `api/api-token-auth/`.

To run locally:

```bash
cd api_project
pip install django djangorestframework djangorestframework-authtoken
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

API endpoints:

- `api/books/` — ListAPIView (BookList)
- `api/books_all/` — Router-based ViewSet endpoints (list, retrieve, create, update, destroy)
- `api/api-token-auth/` — Token retrieval endpoint
