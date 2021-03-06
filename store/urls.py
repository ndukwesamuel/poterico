from django.urls import path

from . import views

urlpatterns = [

	#Leave as empty string for base url
	path('', views.home, name="home"),
	path('store/', views.store, name="store"),
	path('cart/',views.cart, name='cart'),
	path('cart2/', views.cart2, name="cart2"),
	path('checkout/', views.checkout, name="checkout"),

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),

	# path('reg/', views.reg, name="reg"),
	# path('log_page/', views.log_page, name="log_page"),
	# path('logoutUser/', views.logoutUser, name="logoutUser"),
	path('product/', views.product, name="product"),




]