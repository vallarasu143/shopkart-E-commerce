from django.urls import path
from mainapp import views
urlpatterns = [
    
    path('',views.mainpage,name='mainpage'),
    path('login/',views.loginpage,name='loginpage'),
    path('logout/',views.logoutpage,name='logoutpage'),
    path('register/',views.registerpage,name='registerpage'),
    path('collection/',views.collection,name='collectionpage'),
    path('col-item/<int:id>',views.collection_item,name='collection_item'),
    path('item-details/<int:id>',views.item__details,name='item_deatails'),
    path('Mobiles/<int:id>',views.mobile_detail,name='mobile_deatails'),
    path('trending/',views.trendings,name='trending'),
    path('userchange',views.profilechange,name='userchange'),
    path('addtocart',views.add_to_cart,name='addtocart'),
    path('details/',views.cartdetails,name='cart_details'),
    path('cart_remove/<int:id>',views.cart_product_remove,name='cartdetails_remove'),
    path('itemplus/<int:id>',views.cart_itemplus,name='cart_itemplus'),
    path('itemminus/<int:id>',views.cart_itemminus,name='cart_itemminus'),
    path('add_whisitlist',views.add_to_whisitlists,name='add_whisitlist'),
    path('whisitlist/details/',views.whisitlist_item,name='whisitlist_details'),
    path('whisitlist/item/remove/id/<int:id>',views.whisitlist_item_remove,name='whisitlist_remove'),
    path('user/account/delete/',views.user_remove,name='user_remove'),
    path('user/uploadpicture/',views.upload_user_picture,name='user_uploadpicture'),
    
]