from django.urls import path
from .views import (get_context_data, 
                    register, 
                    about, contact, 
                    destinations, news, create_user, 
                    give_detail, search_tag)

urlpatterns = [
    path('', get_context_data, name='index'),
    path('about/', about, name='about'),
    path('create_user/', create_user, name='create_user'),
    path('contact/', contact, name="contact"),
    path('destinations/<int:pk>/', give_detail, name='destinations'),
    path('news/', news, name='news'),
    path('search/',search_tag, name='search_tag'),
    path('register/', register, name='register'),
]