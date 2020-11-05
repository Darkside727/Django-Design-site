from django.views import View
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import  check_password
from DesginApp.models.customer import Customer
from DesginApp.models.products import Product



class Cart(View):

    def get(self, request):
        ids = list(request.session.get('cart').keys())
        print(ids)
        product = Product.get_products_by_id(ids)
        return render(request, 'cart.html', {'products' : product})
   
     

