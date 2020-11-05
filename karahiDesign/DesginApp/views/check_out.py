from django.views import View
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import  check_password
from DesginApp.models.customer import Customer
from DesginApp.models.products import Product
from DesginApp.models.orders import Order


class Check_out(View):

    def post(self, request):
        addr = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer_id')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))

        for product in products:
            order = Order(customer = Customer(id = customer), product = product, price = product.price,
             address  = addr,
             phone = phone,
             quantity = cart.get(str(product.id)))
            
            order.placeorder()
            request.session['cart'] = {}
        return redirect('cart')

