from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Task
from .serializers import TaskSerializer

class TaskListCreateView(ListCreateAPIView):
    queryset = Task.objects.all().order_by('-due_date')
    serializer_class = TaskSerializer

class TaskDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
