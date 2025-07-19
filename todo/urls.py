from django.urls import path

from todo import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tags/', views.TaskListView.as_view(), name='tags'),
]

app_name = "todo"