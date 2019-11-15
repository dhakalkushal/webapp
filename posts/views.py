from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import redirect, render_to_response, get_object_or_404, render
from django.shortcuts import render, redirect
from .models import Post
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import ListForms
from comments.forms import CommentForm
from comments.models import Comment
from django.db.models import Q

class PostIndex(generic.ListView):
    template_name = 'posts/post_index.html'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.all()

class SearchResultView(generic.ListView):
    template_name = 'posts/post_index.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
        return object_list

'''
class PostDetail(generic.DetailView,CreateView):
    model = Post
    form_class = CommentForm
    template_name = 'posts/post_detail.html'
    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.instance.author = self.request.user
            form.save()
        return redirect(reverse("index"))
    def get_success_url(self):
        return reverse("index")
'''

def view_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = CommentForm(request.POST or None)
    comments = Comment.objects.filter(post=post,reply = None)
    context = {
        'post':post,
        'form':form,
        'comments':comments,
    }

    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.author = request.user
        reply_id = request.POST.get('comment_id')
        comment_qs = None
        if reply_id:
            comment_qs = Comment.objects.get(id=reply_id)
        comment.reply = comment_qs
        comment.save()
        return redirect(request.path)
    return render(request, 'posts/post_detail.html',context)

class PostCreate(LoginRequiredMixin,UserPassesTestMixin ,CreateView ):
    model = Post
    form_class = ListForms

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.is_staff:
            return True
        return False

class PostUpdate(LoginRequiredMixin,UserPassesTestMixin ,UpdateView):
    model = Post
    form_class = ListForms

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        user = self.get_object()
        if self.request.user== user.author:
            return True
        return False
