README: Book Collection API
Overview
This  Book Collection API is a Django-based RESTful service for managing books in a collection. Users can create, read, update, and delete book records.
 Additionally, users can mark books as their favorites and retrieve personalized book recommendations.
 CRUD Operations:

Installation
1.Clone the repository:
git clone https://github.com/jenberu/InterTecHub-Collect-Book-Sever
cd book-collection
2.Set up a virtual environment:
python -m venv venv
source venv/bin/activate  
# On Windows: venv\Scripts\activate
3.Install dependencies:
pip install -r requirements.txt

4.Apply database migrations:
python manage.py makemigrations
python manage.py migrate
5.Run the development server:
python manage.py runserver

Validation Rules
Title: Must not contain numbers.
Author: Must not contain numbers.
ISBN: Must be exactly 13 characters long.
Published Year: Must be between 1900 and 2024.

End points

GET /books: Fetch all books.
POST /books: Add a new book.
PUT /books/:id: Update an existing book by ID.
DELETE /books/:id: Remove a book by ID.
Favorite Books:

POST books/favorite/: Mark a book as a favorite.

Custom Endpoints:

GET /books/recommendations: Suggest a random book from the collection.
GET /books/favorites:  Mark a book as a favorite.

Testing
1.Install Postman or a similar API testing tool.
2.Use the endpoints with the appropriate HTTP methods and request bodies.
3.Test the validation logic by providing invalid inputs for fields like title, author, isbn, and published_year.


Example Requests
Create a Book:
POST /books/
Content-Type: application/json

{
    "title": "Django for Beginners",
    "author": "Jembeu kassie",
    "isbn": "1234567890123",
    "published_year": 2020
}

Mark a Book as Favorite:


POST /mark-favorite/
Content-Type: application/json

{
    "book_id": 1
}


Future Improvements
Add user authentication and authorization for secure access.
Implement advanced filtering and search for books.
Extend the recommendation engine to suggest books based on user preferences.


Developed by Jemberu Kassie
Email: jemberu0970@gmail.com
Location: Bahir Dar, Ethiopia