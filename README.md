# Django REST API Practical

A beginner-friendly Django project for learning the fundamentals of Django and Django REST Framework through practical examples.

## 🚀 Features

* Django 6.0.6
* Django REST Framework 3.17.1
* django-filter 25.2
* Basic URL routing
* Function-based views
* HTML response using `HttpResponse`

## 📂 Project Structure

```text
algorithm/
│── manage.py
│── db.sqlite3
│
├── algorithm/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   ├── wsgi.py
│   └── __init__.py
│
├── algoapp/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   └── __init__.py
│
├── README.md
└── requirements.txt
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Sumitra29/django-practical.git
```

Navigate to the project directory:

```bash
cd django-practical/algorithm
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## ▶️ Run the Development Server

```bash
python manage.py runserver
```

Open your browser:

```text
http://127.0.0.1:8000/api/
```

## 📌 Available Endpoint

| Method | Endpoint | Description                                            |
| ------ | -------- | ------------------------------------------------------ |
| GET    | `/api/`  | Returns algorithm book information as an HTML response |

### Sample Response

```html
<h2>
book_name: Grokking Algorithms
<br>
author_name: Aditya Y. Bhargava
<br>
edition: 2
</h2>
```

## 🛠 Technologies Used

* Python
* Django 6.0.6
* Django REST Framework
* SQLite

## 📖 What I Learned

* Creating a Django project
* Creating a Django app
* URL routing
* Function-based views
* Returning an HTML response using `HttpResponse`

## Practical Project Demo
<p align="center">
  <img src="1.gif" width="45%" alt="Voice-Automation">
</p>
<p align="center">
  <em>Django REST-API using HTML</em>
</p>

## 👨‍💻 Author

**Sumitra**
