# In-memory Django CRUD API (No DB / No Migrations)

Python 3.11  
Django 4.2 (any 4.2.x)

This is a minimal backend-only Django project that exposes simple CRUD
operations over an in-memory store (a Python dict). **No database is used**
and you **do not need to run any migrations**.

Everything is kept in memory and resets whenever you restart the server.

## 1. Setup

```bash
python -m venv venv
# Windows: venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

pip install -r requirements.txt
```

## 2. Run the dev server (no migrations needed)

```bash
python manage.py runserver
```

Server will start at: <http://127.0.0.1:8000/>

## 3. API endpoints

Base path for the API is `/api/`.

### List items

**GET** `/api/items/`

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

## 4. Notes

- Storage is a simple in-memory Python dictionary (`ITEMS`) in `api/views.py`.
- A few sample items are hard-coded on startup so that `/api/items/` already
  returns data.
- When you stop and start `runserver`, all runtime changes are cleared and
  the data is reset to the initial hard-coded values.
