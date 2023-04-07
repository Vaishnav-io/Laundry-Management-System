from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(CRegistration)
admin.site.register(BRegistration)
admin.site.register(DRegistration)
admin.site.register(BDetails)
admin.site.register(B_C_Request)

