📦 In-Memory Django CRUD API

A lightweight Django 4.2 backend that performs pure in-memory CRUD operations (no database, no migrations, no ORM).
Perfect for demos, prototypes, or learning API basics.

🚀 Features

✅ No database required — all data lives in Python memory

✅ No migrations — Django runs without creating any DB tables

✅ Simple CRUD API using pure Python lists

✅ Zero external dependencies (only Django)

✅ Fast to run & restart

❗ Data resets automatically on each server restart (because it's in-memory)

🗂 Project Structure
inmemory_crud/
├── manage.py
├── requirements.txt
├── inmemory_crud/
│   ├── __init__.py
│   ├── settings.py       ← No migrations needed
│   ├── urls.py
└── api/
    ├── __init__.py
    ├── urls.py
    ├── views.py          ← In-memory CRUD logic

⚙️ Requirements

Python 3.11+

Django 4.2.*

Install requirements:

pip install -r requirements.txt

▶️ Run the Server
python manage.py runserver


Server will start at:

http://127.0.0.1:8000/

📡 API Endpoints (CRUD)

Base URL:

http://127.0.0.1:8000/api/items/


All data is stored inside a global list in views.py.

➕ Create Item

POST /api/items/

Body:

{
  "title": "My Item",
  "description": "Some description"
}


Response (201):

{
  "id": 1,
  "title": "My Item",
  "description": "Some description"
}

📄 List All Items

GET /api/items/

Response:

[
  {
    "id": 1,
    "title": "My Item",
    "description": "Some description"
  }
]

🔍 Get Single Item

GET /api/items/<id>/

📝 Update Entire Item

PUT /api/items/<id>/

{
  "title": "Updated title",
  "description": "Updated details"
}

✏️ Partial Update

PATCH /api/items/<id>/

{
  "description": "Changed only this"
}

🗑 Delete Item

DELETE /api/items/<id>/

Response:

{"detail": "deleted"}

🛠 How It Works (In-Memory Logic)

Inside api/views.py:

ITEMS = []
NEXT_ID = 1


Every new item gets appended to this list.
No database, no models, no ORM — just plain Python.

📌 Notes

Data is cleared on every server restart.

No DB file is created because settings.py uses:

"NAME": ":memory:"


Suitable for: demos, PoC, tutorials, interview tasks.