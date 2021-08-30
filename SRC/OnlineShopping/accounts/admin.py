from django.contrib import admin
from .models import CustomUser, Admin, Staff, Customer

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Admin)
admin.site.register(Staff)
admin.site.register(Customer)
