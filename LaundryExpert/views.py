from django.shortcuts import redirect,render
from .forms import *            # add  * so everything will be added automatically
from .models import *       
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404
from django.urls import reverse,resolve
# from .models import registration
 # Create your views here.
from django.core.mail import send_mail

                # STATIC PAGES
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')
def help(request):
    return render(request,'help.html')
def contact(request):
    return render(request,'contact.html')



                #REGISTRATIONS...

def cregistration(request): 
    form= CustomerUserForm()
    userForm1= CustomerForm()
    mydict={'form':form,'userForm1':userForm1}
    if request.method=='POST':
        form= CustomerUserForm(request.POST)
        userForm1= CustomerForm(request.POST, request.FILES)#profile pic
        if form.is_valid() and userForm1.is_valid():
            print(1)
            user=form.save()
            user.set_password(user.password)
            user.save()
            messages.success(request, 'Your account has been created! Please log in to continue...')
            print(user)
            Customer=userForm1.save(commit=True) #VARIABLE
            Customer.user=user
            Customer.save()
            print(Customer)
            group = Group.objects.get_or_create(name='Customers')#group name
            group[0].user_set.add(user)
            return redirect('laundry:login')
        messages.success(request, 'It is a mistake on our end. Please try again!!')

    return render(request,'cregistration.html',context=mydict)

def bregistration(request):
   
    form= BusinessUserForm()
    buserForm1= BusinessForm()
    mydict={'form':form,'buserForm1':buserForm1}
    if request.method=='POST':
        
        form= BusinessUserForm(request.POST)
        buserForm1= BusinessForm(request.POST, request.FILES) #profile pic
        if form.is_valid() and buserForm1.is_valid():           
            print(1)
            user=form.save()
            # send send_mail
            email=user.email
            print('email is',email)
            subject = 'Subject of the email'
            message = 'Message of the email'
            from_email = 'laundrydazzle@example.com'
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list)
            # send send_mail

            user.set_password(user.password)
            user.save()
            messages.success(request, 'Your account has been created! Please log in to continue...')
            print(user)
            BRegistration=buserForm1.save(commit=True) #VARIABLE
            BRegistration.user=user
            BRegistration.save()
            print(BRegistration)
            group = Group.objects.get_or_create(name='Business') #group name
            group[0].user_set.add(user)

            return redirect('laundry:login')
        messages.success(request, 'It is a mistake on our end. Please try again!!')


    return render(request,'bregistration.html',context=mydict)

def dregistration(request):
    form= DeliveryUserForm()
    duserForm1= DeliveryForm()
    mydict={'form':form,'duserForm1':duserForm1}
    if request.method=='POST':
        form= DeliveryUserForm(request.POST)
        duserForm1= DeliveryForm(request.POST, request.FILES) #profile pic
        if form.is_valid() and duserForm1.is_valid():
            print(1)
            user=form.save()
            user.set_password(user.password)
            user.save()
            messages.success(request, 'Your registration has been completed! Please wait for verification from the administrator. Then you will be able to log in')
            print(user)
            DRegistration=duserForm1.save(commit=True) #VARIABLE
            DRegistration.user=user
            DRegistration.save()
            print(DRegistration)
            group = Group.objects.get_or_create(name='Delivery') #group name
            group[0].user_set.add(user)
            return redirect('laundry:index')
        messages.success(request, 'It is a mistake on our end. Please try again!!')

    return render(request,'dregistration.html',context=mydict)

def addshop(request):
    var1=BRegistration.objects.get(user_id=request.user)
    cr=var1.user.first_name
    print(cr)
  
    form2=BDetailsForm(instance=var1.user)
    mydict={
       'var1':var1,
       'cr':cr,
        'form2':form2,
    }
    if request.method=='POST':
        # var1=BRegistration.objects.get(user_id=request.user)
        
        form2=BDetailsForm(request.POST)
        if form2.is_valid():
            user1=form2.save()
            user1.user=request.user
            user1.save()
            return redirect('laundry:bdashboard')
        else :
            print("Invalid Form")
    return render(request,'addshop.html',context=mydict)


                #GROUPS...

def Customer(user):
    print(user)
    return user.groups.filter(name='Customers').exists()

def Business(user):
    print(user.groups.filter(name='Business').exists())
    return user.groups.filter(name='Business').exists()

def Delivery(user):
    print("Delivery")
    return user.groups.filter(name='Delivery').exists()


                #LOGOUT

