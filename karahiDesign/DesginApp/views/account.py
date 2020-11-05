from django.views import View
from django.shortcuts import render , redirect
from django.http import HttpResponse
from DesginApp.models.customer import Customer
from django.contrib.auth.hashers import make_password


class Account(View):

    def get(self, request):
        return render(request, 'account.html')


    def post(self, request):
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        email  = request.POST.get('email')
        contact  = request.POST.get('contact')
        password  = request.POST.get('password')

        value = {
         'name' : name,
         'lastname' : lastname,
         'email' : email,
         'contact' : contact,
         'password' : password,
        }

        error_message = None

        customer = Customer(
            first_name=name,
            last_name=lastname,
            phone=contact,
            email=email,
            password=password,
        )
        error_message = self.validateCustomer(customer)
        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('login')
        else:

            data = {

                'error' : error_message,
                'values' : value
            }

            return render(request, 'account.html', data)


    def validateCustomer(self, customer):
        error_message = None
        if not customer.first_name:
            error_message = "First Name Required"
        elif len(customer.first_name)< 4:
            error_message = "First Name must be 4 char long or more"
        elif not customer.last_name:
            error_message = "Last Name Required"
        elif len(customer.last_name) < 4:
            error_message = "Last Name must be 4 char long or more"
        elif not customer.phone:
                error_message = 'Phone Number required'
        elif len(customer.phone) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len(customer.password) < 6:
            error_message = 'Password must be 6 char long'
        elif len(customer.email) < 5:
            error_message = 'Email must be 5 char long'
        elif customer.isExits():
            error_message = 'Email Address Already Registered..'


        return error_message



