from django.contrib import admin

# Register your models here.
from models import Hotel
from models import Comentario
from models import CSS
from models import PersonalPage
from models import PersonalHotel
# Register your models here.
admin.site.register(Hotel)
admin.site.register(Comentario)
admin.site.register(CSS)
admin.site.register(PersonalPage)
admin.site.register(PersonalHotel)
