# My Library Book Organiser

# Step 1: Create a list of books
books = ["The Alchemist", "1984", "To Kill a Mockingbird", "Pride and Prejudice"]

print("Initial Book List:", books)

# Step 2: Perform list operations
# Adding a book
books.append("The Great Gatsby")
print("\nAfter Adding a Book:", books)

# Removing a book
books.remove("1984")
print("After Removing a Book:", books)

# Sorting books
books.sort()
print("Sorted Book List:", books)

# Reversing books
books.reverse()
print("Reversed Book List:", books)

# Indexing
print("Book at index 2:", books[2])

# Slicing
print("First three books:", books[:3])

# Step 3: Create a dictionary for librarian details
librarian = {
    "name": "Aparna Desai",
    "employee_id": "LIB123",
    "shift": "Morning",
    "contact": "aparna.desai@library.com"
}

print("\nLibrarian Details:", librarian)

# Dictionary operations
# Accessing a value
print("Librarian Name:", librarian["name"])

# Updating a value
librarian["shift"] = "Evening"
print("Updated Librarian Details:", librarian)

# Adding a new key-value pair
librarian["experience_years"] = 5
print("After Adding Experience:", librarian)

# Removing a key-value pair
del librarian["contact"]
print("After Removing Contact:", librarian)

# Step 4: Convert two lists into a book directory using dict() and zip()
book_titles = ["The Alchemist", "To Kill a Mockingbird", "Pride and Prejudice", "The Great Gatsby"]
book_authors = ["Paulo Coelho", "Harper Lee", "Jane Austen", "F. Scott Fitzgerald"]

book_directory = dict(zip(book_titles, book_authors))
print("\nBook Directory (Title → Author):", book_directory)
