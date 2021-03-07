
from django.urls import include, path
from rest_framework import routers
from rest_framework.routers import SimpleRouter
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


router = routers.DefaultRouter()
# router.register(r'exam', views.ExamViewSet)
# router.register(r'students', views.StudentViewSet)
# router.register(r'grades', views.GradeViewSet)

urlpatterns = [
    path('', include(router.urls))]