from django.urls import path
from . import views

app_name = 'diary'

urlpatterns = [
    path('',views.IndexView.as_view(), name='index'), # http://127.0.0.1:8000/diary/
    path('add/',views.AddView.as_view(), name='add'), # http://127.0.0.1:8000/diary/add/
    path('update/<int:pk>', views.UpdateView.as_view(), name='update'), # http://127.0.0.1:8000/diary/update/#
    path('delete/<int:pk>', views.DeleteView.as_view(), name='delete'), # http://127.0.0.1:8000/diary/delete/#
    path('detail/<int:pk>', views.DetailView.as_view(), name='detail'), # http://127.0.0.1:8000/diary/detail/#
]