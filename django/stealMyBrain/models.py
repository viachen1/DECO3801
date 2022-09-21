from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text

class Input(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    input_text = models.CharField(max_length=200)

    def __str__(self):
        return self.input_text

# Supervisor Model
class Supervisor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.IntegerField(null=True)
    email = models.EmailField(max_length=50, default='default@stealmybrain.com')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

# Employee Model
class Employee(models.Model):
    APPRENTICE = 'APP'
    TRAINEE = 'TR'
    JUNIOR = 'JR'
    SENIOR = 'SNR'
    LEAD = 'LD'
    HEAD = 'HD'

    EMPLOYEE_TYPE_CHOICES = [
        (APPRENTICE, 'Apprentice'),
        (TRAINEE, 'Trainee'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        (LEAD, 'Lead'),
        (HEAD, 'Head'),
    ]

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.IntegerField()
    email = models.EmailField(max_length=50)
    age = models.IntegerField()
    role = models.CharField(max_length=4, choices=EMPLOYEE_TYPE_CHOICES)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

