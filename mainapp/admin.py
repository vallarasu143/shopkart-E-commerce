from django.contrib import admin
from .models import userimage,collections,items,items_detail,mobiledetails,add_cart

class userimage_admin(admin.ModelAdmin):
    list_display=['user','userpic']
admin.site.register(userimage,userimage_admin)

class collection_admin(admin.ModelAdmin):
    list_display=['categeory','image']
admin.site.register(collections,collection_admin)

class items_admin(admin.ModelAdmin):
    list_display=['categeries','item_name','item_image','status']
admin.site.register(items,items_admin)

class item_detail_admin(admin.ModelAdmin):
    list_display=['brand','brand_model','model_image','trending']
admin.site.register(items_detail,item_detail_admin)

class mobile_details_admin(admin.ModelAdmin):
    list_display=['mobile_model','storage','rear_camera','fornd_camera','display',
                 'processor','battery','network']
admin.site.register(mobiledetails,mobile_details_admin)

class cart_admin(admin.ModelAdmin):
    list_display=['user','product','qty']
admin.site.register(add_cart,cart_admin)