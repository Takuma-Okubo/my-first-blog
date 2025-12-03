from django.urls import path
from . import views     #blogアプリの全てのビューをインポートする

urlpatterns = [
    path('', views.post_list, name='post_list'),
]