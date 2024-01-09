from django.db import models
from django.contrib.auth.models import User

class userimage(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    userpic=models.ImageField()

class collections(models.Model):
    categeory=models.CharField(max_length=100)
    image=models.ImageField()
    def __str__(self):
        return self.categeory

class items(models.Model):
    categeries=models.ForeignKey(collections, on_delete=models.CASCADE,null=True)
    item_name=models.CharField(max_length=100,)
    item_image=models.ImageField(null=False)
    status=models.BooleanField(null=True)
    def __str__(self):
        return self.item_name


class items_detail(models.Model):
    brand=models.ForeignKey(items,on_delete=models.CASCADE)
    brand_model=models.CharField(max_length=30,null=False)
    model_image=models.ImageField(null=False)
    prize=models.FloatField(null=True)
    stack=models.IntegerField(null=True)
    trending=models.BooleanField(null=True)

    def __str__(self):
        return self.brand_model
    
class mobiledetails(models.Model):
    mobile_model=models.ForeignKey(items_detail,on_delete=models.CASCADE)
    storage=models.CharField(max_length=50)
    rear_camera=models.CharField(max_length=100)
    fornd_camera=models.CharField(max_length=100)
    display=models.CharField(max_length=100)
    processor=models.CharField(max_length=100)
    battery=models.CharField(max_length=100)
    network=models.CharField(max_length=100)
    

class add_cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(items_detail,on_delete=models.CASCADE)
    qty=models.IntegerField(null=False,blank=False)

class whisitlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(items_detail,on_delete=models.CASCADE)




