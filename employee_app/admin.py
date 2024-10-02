from django.contrib import admin
from .models import Department, Employee, Achievement, AchievementEmployee

admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Achievement)
admin.site.register(AchievementEmployee)