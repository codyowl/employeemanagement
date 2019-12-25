from django.core.management.base import BaseCommand
from django.utils import timezone
from django.conf import settings
from django.models import Employee, GENDER
import csv

employee_csv_path = settings.CSV_PATH + '/' + settings.EMPLOYEE_CSV_NAME


class Command(BaseCommand):
    help = 'Migrate employee to db'

    def handle(self, *args, **kwargs):
    	with open(employee_csv_path) as f: 
		    reader = csv.reader(f) 
		    next(reader) 
		    for row in reader: 
		    	gender = row[5]
		    	if gender == 'Male':
					gender = GENDER[0][0]
				else:
					gender = GENDER[1][0]

		    	_, created = Employee.objects.get_or_create(
		                employee_number=row[0],
		                employee_name=row[1],
		                email_id=row[2],
		                chargeable=row[3],
		                project_manager=row[4],
		                gender=gender,
		                business_unit=row[6],
		                designation=row[7]
		                )