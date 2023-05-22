from django.contrib import admin
from .models import Doctor, Pacient, Image

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Pacient)
admin.site.register(Image)
