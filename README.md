# In-memory Flask CRUD API (No DB)

Python 3.11  
Flask 2.3.x

This is a minimal Flask backend that exposes simple CRUD operations
over an in-memory store (a Python dict). **No database is used** and
everything resets whenever you restart the server.

## 1. Setup

```bash
python -m venv venv
# Windows: venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

pip install -r requirements.txt
```

## 2. Run the server

```bash
python app.py
```

Server will start at: <http://127.0.0.1:5000/>

## 3. API endpoints

Base path: `/items`

### List items

**GET** `/items`

### Create item

**POST** `/items`

Body:

```json
{
  "name": "First Item",
  "description": "My first in-memory item"
}
```

### Retrieve single item

**GET** `/items/<id>`

Example: `/items/1`

### Update item

**PUT** `/items/<id>`

Body (fields optional, missing fields keep old values):

```json
{
  "name": "Updated name",
  "description": "Updated description"
}
```

### Delete item

**DELETE** `/items/<id>`

Response (204 No Content):

```json
{
  "message": "Item deleted."
}
```

## 4. Notes

- Storage is a simple in-memory Python dictionary (`ITEMS`) in `app.py`.
- A few sample items are hard-coded on startup so that `/items` already
  returns data.
- When you stop and start the server, all runtime changes are cleared
  and the data is reset to the initial hard-coded values.
