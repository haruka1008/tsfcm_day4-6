from django.urls import path
from . import views

app_name = 'diary'

urlpatterns = [
    path('',views.Index, name='index'), # http://127.0.0.1:8000/diary/
]