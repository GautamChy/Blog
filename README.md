# 📝 Blog Platform with Commenting System

A Django-based blog platform where users can read, create, and manage blog posts, leave comments, and explore content using filters and search.
The project also includes RESTful API support with Swagger documentation.

## 🚀 Features Included.

1) ✅ Create, Read, Update, Delete (CRUD) for posts, categories, comments, and tags
2) 🏷️ Data filtering and searching:
      * Allow users to search blog posts by title,category,or author.
      * Filter posts by tags or pub;ication data.
3) 📄 Data Pagination:
      * Paginate blog posts and comment threads for easier navigation.
4) 🔐 Authentication:
      * Use Django's built-in authentication for secure login and registration.
      * ⚙️ Role_based access: Authors manage their posts,and readers manage their profile and comments.
5) Testing and API Documentation:
   * 🧾 Swagger API documentation using `drf-spectacular`

6)  💬 Commenting system for each post

- 📂 Modular structure using Django apps and Django REST Framework (DRF)

-------------------------------------------------

## 🛠️ Tech Stack

- Backend: Django, Django REST Framework
- Database: SQLite (can be switched to PostgreSQL/MySQL)
- API Docs: drf-spectacular (Swagger UI)
- Auth: Django’s built-in authentication

---

## 📂 Project Structure

```bash
BlogPCS/
├── blog_app/              # App for blog, posts, comments
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
├── user_app/              # App for user login/register   
├── project/               # Django project settings
│   └── urls.py
└── manage.py
