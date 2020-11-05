from django.urls import path
from .views.home import home
from .views.home import contact
from .views.account import Account
from .views.product import Products
from .views.cart import Cart
from .views.check_out import Check_out
from .views.login import Login, logout
from django.conf.urls.static import static
from django.conf import settings
from .views.orders import Orders


urlpatterns = [
    path('', home, name="home"),
    path('contact', contact, name="contact"),
    path('account', Account.as_view(), name="account"),
    path('login', Login.as_view(), name="login"),
    path('logout', logout, name="logout"),
    path('product', Products.as_view(), name="products"),
    path('cart', Cart.as_view(), name="cart"),
    path('checkout', Check_out.as_view(), name="checkout"),
    path('order', Orders.as_view(), name="order"),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
