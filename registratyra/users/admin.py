from django.contrib import admin

# Register your models here.
from .models import User, Patient, Speciality, Doctor

admin.site.register(User)
admin.site.register(Patient)
admin.site.register(Speciality)
admin.site.register(Doctor)