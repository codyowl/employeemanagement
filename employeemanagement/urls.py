"""employeemanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from employee.views import *

"""
Get Business Unit wise employee count
Business Unit wise chargeable and nonchargeable count
Project wise Employee count, with total chargeable and nonchargeable count
Skill wise employee count
Total Designation Count
Get All Employees
Get all Employees working on a Specific project
Add/Delete Employees
Authentication for all the API’s
a. Add Users table using information provided in Employee table
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bus-emp-count/', Businessunit_employee_count.as_view(), name='busempcount'),
    path('bus-charg-emp-count/', Businessunit_char_employee_count.as_view(), name='busempcharcount'),
    path('project-emp-count/', Project_employee_count.as_view(), name='projempcount'),
    path('skill-emp-count/', Skillsbased_employee_count.as_view(), name='skempcount'),
    path('designation-count/', Designation_count.as_view(), name='desigcount'),
    path('employee/', Get_all_employee.as_view(), name='allemployee'),
    path('employee/add/', Employee_add.as_view(), name='addemp'),
    path('employee/delete/<int:pk>/', Employee_delete.as_view(), name='delemp'),
    path('employee/project/', Get_employee_project.as_view(), name='getempbyproj'),
]
