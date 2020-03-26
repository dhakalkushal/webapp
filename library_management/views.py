from django.shortcuts import render
from django.views import generic
from .models import Book, Borrower, Student
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import redirect, render_to_response, get_object_or_404, render
from .forms import ListForms, StudentForm
from django.urls import reverse
from django.utils import timezone

# Create your views here.
class ListBooks(generic.ListView):
    template_name = "library_management/book_index.html"

    def get_queryset(self):
        return Book.objects.all()

class ListBorrowers(generic.ListView):
    template_name = "library_management/borrower_index.html"

    def get_queryset(self):
        #return Borrower.objects.all()
        return Borrower.objects.filter(returned=False)

class ListStudent(generic.ListView):
    template_name = "library_management/student_index.html"

    def get_queryset(self):
        return Student.objects.all()

def book_detail(request, pk):
    book = get_object_or_404(Book, pk= pk)
    context = {
        'book' : book,
    }
    return render(request,'library_management/book_detail.html', context)

def student_detail(request, pk):
    student = get_object_or_404(Student, pk = pk)
    context = {
        'student' : student,
    }
    return render(request, 'library_management/student_detail.html', context)

def request_borrow(request, pk):
    book = Book.objects.get(isbn = pk)
    student = Student.objects.get(id = request.user)
    s = get_object_or_404(Student, id = str(request.user))

    if s.total_books_due < 5:
        borrow = Borrower()
        borrow.issued_by = request.user
        borrow.issue_date = timezone.now()
        borrow.student = student
        borrow.book = book

        book.available_copies -= 1
        book.save()

        student.total_books_due += 1
        student.save()
        borrow.save()
    return render(request, 'library_management/borrower_form.html')

def return_book(request, pk):
    if not request.user.is_staff:
        return redirect('borrower-index')
    obj = Borrower.objects.get(id = pk)
    book_pk = obj.book.isbn
    student_pk = obj.student.id
    student = Student.objects.get(id = student_pk)
    student.total_books_due -=1
    student.save()

    book = Book.objects.get(isbn=book_pk)
    book.available_copies += 1
    book.save()
    obj.returned = True
    obj.return_date = timezone.now()
    obj.returned_to = request.user
    obj.save()
    return redirect('borrower-index')


class UpdateBook(UpdateView):
    model = Book
    form_class = ListForms

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('book-index')

class UpdateStudent(UpdateView):
    model = Student
    form_class = StudentForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('student-index')