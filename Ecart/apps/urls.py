from django.urls import path
from .views import *
from . import views
app_name='apps'

urlpatterns=[
    path('',AllProducts.as_view(),name='allprod'),
    path('all-products/',AllCategory.as_view(),name='allcats'),
    path('product/<slug:slug>/',ProductDetails.as_view(),name='prodetails'),
    path('category/<slug:slug>/',ProByCat.as_view(),name='probycat'),
    path('register',views.register,name='registration'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('addtocart/<int:pro_id>/',AddToCart.as_view(),name='addcart'),
    path('mycart',MyCart.as_view(),name='mycart')

]