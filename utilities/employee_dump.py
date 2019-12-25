import csv
import os
from employee.models import Employee


with open('Employee.csv') as f: 
    reader = csv.reader(f) 
    next(reader) 
    for row in reader: 
    	_, created = Employee.objects.get_or_create(
                employee_number=row[0],
                employee_name=row[1],
                email_id=row[2],
                chargeable=row[3],
                project_manager=row[4],
                gender=row[5],
                business_unit=row[6],
                designation=row[7]
                )
        print ("record inserted !") 


# for project:
with open('Project.csv') as f:  
    reader = csv.reader(f)  
    next(reader) 
    for row in reader:  
    _, created = Projects.objects.get_or_create( 
        project_name = row[1]) 


# for project emp relation:
with open('ProjectEmpMapping.csv') as f: 
    reader = csv.reader(f) 
    next(reader) 
    for row in reader: 
        emp_id = row[0] 
        pro_id = row[1] 
        emp = Employee.objects.get(pk=emp_id) 
        pro = Projects.objects.get(pk=pro_id) 
        _, created = EmployeeProjectRelation.objects.get_or_create(emp_id=emp, project_id=pro)

# for skills
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
