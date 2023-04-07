from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class CRegistration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    profile_pic = models.ImageField(upload_to='Customer_pics/CustomerProfile/', null=True, blank=True)
    address = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20) #null=True
    status = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.user}"
    

class BRegistration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    business_pic = models.ImageField(upload_to='Business_pics/BusinessProfile/', null=True, blank=True)
    contactname = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    lic_no = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20) #null=True
    status = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.user}"


class DRegistration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    delivery_pic = models.ImageField(upload_to='Delivery_pics/DeliveryProfile/', null=True, blank=True)
    lic_pic = models.ImageField(upload_to='Delivery_pics/DL_pic/', null=True, blank=True)
    address = models.CharField(max_length=100)
    lic_no = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20) #null=True
    Approve = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.user}"
    

class BDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name=models.CharField(max_length=100,null=True)
    services=(
        ('None','None'),
        ('Irioning','Irioning'),
        ('Dry Cleaning','Dry Cleaning'),
        ('wet Cleaning','wet Cleaning'),
        ('Shoe laundry','Shoe laundry'),
        ('Chemical Washing','Chemical Washing'),
        ('Carpet Laundry','Carpet Laundry'),
    )
    services1 = models.CharField(max_length=100, choices=services,null=True,default='None')
    rate1 = models.CharField(max_length=100,null=True,default=0)
    services2 = models.CharField(max_length=100, choices=services,null=True,default='None')
    rate2 = models.CharField(max_length=100,null=True,default=0)
    services3 = models.CharField(max_length=100, choices=services,null=True,default='None')
    rate3 = models.CharField(max_length=100,null=True,default=0)
    services4 = models.CharField(max_length=100, choices=services,null=True,default='None')
    rate4 = models.CharField(max_length=100,null=True,default=0)
    services5 = models.CharField(max_length=100, choices=services,null=True,default='None')
    rate5 = models.CharField(max_length=100,null=True,default=0)
    services6 = models.CharField(max_length=100, choices=services,null=True,default='None')
    rate6 = models.CharField(max_length=100,null=True,default=0)

class B_C_Request(models.Model):
    userB = models.ForeignKey(User,related_name='topic_userB', on_delete=models.CASCADE,  blank = True)
    userC = models.ForeignKey(User,related_name='topic_userC', on_delete=models.CASCADE,  blank = True)
    userD = models.ForeignKey(User,related_name='topic_userD', on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=1000,null=True,default=0)
    ph = models.CharField(max_length=1000,null=True,default=0)
    clothingItemsname = models.CharField(max_length=1000,null=True,default=0)
    clothingItems = models.CharField(max_length=1000,null=True,default=0)
    clothingqty = models.CharField(max_length=1000,null=True,default=0)
    rate = models.CharField(max_length=1000,null=True,default=0)

    status =models.CharField(max_length=100,null=True,default=0)
    def __str__(self):
        return f"{self.userB}"

    



    

