from django.contrib import admin
from .models import Property


admin.site.site_header = "Iproperty admin"
admin.site.site_title = "Iproperty admin area"
admin.site.index_title = "Welcome to Iproperty Admin"


admin.site.register(Property)