# employeemanagement
A DRF web service to handle employee management 

## api routes:
- http://127.0.0.1:8000/bus-emp-count/?business_unit=<BUSINESS_UNIT_NAME>
- http://127.0.0.1:8000/bus-charg-emp-count/?business_unit=<BUSINESS_UNIT_NAME>
- http://127.0.0.1:8000/project-emp-count/?project_name=<PROJECT_NAME>
- http://127.0.0.1:8000/skill-emp-count/?skill_name=<SKILL_NAME>
- http://127.0.0.1:8000/designation-count/
- http://127.0.0.1:8000/employee/
- http://127.0.0.1:8000/employee/project/?project_name=<PROJECT_NAME>
- http://127.0.0.1:8000/employee/add/
- http://127.0.0.1:8000/employee/delete/<EMP_ID>/

## prerequisites installation:
    pip3 install -r requirements.txt
    
## Management commands to dump data to db from csv:
### Migrating employee data:   
    python manage.py migrate_employee_to_db
### Migrating project and employee relation data    
    python manage.py migrate_project_employee_relation_to_db
### Migrating projects data    
    python manage.py migrate_projects_to_db
### Migrating skills data    
    python manage.py migrate_skills_to_db
    
### User Authentication:
    Everytime when a record is inserted into Employee table an that record got inserted into User Table as well

   
## Endpoints sample on postman:

### Get Business Unit wise employee count
![1](https://user-images.githubusercontent.com/9798362/71447282-89261f80-2752-11ea-849d-8c3ba1188f0c.png)
### Business Unit wise chargeable and nonchargeable count
![2](https://user-images.githubusercontent.com/9798362/71447283-8aefe300-2752-11ea-9be5-92132e768011.png)
### Project wise Employee count, with total chargeable and nonchargeable count
![3](https://user-images.githubusercontent.com/9798362/71447284-8cb9a680-2752-11ea-8d2e-c3c40ac21b36.png)
### Skill wise employee count
![8](https://user-images.githubusercontent.com/9798362/71447295-95aa7800-2752-11ea-8cb8-5b5e07afc96f.png)
### Total Designation Count
![4](https://user-images.githubusercontent.com/9798362/71447285-8dead380-2752-11ea-8ae6-619bac0ce06c.png)
### Get All Employees
![5](https://user-images.githubusercontent.com/9798362/71447290-8fb49700-2752-11ea-985c-325f778b8d97.png)
### Get all Employees working on a Specific project

### Add/Delete Employees
![6](https://user-images.githubusercontent.com/9798362/71447291-917e5a80-2752-11ea-8c6d-f82abdb29b2c.png)
![7](https://user-images.githubusercontent.com/9798362/71447293-93481e00-2752-11ea-8653-eec35c383952.png)






