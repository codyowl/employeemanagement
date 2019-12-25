from rest_framework import serializers
from employee.models import Employee


class AllEmployeeSerializer(serializers.Serializer):
	employee_number = serializers.IntegerField()
	employee_name = serializers.CharField(max_length=200)
	email_id = serializers.CharField(max_length=200)
	chargeable = serializers.CharField(max_length=200)
	project_manager = serializers.CharField(max_length=200)
	gender = serializers.CharField(max_length=200)
	business_unit = serializers.CharField(max_length=200)
	designation = serializers.CharField(max_length=200)

