from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Comment
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse
from .forms import CommentForm
'''

class CommentCreate(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model = Comment
    fields = ['content']
    success_message = "%(tasks) was successfully made"

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.question_id = self.kwargs["question_id"]
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return reverse("detail-post", kwargs={"pk": self.kwargs["question_id"]})
'''

class CommentDelete(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Comment

    def get_success_url(self):
        content = self.get_object()
        slug = content.post.slug
        return reverse('detail-post',kwargs={'slug':slug})

    def test_func(self):
        content = self.get_object()
        if self.request.user == content.author:
            return True
        return False

class CommentUpdate(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        user = self.get_object()
        if self.request.user== user.author:
            return True
        return False

    def get_success_url(self):
        content = self.get_object()
        slug = content.post.slug
        return reverse('detail-post',kwargs={'slug':slug})