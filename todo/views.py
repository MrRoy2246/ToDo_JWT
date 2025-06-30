from rest_framework.generics import CreateAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer,RegisterSerializer
from django.contrib.auth.models import User
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
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
        return Task.objects.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        # Set the user automatically when creating a new task
        serializer.save(user=self.request.user)

class MyTaskRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    serializer_class=TaskSerializer
    permission_classes=[IsAuthenticated]
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    
class ToggleTaskCompletionApiView(APIView):
    permission_classes=[IsAuthenticated]
    def patch(self,request,pk):
        task=get_object_or_404(Task,pk=pk,user=request.user)
        task.completed=not task.completed
        task.save()
        return Response({'id': task.id, 'completed': task.completed}, status=status.HTTP_200_OK)