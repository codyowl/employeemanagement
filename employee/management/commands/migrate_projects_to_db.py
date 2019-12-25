from django.core.management.base import BaseCommand
from django.utils import timezone
from django.conf import settings
from employee.models import Projects
import csv

project_csv_path = settings.CSV_PATH + '/' + settings.PROJECT_CSV_NAME

class Command(BaseCommand):
    help = 'Migrate projects to db'

    def handle(self, *args, **kwargs):
    	with open(project_csv_path) as f:  
		    reader = csv.reader(f)  
		    next(reader) 
		    for row in reader:  
		    _, created = Projects.objects.get_or_create( 
		        project_name = row[1]) 
