#-------------------------------------------------------------------------------
# HA5_class
# Student Name: 
# Python version: 
# Submission Date: 99/99/9999
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines as set forth by the
# instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: 
#-------------------------------------------------------------------------------
# Notes to grader: 
#-------------------------------------------------------------------------------
# NOTE: width of source code should be < 80 characters to facilitate printing
#-------------------------------------------------------------------------------
class InvalidItem(Exception):
    def __str__(self):
        return 'Item not found!'

class BookList(list):
    def search(self, key, search_criteria):
        for book in self:
            if search_criteria == 't': #search by title
                if key.lower() == book.title.lower():
                    return book
            elif search_criteria == 'i': #search by isbn
                if key == book.isbn:
                    return book
            elif search_criteria == 'k': #search by keyword
                if key.lower() in book.title.lower():
                    return book
        return False
            
class Book(object):
    all_books = BookList()
    def __init__(self, genre, isbn,title, author, stack):
        self.genre = genre
        self.isbn = isbn
        self.title = title
        self.author = author
        self.stack = stack
        Book.all_books.append(self)

    def __str__(self):
        return 'ISBN #: {}\nTitle: {}\nGenre: {}\nAuthor: {}\nStack :{}\n'.format(\
    	self.isbn, self.title, self.genre, self.author, self.stack)
    
class Novel(Book):
    def __init__(self, genre, isbn,title, author, stack, sub_genre):
        super().__init__(genre, isbn, title, author, stack)
        self.sub_genre = sub_genre[0] #mystery, historic
        
    def __str__(self):
        return super().__str__() + 'Sub-genre: {}\n'.format(self.sub_genre)
        
        
class Scifi(Book):
    def __init__(self, genre, isbn,title, author,  stack, movie_night_date):
        super().__init__(genre, isbn, title, author, stack)
        if movie_night_date[0] == 'No upcoming movie':
        	self.date = 'No upcoming movie' #date of upcoming movie night
        	self.location = 'No location information'
        else:
        	self.date, self.location = movie_night_date
    
    def __str__(self):
        return super().__str__() + 'Movie date: {} and location:{}'.format(self.date, self.location)



def main():
    
    with open('library.txt') as f:
    #process input file and creating Book objects
        for line in f:
            line =  line.split(',')
            genre,isbn,title,author, stack = line[:5]
            additional_info = line[5:]
            #print(additional_info)
            if genre == 'Novel': #create a novel object
                n = Novel(genre,isbn,title,author, stack, additional_info)
            elif genre == 'Scifi': #create a scifi object
                s = Scifi(genre,isbn,title,author, stack, additional_info)
            
    
        
main() 
        
        
    
