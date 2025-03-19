from django.db import models
from django.utils.timezone import now
from phonenumber_field.modelfields import PhoneNumberField

class Division(models.Model):
    div_name = models.CharField(max_length=25, verbose_name="Division Name")
    in_scope = models.BooleanField(help_text="If the division is target for the learning program, check this field")

    class Meta:
        verbose_name = "Division"
        verbose_name_plural = "Divisions"

    def __str__(self):
        return f"{self.div_name}"


class Employee(models.Model):
    PRIORITIES = [('H', 'High'), ('M', 'Medium'), ('L', 'Low')]
    name = models.CharField(max_length=25, verbose_name='Name')
    priority = models.CharField(
        max_length=1,
        verbose_name="Learning Priorities",
        choices=PRIORITIES,
        default="M"
    )
    reg_date = models.DateField(default=now, verbose_name="Registration Date")
    division = models.ForeignKey(Division, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def __str__(self):
        return f"{self.name}"


class PersonalInfo(models.Model):
    name = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key=True)
    tel = PhoneNumberField(
        verbose_name="Telephone Number",
        blank=True,
        null=True,
        help_text="Enter a valid phone number (e.g. +12125552368)",
    )
    address = models.CharField(max_length=100, verbose_name="Address")

    def __str__(self):
        return f"Personal Info for {self.name}"


class LearningCourse(models.Model):
    LEVEL = [('B', 'Basic'), ('I', 'Intermediate'), ('A', 'Advanced')]
    title = models.CharField(max_length=50, verbose_name="Course Title", unique=True)
    level = models.CharField(max_length=1, verbose_name="Course Level", choices=LEVEL, default="B")
    employee = models.ManyToManyField(Employee, verbose_name="Enrolled Employees")

    class Meta:
        verbose_name = "Learning Course"
        verbose_name_plural = "Learning Courses"

    def __str__(self):
        return f"{self.title}"
