# Cashier System Backend - Django

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Getting Started](#getting-started)
5. [Project Structure](#project-structure)
6. [Usage](#usage)
7. [Database](#database)


---

## Introduction

The Cashier System Backend is a Django-based application that provides the server-side functionality for a cashier system. This system is designed to help manage sales and inventory in a retail or business environment. It offers various features to facilitate the cashier's tasks and provides RESTful APIs for easy integration.

## Features

- User authentication and authorization system.
- Product management with CRUD operations.
- Inventory management to track product quantities.
- Role-based access control for different user types (cashiers, managers, admins, etc.).

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6+
- Django 3.0+
- Django Rest Framework (DRF)
- PostgreSQL or another compatible database
- Virtual environment (recommended)

## Getting Started

1. **Clone the repository:**

   ```bash
   git clone git@github.com:Sara-Alkhateeb/Cashier-System.git

2. **Create a virtual environment and activate (optional but recommended):**
    python -m venv .venv
    activate: source .venv/bin/activate

3. **Install the project dependencies:** 
    pip install -r requirements.txt

4. **Run the development server:**
    python manage.py runserver


## Project Structure
            cashier_system/
        │
        ├── cashier_app/            # Main application folder
        │   ├── migrations/         # Database migration files
        │   ├── admin.py            # Admin panel configurations
        │   ├── models.py           # Database models
        │   ├── serializers.py      # API serializers
        │   ├── views.py            # API views and logic
            |__ urls.py             # App-level URLs routing
        │
        ├── cashier_system/         # Project settings and configurations
        │   ├── settings.py         # Django settings
        │   ├── urls.py             # Project-level URL routing
        │
        ├── static/                  # Static files (CSS, JavaScript, etc.)
        ├── templates/               # HTML templates
        ├── .env                     # Environment variables (not in the repository)
        ├── manage.py                # Django management script
        └── requirements.txt         # Project dependencies

## Usage
    To use the Cashier System Backend, you can interact with it through the provided RESTful APIs. You can integrate these APIs with your front-end application to build a complete cashier system.

## Database
    The default database used in this project is PostgreSQL. You can configure the database settings in the .env file. Make sure to run database migrations (python manage.py migrate) after making changes to the database settings.

## Useful Url:
    Products list + Add product:  /api/products/
    View product details + Edit + delete : /api/products/{id}
    Adminstration : http://127.0.0.1:8000/admin/
    Create transactions : /api/transactions/create/
    Transections report : /api/transactions/report/
    Filtered transactions : by cashier : /api/transactions/filtered/?cashier_id=1
                            by date range : /api/transactions/filtered/?start_date=2023-09-01&end_date=2023-09-30 
