from rest_framework.generics import CreateAPIView,ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer,RegisterSerializer
from django.contrib.auth.models import User


class RegisterView(CreateAPIView):
    queryset=User.objects.all()
    serializer_class=RegisterSerializer

class MyTaskListCreateApiView(ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access
    def get_queryset(self):
        # Only return tasks belonging to the logged-in user
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Set the user automatically when creating a new task
        serializer.save(user=self.request.user)
