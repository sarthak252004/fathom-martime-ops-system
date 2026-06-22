# Fathom Maritime Operations & Compliance System

This is a backend API project made for managing ship maintenance, safety drills, and compliance monitoring for marine organizations.

## Tech Stack
* Backend: FastAPI (Python)
* Database: PostgreSQL and SQLAlchemy ORM

## Why we chose these tools:
* FastAPI is fast, has automatic Swagger docs, and works well with SQLAlchemy.
* PostgreSQL is good for relational data and lets us use JSON fields for notes and attendance.
* SQLAlchemy ORM makes database models and migrations easier.
* CORS Middleware is added for when we build a frontend later.

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/sarthak252004/fathom-martime-ops-system.git(https://github.com/sarthak252004/fathom-martime-ops-system.git)
cd fathom-martime-ops-system
# install the requirements
pip install -r requirements.txt

# Database Config:
# Go to database.py and change DATABASE_URL to your own PostgreSQL details
# postgresql://username:password@localhost/dbname

# Start the server
uvicorn main:app --reload
