import json
from django.http import JsonResponse
from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.urls import reverse
from .models import userimage,collections,items,items_detail,mobiledetails,add_cart,whisitlist
from .forms import userimage_form,customUserform
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

def mainpage(requset):
    collection_items=collections.objects.all()
    trending_item=items_detail.objects.filter(trending=True)
    if requset.user.is_authenticated:
        userid=requset.user.id
        #username=requset.user.username
        image=userimage.objects.all()
        for msg in image:
            if msg.user_id == userid:
                image=userimage.objects.get(user_id=userid)
                return render(requset,'other/home.html',{'image':image,'item':collection_items,'items':trending_item})
        return render(requset,'other/home.html',{'item':collection_items,'items':trending_item})
    return render(requset,'other/home.html',{'item':collection_items,'items':trending_item})

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('mainpage')
    
    if request.method == "POST":
        user_name=request.POST['user-name']
        user_pass=request.POST['user-password']
        user=authenticate(username=user_name,password=user_pass)
        if user is not None:
            login(request,user)
            return redirect('mainpage')
        else:
            messages.error(request,"please check your details")
            return redirect('loginpage')
    return render(request,"other/login.html")

def logoutpage(request):
    logout(request)
    messages.success(request,'logout successfully')
    return redirect("loginpage")


def registerpage(request):
    if request.user.is_authenticated:
        return redirect('mainpage')
    form=customUserform()
    if request.method == "POST":
       form=customUserform(request.POST,request.FILES)
       if form.is_valid():
           form.save()
           messages.success(request,'Successfully registerd')
           return redirect('loginpage')
    
    return render(request,'other/register.html',{'form':form})

def collection(request):
    collection_items=collections.objects.all()
    if request.user.is_authenticated:
        userid=request.user.id
        image=userimage.objects.all()
        
        for msg in image:
            if msg.user_id == userid:
                image=userimage.objects.get(user_id=userid)
                return render(request,'other/collection.html',{'image':image,'item':collection_items})
        return render(request,'other/collection.html',{'item':collection_items})
    return render(request,'other/collection.html',{'item':collection_items})

def collection_item(request,id):
    col_items=items.objects.filter(categeries__pk=id)
    if request.user.is_authenticated:
        userid=request.user.id
        image=userimage.objects.all()
        for msg in image:
            if msg.user_id == userid:
                image=userimage.objects.get(user_id=userid)
                return render(request,'other/items.html',{'image':image,'item':col_items})
        return render(request,'other/items.html',{'item':col_items})
    return render(request,'other/items.html',{'item':col_items})

def item__details(request,id):
    details=items_detail.objects.filter(brand__pk=id)
    if request.user.is_authenticated:
        userid=request.user.id
        image=userimage.objects.all()
        for msg in image:
            if msg.user_id == userid:
                image=userimage.objects.get(user_id=userid)
                return render(request,'other/itemdetails.html',{'image':image,'item':details})
        return render(request,'other/itemdetails.html',{'item':details})
    return render(request,'other/itemdetails.html',{'item':details})

def mobile_detail(request,id):
    detail=mobiledetails.objects.filter(mobile_model__pk=id)
    if request.user.is_authenticated:
        userid=request.user.id
        image=userimage.objects.all()
        whisiticon=whisitlist.objects.filter(user=userid,product_id=id)
        for msg in image:
            if msg.user_id == userid:
                image=userimage.objects.get(user_id=userid)
                return render(request,'other/mobilehtml.html',{'image':image,'item':detail,'icon':whisiticon}) 
        return render(request,'other/mobilehtml.html',{'item':detail,'icon':whisiticon}) 
    return render(request,'other/mobilehtml.html',{'item':detail}) 

def trendings(request):
    trending_item=items_detail.objects.filter(trending=True)
    if request.user.is_authenticated:
        userid=request.user.id
        image=userimage.objects.all()
        for msg in image:
            if msg.user_id == userid:
                image=userimage.objects.get(user_id=userid)
                return render(request,'other/trending.html',{'image':image,"item":trending_item})
        return render(request,'other/trending.html',{"item":trending_item})
    return render(request,'other/trending.html',{"item":trending_item})

def profilechange(request):
    if request.user.is_authenticated:
        user_name=User.objects.get(id=request.user.id)
        image=userimage.objects.all()
        if request.method == "POST":
            if 'user-name' in request.POST:
                name=request.POST['user-name']
                user_name.username=name
                user_name.save()
                messages.success(request,'Username Successfully Changed')
                return redirect('userchange')
            elif "user-email" in request.POST:
                email=request.POST["user-email"]
                user_name.email=email
                user_name.save()
                messages.success(request,'Email successfully changed ')
                return redirect('userchange')
            elif 'user-pass1' in request.POST:
                pass1=request.POST['user-pass1']
                pass2=request.POST['user-pass2']
                if pass1 == pass2:
                    user_name.set_password(pass2)
                    user_name.save()
                    messages.success(request,' Successfully Password Updated Please login')
                    return redirect('loginpage')
                else:
                    messages.error(request,'Mismatch Your Password Please Tryagin')
                    return redirect('userchange')
            return redirect('mainpage')
        
        for msg in image:
            if msg.user_id == request.user.id:
                image=userimage.objects.get(user_id=request.user.id)    
                return render(request,'other/userchange.html',{"userchange":user_name,"image":image})
        return render(request,'other/userchange.html',{"userchange":user_name})
    return redirect('mainpage')

