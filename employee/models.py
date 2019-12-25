from django.db import models


CHARGEABLE_CHOICE = (
	('0', 'chargeable'),
	('1', 'non-chargeable')
	)

GENDER = (
	('M', 'Male'),
	('F', 'Female')
	)

SKILLS_CHOICE = (
	('0', 'Beginner'),
	('1', 'Intermediate'),
	('2', 'Pro')
	)

# Create your models here.
class Employee(models.Model):
	employee_number = models.AutoField(primary_key=True)
	employee_name = models.CharField(max_length=200)
	email_id = models.EmailField()
	chargeable = models.CharField(max_length=1, choices=CHARGEABLE_CHOICE)
	project_manager = models.CharField(max_length=200)
	gender = models.CharField(max_length=1, choices=GENDER)
	business_unit = models.CharField(max_length=200)
	designation = models.CharField(max_length=200)

	def __str__(self):
		return self.employee_name


class SkillName(models.Model):
	skill_name = models.CharField(max_length=200)

	def __str__(self):
		return self.skill_name


class Skill(models.Model):
	emp_id = models.ForeignKey('Employee',on_delete=models.CASCADE)
	skills = models.ManyToManyField('SkillName')
	grade = models.CharField(max_length=1, choices=SKILLS_CHOICE)

	def __str__(self):
		return self.emp_id.employee_name



class Projects(models.Model):
	project_name = models.CharField(max_length=200)

	def __str__(self):
		return self.project_name

class EmployeeProjectRelation(models.Model):
	emp_id = models.ForeignKey('Employee',on_delete=models.CASCADE)
	project_id = models.ForeignKey('Projects',on_delete=models.CASCADE,default="")

