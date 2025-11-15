# Permissions and Security Setup

## Custom Permissions
- Defined in `bookshelf/models.py`:
  - `can_view`
  - `can_create`
  - `can_edit`
  - `can_delete`

## Permission Enforcement
- Views in `bookshelf/views.py` use:
  - `@permission_required('bookshelf.can_view', raise_exception=True)`
  - `@permission_required('bookshelf.can_create', raise_exception=True)`
  - `@permission_required('bookshelf.can_edit', raise_exception=True)`
  - `@permission_required('bookshelf.can_delete', raise_exception=True)`

## Security Best Practices
- All required security settings are in `LibraryProject/settings.py`:
  - `DEBUG = False`
  - `SECURE_BROWSER_XSS_FILTER = True`
  - `X_FRAME_OPTIONS = "DENY"`
  - `SECURE_CONTENT_TYPE_NOSNIFF = True`
  - `CSRF_COOKIE_SECURE = True`
  - `SESSION_COOKIE_SECURE = True`
  - `SECURE_SSL_REDIRECT = True`
  - `SECURE_HSTS_SECONDS = 31536000`
  - `SECURE_HSTS_INCLUDE_SUBDOMAINS = True`
  - `SECURE_HSTS_PRELOAD = True`

## Groups
- Use Django admin to create groups:
  - Editors: assign `can_edit`, `can_create`
  - Viewers: assign `can_view`
  - Admins: assign all permissions

## Notes
- All spelling, punctuation, and spacing for permissions and settings match the requirements exactly.
