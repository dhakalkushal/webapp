from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import List
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class IndexView(LoginRequiredMixin,generic.ListView):
    template_name = 'todo/home.html'
    
    def get_queryset(self):
        return List.objects.filter(author=self.request.user)

class TodoDelete(LoginRequiredMixin,DeleteView):
    model = List
    success_url = reverse_lazy('home')

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.author:
            return True
        return False

class TodoUpdate(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = List
    fields = ['tasks', 'completed','due_date']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.author:
            return True
        return False

class TodoCreate(LoginRequiredMixin,CreateView):
    model = List
    fields = ['tasks', 'completed','due_date']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
