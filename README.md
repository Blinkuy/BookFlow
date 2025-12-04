# BookFlow

<div align="center">

*Project tech stack*

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat\&logo=python\&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-092E20?style=flat\&logo=django\&logoColor=white)](https://www.djangoproject.com/)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat\&logo=sqlite\&logoColor=white)](https://www.sqlite.org/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat\&logo=html5\&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat\&logo=css3\&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
</div>

---

## 📋 Project Overview

**BookFlow** is a simple web application for managing a library booking system. It allows users (or librarians) to manage books, perform bookings, returns, and other basic library operations through a web interface.

---

## 🛠 Technologies

* **Python + Django** — backend web framework, routing, ORM and templating
* **SQLite** — default database (can be configured otherwise)
* **HTML, CSS, JS** — frontend interface using Django templates / static files
* Dependencies managed via `requirements.txt`

---

## 🚀 Installation and Running

### Requirements

* Python 3.11.9
* `pip`

### 1. Clone the repository

```bash
git clone https://github.com/Blinkuy/BookFlow.git
cd BookFlow
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Apply migrations (if project uses Django migrations) and run server

```bash
python manage.py migrate
python manage.py runserver
```

After that the app will be accessible at **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)** (check console).

---

