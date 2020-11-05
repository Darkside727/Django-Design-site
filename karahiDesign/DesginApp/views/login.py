from django.views import View
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import  check_password
from DesginApp.models.customer import Customer



class Login(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session["customer_id"] = customer.id
                request.session["customer_email"] = customer.email

                error_message = "yes"
            else:
                error_message = "no"
        flash_messg = {
             "error_message" : error_message
        }
        return render(request, 'login.html', flash_messg)


def logout(request):
    request.session.clear()
    return redirect('login')
