from rest_framework import viewsets
from rest_framework_extensions import mixins

from .models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer


class ProjectViewSet(mixins.NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('-last_edited')
    serializer_class = ProjectSerializer


class TaskViewSet(mixins.NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

