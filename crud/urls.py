from django.urls import path,include
from crud.views import EmployeeAPIView,EmployeeRetrieveUpdateDestroyAPIView,EmployeeCRUDViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('v2',EmployeeCRUDViewSet)

urlpatterns = [
    path('employees/v1/',EmployeeAPIView.as_view()),
    path('employees/v1/<int:pk>',EmployeeRetrieveUpdateDestroyAPIView.as_view()),
    path('employees/',include(router.urls)),
]