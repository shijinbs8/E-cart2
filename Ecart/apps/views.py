from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from .models import Products, Category,Cart,Cart



# Create your views here.


class AllProducts(TemplateView):
    template_name = 'category.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['product_list']=Products.objects.all()
        context['allcategories']=Category.objects.all()
        return context

class AllCategory(TemplateView):
    template_name = 'allcats.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['allcategories']=Category.objects.all()
        return context

class ProductDetails(TemplateView):
    template_name = 'productdetails.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        c_slug=self.kwargs['slug']
        product=Products.objects.get(slug=c_slug)
        context['product']=product
        return context

class ProByCat(TemplateView):
    template_name = 'probycat.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        cc_slug=self.kwargs['slug']
        category=Category.objects.get(slug=cc_slug)
        context['category']=category
        context['all']=Products.objects.all().filter(category=category)
        return context
def register(request):
    if request.method== 'POST':
        username1=request.POST["name"]
        email1=request.POST["email"]
        password1=request.POST['password']
        cpassword=request.POST['cpassword']
        if password1==cpassword:
            if User.objects.filter(username=username1).exists():
                messages.info(request,"USERNAME TAKEN")
                return redirect('register')
            elif User.objects.filter(email=email1).exists():
                messages.info(request,"EMAIL ALREADY TAKEN")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username1,email=email1,
                                              password=password1)
                user.save();
                print("user created")
                return redirect('/')
        else:
            messages.info(request,"Password not matching")
            return redirect('register/')
        return redirect('/')
    return render(request,'registration.html')


def login(request):
    if request.method=='POST':
        username=request.POST["name"]
        password2=request.POST["password"]
        user=auth.authenticate(username=username,password=password2)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid login")
            return redirect('login')
    return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')

class AddToCart(TemplateView):
    template_name = 'addcart.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        # get product id
        product_id=self.kwargs['pro_id']
        #get product
        product_object=Products.objects.get(id=product_id)
        cart_id=self.request.session.get('cart_id',None)
        if cart_id:
            cartobj=Cart.objects.get(id=cart_id)
            print('old cart')
            #fetching from models cartproduct
            this_product_in_cart=cartobj.cartproduct_set.filter(product=product_object)
            #if already exists in cart:
            if this_product_in_cart.exists():
                cartproduct=this_product_in_cart.last()
                cartproduct.quantity+=1
                cartproduct.subtotal+=product_object.price
                cartproduct.save()
                cartobj.total+=product_object.price
                cartobj.save()
            # new item added to cart
            else:
                cartproduct=CartProduct.objects.create(cart=cartobj,product=product_object,rate=product_object.price,quantity=1,subtotal=product_object.price)
                cartobj.total += product_object.price
                cartobj.save()
        else:
            cartobj=Cart.objects.create(total=0)
            self.request.session['cart_id']=cartobj.id
            print('new cart')
            cartproduct = CartProduct.objects.create(cart=cartobj, product=product_object, rate=product_object.price,
                                                     quantity=1, subtotal=product_object.price)
            cartobj.total += product_object.price
            cartobj.save()

        return context
class MyCart(TemplateView):
    template_name = 'mycart.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        cart_id=self.request.session.get['cart_id',None]
        if cart_id:
            cart=Cart.objects.get(id=cart_id)
        else:
            cart=None
        context['cart']=cart
        return context