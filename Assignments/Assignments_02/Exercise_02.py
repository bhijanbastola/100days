"""
Task 01: Create a Book Filtering Function
Question : Book Keeper

Following the data below , complete the given Tasks :

# A list of tuples, where each tuple contains information about a book: (title, genre, year_published, times_borrowed).

books = [
    ("The Alchemist", "Fiction", 1988, 250),
    ("The Da Vinci Code", "Mystery", 2003, 300),
    ("A Brief History of Time", "Science", 1988, 150),
    ("The Theory of Everything", "Science", 2002, 100),
    ("Pride and Prejudice", "Fiction", 1813, 200),
    ("To Kill a Mockingbird", "Fiction", 1960, 180),
    ("The Catcher in the Rye", "Fiction", 1991, 220),
    ("Angels & Demons", "Mystery", 2000, 210),
    ("The Grand Design", "Science", 2010, 90),
    ("1984", "Fiction", 1949, 190)
]
Task 01: Create a Book Filtering Function

Given the list books as shown below, write a Python 
function named filter_books that filters books based on genre 
and publication year. 
The function should take two parameters: genre (a string) and year (an integer). 
It should return a list of book titles that match the given genre and have been published on or after the specified year.

Example usage : print(filter_books("Fiction", 1980))
Expected output: ['The Alchemist', 'The Catcher in the Rye']
Try to use List Comprehension with If condition
"""


#SOLUTION
books = [
    ("The Alchemist", "Fiction", 1988, 250),
    ("The Da Vinci Code", "Mystery", 2003, 300),
    ("A Brief History of Time", "Science", 1988, 150),
    ("The Theory of Everything", "Science", 2002, 100),
    ("Pride and Prejudice", "Fiction", 1813, 200),
    ("To Kill a Mockingbird", "Fiction", 1960, 180),
    ("The Catcher in the Rye", "Fiction", 1991, 220),
    ("Angels & Demons", "Mystery", 2000, 210),
    ("The Grand Design", "Science", 2010, 90),
    ("1984", "Fiction", 1949, 190)
]





def filter_books(genres :str, years: int )->list:
    return [ name for name,genre,year,_ in books if genre.lower()==genres.lower().strip() and year>=years]



while True:
    genre=input("Enter the genre of the book : ").lower().strip()
    year=int(input("Enter the year of the book : "))
    filter_books(genre,year)
    print(filter_books(genre,year))
    print("Do you want to continue ? (y/n)")
    choice=input().lower().strip()
    if choice=='n':
        break   


#######################################################################################
"""
Task 02:Using lamda expression to sort the names of book based on published year in ascending order 

"""
def sort_books_by_year(books):

    
    return [name for name,_,_,_ in sorted(books,key=lambda x:x[2])]

        


print(sort_books_by_year(books))