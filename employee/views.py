from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from employee.models import Employee, Projects, EmployeeProjectRelation, \
SKILLS_CHOICE, GENDER, Skill, SkillName
from employee.serializers import AllEmployeeSerializer
from rest_framework import status
from django.contrib.auth.models import User

DEFAULT_PASSWORD = "qwerty123456_"

# Create your views here.
# businessunit_employee_count
# businessunit_char_employee_count
# project_employee_count
# skillsbased_employee_count
# designation_count
# get_all_employee
# employee_add
# employee_delete
# get_employee_project

class Businessunit_employee_count(APIView):
	def get(self, request):
		business_unit = request.GET.get('business_unit', '')
		business_unit_count = Employee.objects.filter(business_unit=business_unit).count()
		response_dict = {}
		response_dict['business_unit'] = business_unit
		response_dict['employee_count'] = business_unit_count
		return Response(response_dict)

class Businessunit_char_employee_count(APIView):
	def get(self, request):
		business_unit = request.GET.get('business_unit', '')
		employee_list = Employee.objects.filter(business_unit=business_unit)
		chargeable = len([data for data in employee_list if data.chargeable=='1'])
		nonchargeable = len([data for data in employee_list if data.chargeable=='0'])
		response_dict = {}
		response_dict["business_unit"] = business_unit
		response_dict["chargeable_employee_count"] = chargeable
		response_dict["nonchargeable_employee_count"] = nonchargeable
		return Response(response_dict)


class Project_employee_count(APIView):
	def get(self, request):
		project_name = request.GET.get('project_name', '')
		project = Projects.objects.get(project_name=project_name)
		project_id = project.id
		emp_list = EmployeeProjectRelation.objects.filter(project_id=project)   
		chargeable = len([data for data in emp_list if data.emp_id.chargeable=='1'])
		nonchargeable = len([data for data in emp_list if data.emp_id.chargeable=='0'])
		response_dict = {}
		response_dict['project_name'] = project_name
		response_dict["chargeable_emp_proj_count"] = chargeable
		response_dict["nonchargeable_emp_proj_count"] = nonchargeable
		return Response(response_dict)

class Skillsbased_employee_count(APIView):
	def get(self, request):
		skill_name = request.GET.get('skill_name', '')
		skill_emp_count = Skill.objects.filter(skills__skill_name=skill_name).count()
		response_dict = {}
		response_dict['skill_name'] = skill_name
		response_dict['employee_count'] = skill_emp_count
		return Response(response_dict)	
	

class Designation_count(APIView):
	def get(self, request):
		total_designation = Employee.objects.order_by().values('designation').distinct().count()
		return Response({'total_designation_count' : total_designation})        

class Get_all_employee(APIView):
	def get(self, request):
		employee = Employee.objects.all()
		serializer = AllEmployeeSerializer(employee, many=True)
		return Response({"employees_list":serializer.data})

class Employee_add(APIView):
	def post(self, request):
		serializer = AllEmployeeSerializer(data=request.data)
		employee_number = request.data['employee_number']
		employee_name = request.data['employee_name']
		email_id = request.data['email_id']
		chargeable = request.data['chargeable']
		project_manager = request.data['project_manager']
		gender = request.data['gender']
		business_unit = request.data['business_unit']
		designation = request.data['designation']

		if gender == 'Male':
			gender = GENDER[0][0]
		else:
			gender = GENDER[1][0]

		if serializer.is_valid():
			employee = Employee.objects.create(
					employee_number = employee_number,
					employee_name = employee_name,
					email_id = email_id,
					chargeable = chargeable,
					project_manager = project_manager,
					gender = gender,
					business_unit = business_unit,
					designation = designation
					)  

			# for every employee createion it will create an user for authentication as well
			user = User.objects.create(
				username = employee_name,
				first_name = employee_name,
				email_id = email_id,	
				)	

			user.set_password(username + DEFAULT_PASSWORD)
			user.save()		 

			
		return Response(serializer.data, status=status.HTTP_201_CREATED)

class Employee_delete(APIView):
	def delete(self, request, pk, format=None):
		employee = get_object_or_404(Employee, pk=pk) 
		employee.delete()
		return Response({'message':'employee deleted'},status=status.HTTP_204_NO_CONTENT)

class Get_employee_project(APIView):
	def get(self, request):
		project_name = request.GET.get('project_name', '')
		employee_list_count = EmployeeProjectRelation.objects.filter(project_id__project_name=project_name).count()
		response_dict = {}
		response_dict['project_name'] = project_name
		response_dict['employee_count'] = employee_list_count
		return Response(response_dict)