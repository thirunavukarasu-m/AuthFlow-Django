# AuthFlow-Django

#### ✅ Features

* JWT-based Auth (Login, Signup, Logout, Refresh)
* Product CRUD (Create, Read, Update, Delete)
* Secure access with access/refresh tokens via headers

#### 🏗️ Setup Instructions

```bash
git clone <repo-url>
cd backend
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

#### 🔐 Auth Endpoints

| Endpoint      | Method | Description          | Auth Required |
| ------------- | ------ | -------------------- | ------------- |
| /api/signup/  | POST   | Register a user      | ❌             |
| /api/login/   | POST   | Login and get tokens | ❌             |
| /api/refresh/ | POST   | Get new access token | ❌             |
| /api/logout/  | POST   | Logout + blacklist   | ✅             |

#### 🛍️ Product Endpoints

| Endpoint            | Method | Description       | Auth Required |
| ------------------- | ------ | ----------------- | ------------- |
| /api/products/      | GET    | List all products | ✅             |
| /api/products/      | POST   | Add new product   | ✅             |
| /api/products/<id>/ | PUT    | Update product    | ✅             |
| /api/products/<id>/ | DELETE | Delete product    | ✅             |

#### 🔑 Token Usage

Send access token in the header:

```
Authorization: Bearer <access_token>
```

---