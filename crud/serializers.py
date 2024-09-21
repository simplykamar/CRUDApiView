from rest_framework import serializers
from crud.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    esal = serializers.DecimalField(max_digits=10,decimal_places=2)

    def validate_esal(self,val):
        if val < 5000:
            raise serializers.ValidationError('Employee salary minimum of 5000')
        return val
    class Meta:
        model = Employee
        fields = '__all__' 