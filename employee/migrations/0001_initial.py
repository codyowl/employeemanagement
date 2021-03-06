# Generated by Django 2.2.5 on 2019-12-24 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_number', models.AutoField(primary_key=True, serialize=False)),
                ('employee_name', models.CharField(max_length=200)),
                ('email_id', models.EmailField(max_length=254)),
                ('chargeable', models.CharField(choices=[('0', 'chargeable'), ('1', 'non-chargeable')], max_length=1)),
                ('project_manager', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('business_unit', models.CharField(max_length=200)),
                ('designation', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills', models.CharField(max_length=200)),
                ('grade', models.CharField(choices=[('0', 'Beginner'), ('1', 'Intermediate'), ('2', 'Pro')], max_length=1)),
                ('emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeProjectRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Employee')),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Projects')),
            ],
        ),
    ]
