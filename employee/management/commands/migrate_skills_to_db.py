from django.core.management.base import BaseCommand
from django.utils import timezone
from django.conf import settings
from employee.models import SkillName, Skill

skills_csv_path = settings.CSV_PATH + '/' + settings.SKILL_CSV_NAME


class Command(BaseCommand):
    help = 'Migrate skills to db'

    def handle(self, *args, **kwargs):
    	print (skills_csv_path)
    	with open('Skills.csv') as f: 
	    	reader = csv.reader(f) 
			next(reader) 
	    	for row in reader:
	        	emp_pk = row[0] 
	        	skill = row[1]
	        	grade = row[2]
		        try:
		            s = SkillName.objects.get(skill_name=skill) 
		        except SkillName.DoesNotExist:
		            s = SkillName.objects.create(skill_name=skill) 
		    
		        if grade == 'Beginner': 
		            grade = SKILLS_CHOICE[0][0] 
		        elif grade == 'Intermediate': 
		            grade = SKILLS_CHOICE[1][0] 
		        elif grade == 'Pro': 
		            grade = SKILLS_CHOICE[2][0] 
		        emp = Employee.objects.get(pk=emp_pk) 
		        skill_create = Skill()
		        skill_create.emp_id = emp
		        skill_create = grade
		        skill_create.save()
		        skill_create.skills.add(s) 