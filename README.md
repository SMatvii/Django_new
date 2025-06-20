# Django_new

**Django_new** is a small Django-based project that implements a simple e-commerce catalog with user registration, authentication, and profile management.

---

## Features

- **Product catalog** with filters (category, price range, rating, search by name, sorting)
- **Product detail page** with images, description, stock, price, discounts, and attributes
- **Shopping cart** functionality
- **User registration/authentication**, profile page and profile editing, email confirmation
- **Responsive interface** using Bootstrap 5

---

## Project Structure

```
catalog/
├── accounts/             # User registration, login, and profile logic
├── products/             # Product models, templates, and views
│   ├── templates/
│   └── _views/
├── catalog/              # Django settings, urls, wsgi/asgi
├── manage.py             # Django launcher
└── requirements.txt      # Project dependencies
```

---

## Technologies Used

- **Python 3.10+**
- **Django 5.1.6**
- **Other Django ecosystem packages** as needed

---

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/SMatvii/Django_new.git
cd Django_new/catalog
```

### 2. Create and activate virtual environment

**On Unix/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```
**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file in the `catalog/` directory and add your secret key:

```
SECRET_KEY=your_secret_key
```

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Run the development server

```bash
python manage.py runserver
```

---

## Useful Templates

- **index.html** — main catalog page with filters
- **product_details.html** — product detail view
- **register.html** — user registration form
- **about.html** — "About Us" page

---
