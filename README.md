# 🧳 Lost & Found Backend (Django REST API)

This repository contains the **backend API** for a Lost & Found board application.  
Users can post lost or found items, view item details, and communicate securely with item owners via an internal messaging system.

Built with **Django**, **Django REST Framework**, and **Token Authentication**.

---

## 🚀 Features

- 🔐 User registration & login with token authentication
- 📦 Create, view, update, and delete lost/found items
- 🖼 Upload images for items
- 🔎 Filter items by status (`lost` or `found`)
- 💬 Messaging system between users
- 📥 Inbox & conversation threads
- 👮 Permissions: only item owners can edit/delete their items

---

## 🛠 Tech Stack

- Python
- Django
- Django REST Framework
- Django REST Framework Authtoken
- SQLite (default, can be swapped)
- Pillow (for image uploads)

---

## 📂 Project Structure (Simplified)
lostandfoundboard/
├── items/
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ └── permissions.py
├── users/
│ ├── models.py
│ └── views.py
├── media/
├── manage.py
└── requirements.txt


**📡 API Endpoints**
**🔐 Authentication**
| Method | Endpoint         | Description               | Auth Required |
| ------ | ---------------- | ------------------------- | ------------- |
| POST   | `/api/register/` | Register a new user       | ❌ No          |
| POST   | `/api/login/`    | Obtain auth token (login) | ❌ No          |

**📦 Items (Lost & Found)**
| Method | Endpoint               | Description                  | Auth Required |
| ------ | ---------------------- | ---------------------------- | ------------- |
| GET    | `/items/`              | Get all items (lost & found) | ❌ No          |
| GET    | `/items/?status=lost`  | Get only lost items          | ❌ No          |
| GET    | `/items/?status=found` | Get only found items         | ❌ No          |
| GET    | `/items/{id}/`         | Get item by ID               | ❌ No          |
| POST   | `/items/`              | Create a new item            | ✅ Yes         |
| PUT    | `/items/{id}/`         | Update an item               | ✅ Owner only  |
| PATCH  | `/items/{id}/`         | Partially update an item     | ✅ Owner only  |
| DELETE | `/items/{id}/`         | Delete an item               | ✅ Owner only  |

**💬 Messaging**
| Method | Endpoint                                 | Description                                 | Auth Required |
| ------ | ---------------------------------------- | ------------------------------------------- | ------------- |
| GET    | `/messages/`                             | Get all messages involving the user (Inbox) | ✅ Yes         |
| GET    | `/messages/?item={itemId}&user={userId}` | Get conversation for a specific item & user | ✅ Yes         |
| POST   | `/messages/`                             | Send a new message                          | ✅ Yes         |
| POST   | `/messages/mark_read/`                   | Mark messages as read for a conversation    | ✅ Yes         |
