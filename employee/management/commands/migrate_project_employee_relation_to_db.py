from django.core.management.base import BaseCommand
from django.utils import timezone
from django.conf import settings
from employee.models import Employee, Projects, EmployeeProjectRelation
import csv

project_emp_csv_path = settings.CSV_PATH + '/' + settings.PROJECT_EMP_MAPPING_CSV_NAME


class Command(BaseCommand):
    help = 'Migrate project employee relation to db'

    def handle(self, *args, **kwargs):
    	with open(project_emp_csv_path) as f: 
		    reader = csv.reader(f) 
		    next(reader) 
		    for row in reader: 
		        emp_id = row[0] 
		        pro_id = row[1] 
		        emp = Employee.objects.get(pk=emp_id) 
		        pro = Projects.objects.get(pk=pro_id) 
		        _, created = EmployeeProjectRelation.objects.get_or_create(emp_id=emp, project_id=pro)
