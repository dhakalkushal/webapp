from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm, UserUpdate
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

# Create your views here.
class UserFormView(View):
    form_class = UserForm
    template_name = 'users/register.html'

    def get(self,request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user.set_password(password)
            user.save()

            #returns User objects if credentials are correct
            user = authenticate(username= username, password = password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('profile')
        return render(request,self.template_name, {'form':form})

@method_decorator(login_required, name='dispatch')
class UserProfileUpdate(UpdateView):
    model = User
    fields = ('first_name','last_name','email')
    template_name = 'users/user_update.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user

@login_required(login_url='/accounts/login/')
def profile(request):
    return render(request, 'users/profile.html')
