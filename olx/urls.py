from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views
from .views import ProductList, CreateProduct, UpdateProduct, DeleteProduct, UserLoginView, RegisterView, \
    FrontProductList

urlpatterns =[
                path('login/', UserLoginView.as_view(), name='login'),
                path('signup/', RegisterView.as_view(), name='signup'),
                path('logout/',LogoutView.as_view(),name='logout'),
                path('front-list/',FrontProductList.as_view(),name='front_list'),
                path('product-list/',ProductList.as_view(),name='list'),
                path('product-create/', CreateProduct.as_view(), name='create'),
                path('product-update/<int:pk>', UpdateProduct.as_view(), name='update'),
                path('product-delete/<int:pk>', DeleteProduct.as_view(), name='delete'),

]