from django.contrib import admin

# Register your models here.
from models import Hotel
from models import PersonalPage

admin.site.register(Hotel)
admin.site.register(PersonalPage)
