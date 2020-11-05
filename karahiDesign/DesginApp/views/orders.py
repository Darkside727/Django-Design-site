from django.views import View
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import  check_password
from DesginApp.models.customer import Customer
from DesginApp.models.products import Product
from DesginApp.models.orders import Order


class Orders(View):

    def get(self, request):
        customer = request.session.get('customer_id')
        orders = Order.get_orders_by_id(customer)
        orders = orders.reverse()
        return render(request, 'orders.html', {'orders' : orders})

