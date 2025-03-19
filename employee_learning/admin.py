from django.contrib import admin
from .models import Employee, Division, PersonalInfo, LearningCourse
# Register your models here.


admin.site.register(Employee)
admin.site.register(Division)

@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'tel', 'address']

# admin.site.register(PersonalInfo)
admin.site.register(LearningCourse)
