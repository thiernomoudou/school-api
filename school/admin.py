from django.contrib import admin

from  .models import School, Batch
from department.models import Department, Room, Subject, ClassLevel
from admission.models import Registration, Admission
from employee.models import Teacher, Employee
from student.models import Student, Exam, Grade, Payment
from timetable.models import Timetable
from attendance.models import Attendance


#admin.site.register(Department)
admin.site.register(Room)
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Employee)
admin.site.register(Registration)
admin.site.register(Admission)
#admin.site.register(Student)
admin.site.register(Exam)
admin.site.register(Grade)
admin.site.register(Batch)
admin.site.register(Payment)
admin.site.register(Timetable)
admin.site.register(Attendance)

class GradeInline(admin.TabularInline):
    """
    Defines format of inline Grade insertion (used in StudentAdmin)
    """
    model = Grade

class PaymentInline(admin.TabularInline):
    model = Payment



@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    """
    Administration object for Student models. 
    Defines:
     - fields to be displayed in list view (list_display)
     - orders fields in detail view (fields), grouping the date fields horizontally
     - adds inline addition of books in author view (inlines)
    """

    inlines = [GradeInline, PaymentInline]


class ClassLevelInline(admin.TabularInline):
    model = ClassLevel


class StudentInline(admin.TabularInline):
    model = Student


class SubjectInline(admin.TabularInline):
    model = Subject


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    inlines = [ClassLevelInline]

@admin.register(ClassLevel)
class ClassLevelAdmin(admin.ModelAdmin):
    inlines = [SubjectInline]

# class DepartmentInline(admin.TabularInline):
#     model = Department

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    pass
#     inlines = [DepartmentInline]