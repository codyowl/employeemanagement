# Generated by Django 2.2.5 on 2019-12-24 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_auto_20191224_1017'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkillName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='skill',
            name='skills',
        ),
        migrations.AddField(
            model_name='skill',
            name='skills',
            field=models.ManyToManyField(to='employee.SkillName'),
        ),
    ]
