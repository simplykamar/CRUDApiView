from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from crud.serializers import EmployeeSerializer
from crud.models import Employee

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated

from rest_framework import viewsets
# Create your views here.

class EmployeeCRUDViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

class EmployeeAPIView(APIView):
    def get(self,req):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,req):
        serializer = EmployeeSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class EmployeeRetrieveUpdateDestroyAPIView(APIView):
    def get(self,req,pk):
        try:
            employee = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            employee = None
        if employee is None:
            return Response(status=status.HTTP_400_NOT_FOUND)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,req,pk):
        try:
            employee = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            employee = None
        if employee is None:
            return Response(status=status.HTTP_400_NOT_FOUND)
        serializer = EmployeeSerializer(employee, data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self,req):
        pass

    def delete(self,req,pk):
        try:
            employee = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            employee = None
        if employee is None:
            return Response(status=status.HTTP_400_NOT_FOUND)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
