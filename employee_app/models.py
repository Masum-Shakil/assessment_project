from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Achievement(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class AchievementEmployee(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    achievement_date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = (('employee', 'achievement'),)

    def __str__(self):
        return f'employee: {self.employee.name}, achievement: {self.achievement.name}'
