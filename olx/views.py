from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView

from .models import Product


# Create your views here.
class UserLoginView(LoginView):
    fields = "__all__"
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('list')

class RegisterView(FormView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    redirect_authenticated_user = True
    success_url = 'login'

    def form_valid(self, form):
        user=form.save()
        if user is not None:
            login(self.request,user)
        return super(RegisterView,self).form_valid(form)

    def get(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('list')
        return super(RegisterView,self).get(*args,**kwargs)


class FrontProductList(ListView):
    model = Product
    context_object_name = 'product'
    template_name = 'front.html'

class ProductList(LoginRequiredMixin,ListView):
    model = Product
    context_object_name = 'product'
    template_name = 'product_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = context['product'].filter(user = self.request.user)
        return context


class CreateProduct(LoginRequiredMixin,CreateView):
    model = Product
    fields = ['title', 'image_url', 'price', 'description']
    template_name = 'create-product.html'
    success_url = reverse_lazy('list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateProduct,self).form_valid(form)


class UpdateProduct(LoginRequiredMixin,UpdateView):
    model = Product
    fields = ['title', 'image_url', 'price', 'description']
    template_name = 'create-product.html'
    success_url = reverse_lazy('list')


class DeleteProduct(LoginRequiredMixin,DeleteView):
    model = Product
    template_name = 'delete-product.html'
    success_url = reverse_lazy('list')
