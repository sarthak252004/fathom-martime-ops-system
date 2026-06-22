# [cite_start]Fathom Maritime Operations & Compliance System [cite: 1]

[cite_start]This is a backend API project made for managing ship maintenance, safety drills, and compliance monitoring for marine organizations. [cite: 2]

## Tech Stack
* [cite_start]Backend: FastAPI (Python) [cite: 4]
* [cite_start]Database: PostgreSQL and SQLAlchemy ORM [cite: 5]

## Why we chose these tools:
* [cite_start]FastAPI is fast, has automatic Swagger docs, and works well with SQLAlchemy. [cite: 8]
* [cite_start]PostgreSQL is good for relational data and lets us use JSON fields for notes and attendance. [cite: 9]
* [cite_start]SQLAlchemy ORM makes database models and migrations easier. [cite: 10]
* [cite_start]CORS Middleware is added for when we build a frontend later. [cite: 11]

## Setup Instructions

1. Clone the repository:
```bash
git clone [https://github.com/your-username-here/fathom-marine.git](https://github.com/your-username-here/fathom-marine.git)
cd fathom-marine
# install the requirements
pip install -r requirements.txt

# Database Config:
# Go to database.py and change DATABASE_URL to your own PostgreSQL details
# postgresql://username:password@localhost/dbname





# Start the server
uvicorn main:app --reload
