
from django.contrib import admin
from myapp.models import LOGIN, crtateuser , post,activity,Profile,add_ativity,add_data,add_data_all

# Register your models here.
admin.site.register(post)
admin.site.register(crtateuser)
admin.site.register(LOGIN)
admin.site.register(activity)
admin.site.register(Profile)
admin.site.register(add_ativity)
admin.site.register(add_data)
admin.site.register(add_data_all)