# @login_required
# def logout_user(request):
#     logout(request)
#     return redirect('/login')

                #LOGIN REQUIRED PAGES

@login_required(login_url='login')
@user_passes_test(Customer)
def cdashboard(request):
    return render(request,'cdashboard.html')

@login_required(login_url='laundry:login')
@user_passes_test(Customer)
def cprofile(request):    
    cust =CRegistration.objects.get(user_id=request.user.id)
    #my_volunteer1 = Doctor.objects.filter(my_volunteer.gender)
    # c=far.mobile
    if request.method == "POST":
        cust =CRegistration.objects.get(user_id=request.user)
        form = CustomerUserForm(request.POST, instance=cust.user)

        userForm1 = CustomerForm(request.POST, instance=cust)
        if form.is_valid() and userForm1.is_valid():
            user=form.save()
            if(user.password!=""):
                user.set_password(user.password)            
            user.save()
            print(form)
            userForm1.save()
            messages.success(request, 'Your Account has been Updated')
            # return redirect('cdashboard')
            url = reverse('laundry:login')
            return redirect(url)
    else:
            form = CustomerUserForm(instance=cust.user)
            userForm1 = CustomerForm(instance=cust)
            context = {

            'form': form,
            'userForm1': userForm1,
            # 'c':c
            }
    return render(request, 'cprofile.html', context)


@login_required(login_url='laundry:login')
@user_passes_test(Business)
def bdashboard(request):
    return render(request,'bdashboard.html')
    # return redirect('laundry:bdashboard')

@login_required(login_url='laundry:login')
@user_passes_test(Business)
def bprofile(request):    
    bus =BRegistration.objects.get(user_id=request.user.id)
    #my_volunteer1 = Doctor.objects.filter(my_volunteer.gender)
    # c=far.mobile
    if request.method == "POST":
        bus =BRegistration.objects.get(user_id=request.user)
        form = BusinessUserForm(request.POST, instance=bus.user)

        buserForm1 = BusinessForm(request.POST, instance=bus)
        if form.is_valid() and buserForm1.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            print(form)
            buserForm1.save()
            messages.success(request, 'Your Account has been Updated')
            url = reverse('laundry:login')
            return redirect(url)
    else:
            form = BusinessUserForm(instance=bus.user)
            buserForm1 = BusinessForm(instance=bus)
            context = {

            'form': form,
            'buserForm1': buserForm1,
            # 'c':c
            }
    return render(request, 'bprofile.html', context)



@login_required(login_url='login')
@user_passes_test(Delivery)
def ddashboard(request):
    return render(request,'ddashboard.html')

@login_required(login_url='login')
@user_passes_test(Delivery)
def dprofile(request):    
    deliv =DRegistration.objects.get(user_id=request.user.id)
    #my_volunteer1 = Doctor.objects.filter(my_volunteer.gender)
    # c=far.mobile
    if request.method == "POST":
        deliv =DRegistration.objects.get(user_id=request.user)
        form = DeliveryUserForm(request.POST, instance=deliv.user)

        duserForm1 = DeliveryForm(request.POST, instance=deliv)
        if form.is_valid() and duserForm1.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            print(form)
            duserForm1.save()
            messages.success(request, 'Your Account has been Updated')
            url = reverse('laundry:login')
            return redirect(url)
    else:
            form = DeliveryUserForm(instance=deliv.user)
            duserForm1 = DeliveryForm(instance=deliv)
            context = {

            'form': form,
            'duserForm1': duserForm1,
            # 'c':c
            }
    return render(request, 'dprofile.html', context)


                #AFTER LOGIN FUNCTIONS
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
 
def afterlogin_view(request):
    if Customer(request.user):   
        print('username',request.user)
        print('username type',type(request.user))
        u=str(request.user)
        request.session['user']=u
        request.session['userid']=request.user.id
        # print('u')
        # return redirect('http://127.0.0.1:8000/cdashboard')
        url = reverse('laundry:cdashboard')
        return redirect(url)
        # resolve('/cdashboard/')

    elif Business(request.user):
        print("Bu")
        request.session['userid']=request.user.id
        # return redirect('http://127.0.0.1:8000/bdashboard')
        url = reverse('laundry:bdashboard')
        return redirect(url)
        
    elif Delivery(request.user):
        print("Delivery")
        request.session['userid']=request.user.id
        var=DRegistration.objects.all().filter(user_id=request.user.id,Approve=True)
        if var:
                url = reverse('laundry:ddashboard')
                return redirect(url)
        # else:
        #     messages.success(request,'You account Is Not Authorized/approved')
        #     return render(request,'login.html')
        else:
            messages.warning(request, 'Your Account Is Not Authorized/Approved, wait for the verification')
            return render(request, 'index.html')
        
        
 

