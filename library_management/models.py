from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
    name = models.CharField(max_length=200,
                            help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")
    def __str__(self):
        return self.name

##relation containing language of books
class Language(models.Model):
    name = models.CharField(max_length=200,
                            help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)")
    def __str__(self):
        return self.name

class Book(models.Model):
    isbn = models.CharField(max_length=13, primary_key=True,
                            help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    summary = models.CharField(max_length=1000)
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    language = models.ForeignKey(Language, on_delete=models.SET_NULL , null= True)
    total_copies = models.IntegerField()
    available_copies = models.IntegerField()

    def __str__(self):
        return self.title

class Student(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    total_books_due = models.IntegerField(default=0)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Borrower(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date = models.DateTimeField(null=True, blank=True)
    return_date = models.DateTimeField(null=True, blank=True)
    issued_by = models.ForeignKey(User, on_delete=models.CASCADE)
    returned_to = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='returned_to', null=True, blank=True)
    returned = models.BooleanField(default=False)

    def __str__(self):
        return self.student.name + " borrowed " + self.book.title
