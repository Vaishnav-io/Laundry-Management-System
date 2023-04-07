from django.urls import path
from django.contrib.auth.views import LoginView
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views



app_name='laundry'
urlpatterns = [
    path('', views.index, name="index"),
    path('index/', views.index, name="index"),
    path('how-it-works/', views.about, name="about"),
    path('help/', views.help, name="help"),
    path('contact/', views.contact, name="contact"),

    path('login/', LoginView.as_view(template_name="login.html"), name="login"),
    path('afterlogin/', views.afterlogin_view, name="afterlogin"),
    path('logout/',auth_views.logout_then_login,name="logout"),

    path('user/sign-up/', views.cregistration, name="cregistration"),
    path('vendor/sign-up/', views.bregistration, name="bregistration"),
    path('delivery-team/sign-up/', views.dregistration, name="dregistration"),

    path('user/home/', views.cdashboard, name="cdashboard"),
    path('user/profile/', views.cprofile, name="cprofile"),
    path('user/home/place-order/', views.shopnames, name="shopnames"),
    path('user/home/orders-status/', views.UserOrderStatus, name="UserOrderStatus"),
    path('ordercompleted', views.ordercompleted, name="ordercompleted"),

    path('bussiness/home/', views.bdashboard, name="bdashboard"),
    path('bussiness/profile/', views.bprofile, name="bprofile"),
    path('bussiness/home/addshop/', views.addshop, name="addshop"),
    path('bussiness/home/orders/', views.requestToPickup, name="requestToPickup"), 
    path('bussiness/home/orders/send-delivery/', views.sendDelivery, name="sendDelivery"),
    path('bussiness/home/orders/send-delivery/choose-agent', views.saveB_COrder, name="saveB_COrder"),

    path('delivery-agent/home/', views.ddashboard, name="ddashboard"),
    path('delivery-agent/profile/', views.dprofile, name="dprofile"),
    path('delivery-agent/home/pickup/', views.deliveryapproval, name="deliveryapproval"),
    path('delivery-agent/home/pickup/accept', views.acceptOrder, name="acceptOrder"),
    path('delivery-agent/home/pickup/decline', views.rejectOrder, name="rejectOrder"),

    path('saveItems/', views.saveItems, name="saveItems"),
    path('customersaveItems/', views.customersaveItems, name="customersaveItems"),
    path('ShopCustomer/', views.ShopCustomer, name="ShopCustomer"),
    path('saveRate/', views.saveRate, name="saveRate"),

   
]

      
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
