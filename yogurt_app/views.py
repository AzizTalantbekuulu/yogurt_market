from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import login, logout
from .models import *


def register_user(request):

    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['login']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        re_password = request.POST['re-password']
        if password != re_password:
            return render(request, "yogurt_app/registration.html", {'error': True})

        new_user = CustomUser.objects.create(
            email=email,
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        new_user.save()
        return redirect('main')
    return render(request, "yogurt_app/registration.html", {'error': False})


def log_in_user(request):

    error = False
    context = {'error': error}

    if request.method == 'POST':
        username = request.POST['login']
        password = request.POST['password']
        users = CustomUser.objects.all()
        user = None
        for i in users:
            if i.username == username and i.password == password:
                user = i
        if user:
            login(request, user)
            return redirect("main")
        error = True
        context = {'error': error}

    return render(request, "yogurt_app/login.html", context)


def log_out_user(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("main")


def redirect(request):
    return HttpResponseRedirect(reverse('main'))


def main(request):
    yogurts = Yogurt.objects.all()
    context = {
        'yogurts': yogurts
    }

    if request.user.is_authenticated:
        user = CustomUser.objects.get(pk=request.user.pk)
        context = {
            'yogurts': yogurts,
            'user': user
        }

    return render(request, 'yogurt_app/main.html', context)


def yogurt_detail(request, pk):
    yogurt = Yogurt.objects.get(pk=pk)
    context = {
        'yogurt': yogurt
    }

    if request.user.is_authenticated:
        user = CustomUser.objects.get(pk=request.user.pk)
        context = {
            'yogurt': yogurt,
            'user': user
        }

    return render(request, 'yogurt_app/yogurt.html', context)


@login_required(login_url="/log_in/")
def create_order(request, pk):
    user = CustomUser.objects.get(pk=request.user.pk)
    cities = City.objects.all()
    yogurt = Yogurt.objects.get(pk=pk)
    context = {
        'user': user,
        'cities': cities,
        'yogurt': yogurt
    }
    if request.method == 'POST':
        try:
            user_first_name = request.POST['first_name']
            user_last_name = request.POST['last_name']
            user_email = request.POST['email']
            address = request.POST['address']
            city = request.POST['city']
            price = request.POST['price']

            order = Order.objects.create(
                user=user,
                city=city,
                address=address,
                user_email=user_email,
                user_first_name=user_first_name,
                user_last_name=user_last_name,
                yogurt=yogurt,
                total_price=price
            )
            order.save()
            context = {
                'order': order,
                'yogurt': yogurt
            }
            return render(request, 'yogurt_app/order_submit.html', context)
            #return redirect('main')
        except:
            return HttpResponse(status=500)

    return render(request, 'yogurt_app/order.html', context)

