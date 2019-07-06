from django.db import models

class document(models.Model):
    docfile = models.FileField(upload_to='media/%Y/%m/%d/')

class faculties(models.Model):
    faculties_id = models.AutoField(primary_key=True)
    faculties_name = models.CharField(max_length = 100)

class department(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length =100)
    faculties_id = models.ForeignKey(faculties, on_delete=models.CASCADE,null=True)


class course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length = 100)
    department_id = models.ForeignKey(department, on_delete=models.SET_NULL, null=True)
    faculties_id = models.ForeignKey(faculties, on_delete=models.SET_NULL,null=True)

class semester(models.Model):
    semester_id = models.AutoField(primary_key=True)
    semester_name = models.CharField(max_length = 100)
    faculties_id = models.ForeignKey(faculties, on_delete=models.SET_NULL,null =True)
    department_id = models.ForeignKey(department, on_delete=models.SET_NULL, null=True)
    course_id = models.ForeignKey(course, on_delete=models.SET_NULL, null=True)

class downloads(models.Model):
    id = models.AutoField(primary_key=True)
    faculties_id = models.ForeignKey(faculties, on_delete=models.SET_NULL,null=True)
    department_id = models.ForeignKey(department, on_delete=models.SET_NULL, null=True)
    course_id = models.ForeignKey(course, on_delete=models.SET_NULL, null=True)
    semester_id = models.ForeignKey(semester, on_delete=models.SET_NULL, null=True)