def shopnames(request):   
    dt=BRegistration.objects.all()
    my_dict={
        'data':dt,
        'uid':request.session['userid']
    } 
    return render(request,'shopname.html',context=my_dict)

def ShopCustomer(request):  
    bc=B_C_Request.objects.filter(status="0")
    bcDetail=BDetails.objects.filter(user__id=request.GET["bid"])
    my_dict={         
        "bid":request.GET["bid"],
        "uid":request.GET["uid"],
        "bc":bc,
        'bcDetail':bcDetail
    }    
    print(bcDetail)
    return render(request,'shopcustomerItems.html',context=my_dict)

def customersaveItems(request):
    if request.method=='GET':
        dt=B_C_Request()     
        dt.userB=get_object_or_404(User,pk=request.GET["bid"])       
        dt.userC=get_object_or_404(User,pk=request.GET["uid"])  
        dt.status="0"
        BReg=CRegistration.objects.filter(user=get_object_or_404(User,pk=request.GET["uid"])).all()
        dt.address=BReg[0].address
        dt.ph=BReg[0].mobile
        dt.clothingItemsname=request.GET["itemname"]
        dt.clothingItems=request.GET["items"]
        dt.clothingqty=request.GET["qty"]
        dt.save()   
    return redirect('/ShopCustomer/?bid='+request.GET["bid"]+'&uid='+request.GET["uid"])

def requestToPickup(request):   
    # dt=B_C_Request.objects.values('userC','userC__username','userC__id','userC__email','status','address','ph').filter(status="0").distinct()
    dt=B_C_Request.objects.values('userC','userC__username','userC__id','userC__email','status','address','ph').exclude(status="C").distinct()
    # print(dt)
    my_dict={
        'data':dt,        
    } 
    return render(request,'requestToPickup.html',context=my_dict) 

def sendDelivery(request):   
    dt=DRegistration.objects.all()
    my_dict={
        'data':dt, 
        "pid":request.GET["id"]    
    } 
    return render(request,'sendDelivery.html',context=my_dict)



def saveB_COrder(request):
    dt=B_C_Request.objects.filter(userC=request.GET["pid"],status=0).update(userD=get_object_or_404(User,pk=request.GET["id"]) ,status="D")
    # dt.userD=get_object_or_404(User,pk=request.GET["id"]) 
    # dt.status="D"
    # dt.update()
    # return redirect('laundry:requestToPickup')
    url = reverse('laundry:requestToPickup')
    return redirect(url)

def ordercompleted(request):
    # dt=B_C_Request.objects.filter(userC=request.GET["pid"],status="A").update(status="C")
    my_dict={
       
        "pid":request.GET["pid"]    
    } 
    return render(request,'priceenter.html',context=my_dict)

def saveRate(request):
    # print(request.GET["amount"])
    # dt=B_C_Request.objects.filter(userC=request.GET["pid"],status="A").update()
    dts=B_C_Request.objects.filter(userC=request.GET["pid"],status="A").update(rate="10",status="C")    
    url = reverse('laundry:requestToPickup')
    return redirect(url)
     
    

    
def saveItems(request):
    if request.method=='GET':
        dt=B_C_Request.objects.get(pk=request.GET["pid"])
        dt.userD=get_object_or_404(User,pk=request.GET["id"]) 
        dt.status="D"
        dt.clothingItems=request.GET["items"]
        dt.save()   
    return redirect('requestToPickup')


def deliveryapproval(request):
    dt=B_C_Request.objects.filter(status='D')
    my_dict={
        'data':dt,        
    } 
    return render(request,'deliveryapproval.html',context=my_dict)

def acceptOrder(request):
    dt=B_C_Request.objects.get(pk=request.GET["id"])   
    dt.status="A"
    dt.save()
    return redirect('laundry:deliveryapproval')

def rejectOrder(request):
    dt=B_C_Request.objects.get(pk=request.GET["id"])   
    dt.status="R"
    dt.save()
    return redirect('laundry:deliveryapproval')


def UserOrderStatus(request):
    dt=B_C_Request.objects.values('userC','status','userD__username','rate').distinct()
    my_dict={
        'data':dt,        
    } 
    return render(request,'shopname_status.html',context=my_dict)


