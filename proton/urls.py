from django.urls import include, path
from rest_framework_extensions.routers import ExtendedSimpleRouter
from . import views

router = ExtendedSimpleRouter()
(
    router.register(r'projects', views.ProjectViewSet, basename='project')
        .register(r'tasks',
            views.TaskViewSet,
            basename='project-tasks',
            parents_query_lookups=['project_id'])
)

urlpatterns = router.urls 
