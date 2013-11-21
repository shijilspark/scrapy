from django.contrib import admin
from auth.models import  UserProfile, WishList

class WishListAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Deal Name', {'fields': ['deal_name']}),
        ('Item Url',{'fields': ['wishlist']}),
    ]
    search_fields = ['wishlist']
    list_filter = ['deal_name']
    list_display = ['user','deal_name','wishlist']


admin.site.register(UserProfile)
admin.site.register(WishList, WishListAdmin)