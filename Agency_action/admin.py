from django.contrib import admin
from parler.admin import *
from .models import*
# Register your models here.




class Print_Admin(TranslatableAdmin):
    list_display = ('title','added_in','price_per_item','amount')


class Car_Admin(TranslatableAdmin):
    list_display = ('car_name','added_in')


class Web_site_Admin(TranslatableAdmin):
    list_display = ('web_name','web_type','url_hyperlink','added_in')


class Social_Admin(TranslatableAdmin):
    list_display = ('post_name','added_in','post_img')


class Emp_Admin(TranslatableAdmin):
    list_display = ('emp_name','view_emp_img','salary','added_in')


class Provider_Admin(TranslatableAdmin):list_display = ('service_name','provider')



class NameAdmin(TranslatableAdmin):pass

#admin.site.register(User_profile, NameAdmin)




admin.site.register(Printing,Print_Admin)

admin.site.register(Web_site,Web_site_Admin)

admin.site.register(Social_media,Social_Admin)

admin.site.register(Sport_car,Car_Admin)
admin.site.register(Emp_model,Emp_Admin)
admin.site.register(Service_provider,Provider_Admin)



