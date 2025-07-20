from django.urls import path

from todo import views

urlpatterns = [
    path('', views.index, name='index'),
    path(
        "task_complete/<int:pk>",
        views.task_complete_view,
        name='task_complete'
    ),
    path("task_create/", views.TaskCreateView.as_view(), name='task_create'),
    path(
        "task_update/<int:pk>",
        views.TaskUpdateView.as_view(),
        name='task_update'
    ),
    path(
        "task_delete/<int:pk>",
        views.TaskDeleteView.as_view(),
        name='task_delete'
    ),
    path("tags/", views.TagsListView.as_view(), name='tags_list'),
    path("tag_create/", views.TagCreateView.as_view(), name='tag_create'),
    path(
        "tag_update/<int:pk>", views.TagUpdateView.as_view(), name='tag_update'
    ),
    path(
        "tag_delete/<int:pk>", views.TagDeleteView.as_view(), name='tag_delete'
    ),
]

app_name = "todo"
