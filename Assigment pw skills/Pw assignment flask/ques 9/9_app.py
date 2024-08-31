from flask import Flask, jsonify, request

app = Flask(__name__)

#Dummy data for books
books = [
    {"id": 1, "Five point someone": "Book 1", "author": "Chetan Bhagat"},
    {"id": 2, "Karmyog": "Book 2", "author": "Swami Vivekanand"}
]

#GET all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

#GET single book
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    for book in books:
        if book['id'] == book_id:
            return jsonify(book)
    return jsonify({"message": "Book not found"}), 404

# POST new book
@app.route('/books', methods=['POST'])
def create_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(new_book), 201

# PUT update book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    for book in books:
        if book['id'] == book_id:
            book.update(request.get_json())
            return jsonify(book)
    return jsonify({"message": "Book not found"}), 404

# DELETE book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    for index, book in enumerate(books):
        if book['id'] == book_id:
            del books[index]
            return jsonify({"message": "Book deleted"})
    return jsonify({"message": "Book not found"}), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8000)