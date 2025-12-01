# In-memory Django CRUD API

Python 3.11  
Django 4.2 (any 4.2.x)

This is a minimal backend-only Django project that exposes simple CRUD
operations over an in-memory store (a Python dict). **No database writes**
are used for the CRUD — data resets every time you restart the server.

## 1. Setup

```bash
python -m venv venv
# Windows: venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

pip install -r requirements.txt
```

## 2. Run migrations (optional but recommended)

Even though the CRUD is fully in-memory, Django's auth/admin apps use the
default SQLite DB. Running migrations once avoids warnings:

```bash
python manage.py migrate
```

## 3. Run the dev server

```bash
python manage.py runserver
```

Server will start at: <http://127.0.0.1:8000/>

## 4. API endpoints

Base path for the API is `/api/`.

### List items

**GET** `/api/items/`

Response:

```json
[
  {
    "id": 1,
    "name": "First Item",
    "description": "My first in-memory item"
  }
]
```

### Create item

**POST** `/api/items/`

Body:

```json
{
  "name": "First Item",
  "description": "My first in-memory item"
}
```

### Retrieve single item

**GET** `/api/items/<id>/`

Example: `/api/items/1/`

### Update item

**PUT** `/api/items/<id>/`

Body (fields optional, missing fields keep old values):

```json
{
  "name": "Updated name",
  "description": "Updated description"
}
```

### Delete item

**DELETE** `/api/items/<id>/`

Response (204 No Content):

```json
{
  "message": "Item deleted."
}
```

## 5. Notes

- Storage is a simple in-memory Python dictionary (`ITEMS`) in `api/views.py`.
- When you stop and start `runserver`, all items are cleared.
- You can extend this pattern to other entities or later switch to real
  Django models and a database with the same URL structure.
