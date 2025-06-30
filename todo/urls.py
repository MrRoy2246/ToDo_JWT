from django.urls import path
from .views import MyTaskListCreateApiView,RegisterView,MyTaskRetrieveUpdateDestroyApiView,ToggleTaskCompletionApiView

urlpatterns = [
    path('tasks/', MyTaskListCreateApiView.as_view(), name='task-list-create'),
    path('register/', RegisterView.as_view(), name='register'),
    path('tasks/<int:pk>/',MyTaskRetrieveUpdateDestroyApiView.as_view(),name='task-detail'),
    path('tasks/<int:pk>/complete/', ToggleTaskCompletionApiView.as_view(), name='task-toggle-complete'),

]