def add_to_cart(request):
    if request.headers.get('X-requested-with')=='XMLHttpRequest':
        if request.user.is_authenticated:
            data=json.load(request)
            product_id=(data['productid'])
            product_qty=(data['quandity'])
            product_status=items_detail.objects.get(id=product_id)
            if add_cart.objects.filter(user=request.user.id,product_id=product_id):
                return JsonResponse({'status':'product already in your cart'},status=200)
            else:
                if product_status.stack >= product_qty:
                    add_cart.objects.create(user=request.user,product_id=product_id,qty=product_qty)
                    return JsonResponse({'status':'product successfully add'},status=300)
                else:
                    return JsonResponse({'status':'stock not available'},status=200)
                    
            #return JsonResponse({'status':'successfully add to cart'},status=200)
        else:
            return JsonResponse({'status':'login to cart'},status=200)
        
    else:
        return JsonResponse({'status':'invalidaccess'},status=200)

def cartdetails(request):
    if request.user.is_authenticated:
        image=userimage.objects.all()
        car=add_cart.objects.filter(user=request.user)
        for msg in image:
            if msg.user_id==request.user.id:
                image=userimage.objects.get(user_id=request.user.id)
                if car:
                    return render(request,'other/cart.html',{'detail':car,'image':image,})
                else:
                    msg='no product in your cart '
                    return render(request,'other/cart.html',{'msg':msg,'image':image,})
        if car:
            return render(request,'other/cart.html',{'detail':car})
        else:
            msg='no product in your cart '
            return render(request,'other/cart.html',{'msg':msg})
    return redirect("mainpage")
        

def cart_product_remove(request,id):
    if request.user.is_authenticated:
        rem_product=add_cart.objects.get(id=id)
        rem_product.delete()
        return redirect('cart_details')
    return redirect('mainpage')

def cart_itemplus(request,id):
    if request.user.is_authenticated:
        cart=add_cart.objects.get(id=id)
        if cart.qty<10:
            cart.qty += 1
            cart.save()
            return redirect('cart_details')
        else:
            messages.warning(request,'maximun qty limit 1 to 10')
            return redirect('cart_details')
        
    
    return redirect('mainpage')

def cart_itemminus(request,id):
    if request.user.is_authenticated:
        cart=add_cart.objects.get(id=id)
        if cart.qty>1:
            cart.qty -= 1
            cart.save()
            return redirect('cart_details')
        else:
            messages.warning(request,'maximun qty limit 1 to 10')
            return redirect('cart_details')
    return redirect('mainpage')

def add_to_whisitlists(request):
    if request.headers.get('X-requested-with')=='XMLHttpRequest':
        if request.user.is_authenticated:
            data=json.load(request)
            product_id=(data['product'])
            product_status=items_detail.objects.get(id=product_id)
            if whisitlist.objects.filter(user=request.user.id,product_id=product_id):
                return JsonResponse({'status':'product alredy in your whisitlis'},status=200)
            else:
                whisitlist.objects.create(user=request.user,product_id=product_id)
                return JsonResponse({'status':'product added your whisitlist'},status=200)
        else:
            return JsonResponse({'status':'login to whisitlist'},status=200)
    return JsonResponse({'status':'invalidaccess'},status=200)

def whisitlist_item(request):
    if request.user.is_authenticated:
        list_item=whisitlist.objects.all()
        image=userimage.objects.all()
        #image=userimage.objects.get(user_id=request.user.id)
        for msg in image:
            if msg.user_id == request.user.id:
                image=userimage.objects.get(user_id=request.user.id)
                return render(request,'other/whisitlist.html',{'item':list_item,'image':image})
        return render(request,'other/whisitlist.html',{'item':list_item})
    return redirect('mainpage')


def whisitlist_item_remove(request,id):
    item_remove=whisitlist.objects.get(id=id)
    item_remove.delete()
    return redirect("whisitlist_details")
def user_remove(request):
    user_delete=User.objects.get(id=request.user.id)
    user_delete.delete()
    messages.success(request,'Your Account Successfully Deactivated')
    return redirect('registerpage')

def upload_user_picture(request):
    if request.user.is_authenticated:
        if userimage.objects.filter(user_id=request.user.id):
            image=userimage.objects.get(user_id=request.user.id)
            if request.method == "POST" and request.FILES["userpic"]:
                imagepic=request.FILES['userpic']
                if image:
                    image.userpic=imagepic
                    image.save()
                    messages.success(request,'Successfully Profilepicture Uploaded')
                    return redirect("user_uploadpicture")
            return render(request,'other/userpicture.html',{"image":image})
        else:
            if request.method == "POST" and request.FILES["userpic"]:
                imagepic=request.FILES['userpic']
                user_image=userimage(user=request.user,userpic=imagepic)
                user_image.save()
                messages.success(request,'Successfully Profilepicture Uploaded')
                return redirect("user_uploadpicture")
            #it's important function
            '''filename=FileSystemStorage()
                    vs=filename.save(image.name,image)
                    url=filename.url(vs)  '''
            # fileSystemStorage()
            
            return render(request,'other/userpicture.html')
    return redirect('mainpage')
    