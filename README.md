# Ice Cream Parlor Application

This is a Flask-based web application for managing an ice cream parlor. It allows users to:
- Add and view **seasonal flavors**.
- Add and view **allergens**.
- Manage items in the **cart**.

## Features
- User-friendly interface with a modern theme and gradient backgrounds.
- CRUD operations for seasonal flavors, allergens, and cart management.
- Responsive design with HTML and CSS.

## Prerequisites
Before running the project, make sure you have the following installed:
1. **Python** (3.7 or later)
2. **Flask** and its dependencies
3. **SQLite** for the database

## Installation Steps
1. Clone the repository to your local system:
   ```bash
   git clone https://github.com/Praga-234/ice-cream-parlor.git


ice-cream-parlor/
│
├── app/
│   ├── __init__.py         # Application initialization
│   ├── models.py           # Database models
│   ├── routes.py           # Application routes
│   └── static/             # Static files (CSS, images)
│       ├── style.css       # Stylesheet
│       └── img/            # Background images
│
├── migrations/             # Database migrations
├── run.py                  # Entry point of the application
├── requirements.txt        # List of Python dependencies
└── README.md               # Project documentation

Database Migration:

bash
Copy code
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
Run the Application:
flask run


Access the Application:
http://127.0.0.1:5000/
