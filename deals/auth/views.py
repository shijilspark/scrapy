import json
from django import forms
from django.contrib.auth.models import User
# from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect

from auth.models import UserForm, UserProfile, WishList
from scrapdeals.models import SubscribeModel

def auth(request):
    if request.method == 'POST':
        usr = request.POST['username']
        pswrd = request.POST['password']
        if '@' in usr:
            try:
                check = User.objects.get(email=usr)
                usr = check.username
            except:
                pass
        user = authenticate(username=usr, password=pswrd)
        if user is not None:
            if user.is_active:
                login(request, user)
                user_id = request.user.id
                user_wishlist = WishList.objects.filter(user_id=user_id)
                items = []
                for item in user_wishlist:
                    items.append(item.wishlist)            
                items = json.dumps(items)
            return render(request, 'auth.html' ,{'user': request.user, 'list': items})
        else:
            context = {'details' : 'Invalid login'}
            return render(request,'image_view.html', context)
    
    else:
        if request.user.is_authenticated():
            user_id = request.user.id
            user_wishlist = WishList.objects.filter(user_id=user_id)
            items = []
            for item in user_wishlist:
                items.append(item.wishlist)            
            items = json.dumps(items)
            return render(request, 'auth.html' ,{'user': request.user, 'list': items})

        else:
            return render(request,'image_view.html', context)


def user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():        
            usr = form.cleaned_data['username']
            fname = form.cleaned_data['firstname']
            lname = form.cleaned_data['lastname']
            mail = form.cleaned_data['email']
            pswrd = form.cleaned_data['password']
            no = form.cleaned_data['phone_no']
            subscribe = form.cleaned_data['subscribe']
            
            user = User.objects.create_user(usr, mail, pswrd)
            profile = UserProfile()
            profile.user = user
            profile.firstname = fname
            profile.lastname = lname
            profile.phone_no = no
            profile.email = mail
            profile.save()

            if subscribe == True:
                new_user = SubscribeModel()
                new_user.email = mail
                new_user.save()                                         
        else:
            return render(request, 'user.html',{'form': form,})
        return render(request, 'auth.html', {'user': usr})
    else:
        form = UserForm()
    return render(request, 'user.html',{'form': form,})

def logout_views(request):
    logout(request)    
    return render(request, 'image_view.html', {'details' : 'Signed Out'})

@login_required(login_url='index')
def wishlist_views(request):
    user_id = request.user.id
    user_wishlist = WishList.objects.filter(user_id=user_id)
    return render(request, 'wishlist.html',{'list': user_wishlist})

@csrf_exempt
@login_required(login_url='index')
def add_to_cart(request):

    if request.method == 'POST':
        item_id = request.POST['item_id']
        deal_name = request.POST['deal_name']
    
    user = request.user
    if not user.wishlist_set.filter(wishlist=item_id).exists():
        new_item = WishList()
        new_item.user = user
        new_item.deal_name = deal_name
        new_item.wishlist = item_id
        new_item.save()
        
    data={'item_id':item_id}
    data_json = json.dumps(data)
    return HttpResponse(data_json, mimetype='application/json')


@csrf_exempt
@login_required(login_url='index')
def remove_from_cart(request):
    if request.method == 'POST':
        item_id = request.POST['item_id']
        deal_name = request.POST['deal_name']
    
    wish_list = WishList.objects.values_list('wishlist', flat=True)
    deal_list = WishList.objects.values_list('deal_name',flat=True)
    if item_id in wish_list: 
        WishList.objects.filter(wishlist=item_id).delete()
    if deal_name in deal_list:
        WishList.objects.filter(deal_name=deal_name).delete()
    
    data={'item_id':item_id}
    data_json = json.dumps(data)
    return HttpResponse(data_json, mimetype='application/json')