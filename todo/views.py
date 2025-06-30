from rest_framework.generics import CreateAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer,RegisterSerializer
from django.contrib.auth.models import User
from rest_framework import filters

class RegisterView(CreateAPIView):
    queryset=User.objects.all()
    serializer_class=RegisterSerializer

class MyTaskListCreateApiView(ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access
    filterset_fields = ['completed']  # ✅ allow ?completed=true
    search_fields = ['title', 'description']  # ✅ allow ?search=read
    def get_queryset(self):
        # Only return tasks belonging to the logged-in user
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Set the user automatically when creating a new task
        serializer.save(user=self.request.user)

class MyTaskRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    serializer_class=TaskSerializer
    permission_classes=[IsAuthenticated]
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)