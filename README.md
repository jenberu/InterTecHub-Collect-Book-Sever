
Book Collection API

Overview

The Book Collection API is a Django-based RESTful service for managing books in a collection. Users can perform CRUD operations, mark books as favorites, and retrieve personalized book recommendations. The system implements Role-Based Access Control (RBAC) to securely manage permissions for Admin and User roles.

Features

Role-Based Access Control (RBAC)

Admin: Full access to manage books and users.

User: Limited access to view, add, and mark books as favorites.

CRUD Operations

GET /books: Fetch all books.

POST /books: Add a new book.

PUT /books/:id: Update an existing book by ID.

DELETE /books/:id: Remove a book by ID.

Favorites and Recommendations

POST /books/favorite/: Mark a book as a favorite.

GET /books/recommendations: Suggest a random book from the collection.

Installation and Setup

1. Clone the Repository

git clone https://github.com/jenberu/InterTecHub-Collect-Book-Sever
cd InterTecHub-Collect-Book-Sever

2. Set Up a Virtual Environment

python -m venv venv

source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt

4. Apply Database Migrations

python manage.py makemigrations

python manage.py migrate

5. Run the Development Server

python manage.py runserver

Authentication

JWT Token Generation

Sign Up: Access /accounts/register/ to create an account.

Log In: Use /accounts/login/ to log in.

Generate Tokens:

POST /api/token/ with your username and password to receive:

Access Token

Refresh Token
POST /api/token/refresh/ to refresh the access token.

Using Tokens for Protected Routes

Include the access token in the Authorization header for secure endpoints

Authorization: Bearer <your_access_token>

https://chromewebstore.google.com/detail/modheader-modify-http-hea/idgpnmonknjnojddfkpgkljpfnnfcklj?hl=en
Install ModHeader Extension.

Add Authorization: Bearer <your_access_token> as a header for your requests.
Validation Rules

Title: Must not contain numbers.

Author: Must not contain numbers.

ISBN: Exactly 13 characters.

Published Year: Between 1900 and 2024

Endpoints

Public Endpoints

GET /books: Fetch all books.

POST /books/: Add a new book.

Admin-Specific Endpoints

GET /books/all: Fetch all books in the system.

PUT /books/:id: Update any book by ID.

DELETE /books/:id: Remove any book by ID.

Favorites and Recommendations

POST /books/favorite/: Mark a book as a favorite.

GET /books/recommendations: Fetch random book suggestions.

Testing

Use Postman or similar API testing tools.

Test endpoints with various payloads to validate functionality and error handling.

Future Improvements

Add advanced filtering and search options.

Implement a recommendation engine based on user preferences.

Introduce user authentication and role-based authorization for enhanced security.
