from django.urls import path
from .import views

urlpatterns = [
    path('pub_msg/', views.publish_message, name="pub_msg"),
    path('pub_file/', views.publish_file, name="pub_file"),
    path('my_view/', views.my_view, name="my_view"),

]
