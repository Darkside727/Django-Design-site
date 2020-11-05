from django.views import View
from django.shortcuts import render , redirect
from DesginApp.models.products import Product
from DesginApp.models.category import Category
from django.views import View


class Products(View):
    
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')  
        print(cart)
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                   if quantity <= 1:
                       cart.pop(product)
                   else:
                        cart[product] = quantity - 1
                else:
                   cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        
        return redirect('products')
    

    
    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        product = None
        product = Product.get_all_product()
        category = Category.get_all_category()
        category_id = request.GET.get('category')
        if category_id:
            product = Product.get_all_products_by_category_id(category_id)
            if not product:
                product_info = {
                    "productInfo" : True,
                    'categories' : category
                    }
                return render(request, 'product.html', product_info)

                
        else:
            product = Product.get_all_product()
        data = {
            'products' : product,
            'categories' : category
        }
        return render(request, 'product.html', data)   
