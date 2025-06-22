from django.urls import path
from .views import MyTaskListCreateApiView,RegisterView

urlpatterns = [
    path('tasks/', MyTaskListCreateApiView.as_view(), name='task-list-create'),
    path('register/', RegisterView.as_view(), name='register'),
]
