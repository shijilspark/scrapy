from django.conf.urls import patterns, url

from auth import views

urlpatterns = patterns('',
	url(r'^auth/$',views.auth, name='auth'),
	url(r'^user/$',views.user, name='user'),
	url(r'^logout/$',views.logout_views, name='logout'),
	url(r'^wishlist/$',views.wishlist_views, name='wishlist'),
	url(r'^add_to_cart/$',views.add_to_cart, name='add_to_cart'),
	url(r'^remove_from_cart/$',views.remove_from_cart, name='remove_from_cart'),
)