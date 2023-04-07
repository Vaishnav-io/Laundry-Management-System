from django import forms
from .models import CRegistration
from .import models
from django.contrib.auth.models import User

# from .models import CRegistration


# class CRegistrationform(forms.ModelForm):
#     class Meta:
#         model = CRegistration
#         fields = ('cname', 'caddress', 'cemail', 'cphone', 'cpassword')
#         widgets = {
#             'cname': forms.TextInput(attrs={'class': 'form-control'}),
#             'caddress': forms.TextInput(attrs={'class': 'form-control'}),
#             'cemail': forms.TextInput(attrs={'class': 'form-control'}),
#             'cphone': forms.TextInput(attrs={'class': 'form-control'}),
#             'cpassword': forms.TextInput(attrs={'class': 'form-control'}),
#             'password1': forms.TextInput(attrs={'class': 'form-control'}),


#         }


class CustomerUserForm(forms.ModelForm):
    class Meta:
        model=User #django default model
        fields=['first_name','last_name','password','email','username']
        widgets = {
        'password': forms.PasswordInput()
        }
class CustomerForm(forms.ModelForm):
    class Meta:
        model= models.CRegistration
        fields=['address','mobile','profile_pic']


    
class BusinessUserForm(forms.ModelForm):
    class Meta:
        model=User #django default model
        fields=['first_name','password','email','username']
        widgets = {
        'password': forms.PasswordInput()
        }
class BusinessForm(forms.ModelForm):
    class Meta:
        model= models.BRegistration
        fields=['address','mobile','business_pic','lic_no','contactname']

        
       

class DeliveryUserForm(forms.ModelForm):
    class Meta:
        model=User #django default model
        fields=['first_name','password','email','username']
        widgets = {
        'password': forms.PasswordInput()
        }
        
class DeliveryForm(forms.ModelForm):
    class Meta:
        model= models.DRegistration
        fields=['address','mobile','delivery_pic','lic_pic','lic_no']

class BDetailsForm(forms.ModelForm):
    class Meta:
        model=models.BDetails
        fields=['first_name','rate1','rate2','rate3','rate4','rate5','rate6','services1','services2','services3','services4','services5','services6']