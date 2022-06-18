from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from .models import *
from django.forms import inlineformset_factory
from .forms import *


def create_buying(request):   # main page, redirect for create order

    if request.method == 'POST':
        buy = Buying()
        print('-------------')
        buy.save()
        print(buy.id)
        buy.Check = buy.id
        buy.save()
        return redirect('create-buy-order', pk=buy.id)

    context = {
            # 'form': form,
            # 'buying': buying,
            # 'orders': orders
        }
    return render(request, 'coffeshop/create_buying.html', context)


def create_buy_order(request, pk):  # create order, select product
    buying = Buying.objects.get(id=pk)
    orders = Order.objects.filter(Buying=buying)
    form = OrderForm(request.POST or None)
    form2 = BuyingForm(request.POST or None)
    context = {
        'form': form,
        'buying': buying,
        'orders': orders,
    }
    if request.method == 'POST':
        if form.is_valid():
            print('----2----')
            order = form.save(commit=False)
            order.Buying = buying
            # print(order)
            order.save()
            return redirect("detail-order", pk=order.id)
            return redirect('detail-buying', pk=buy.id)
        elif orders:
            print('----1----')
            buy = form2.save(commit=False)
            try:
                c = buy.Customer
                b = buy.Barista
            except:
                print('error!1')
                error = 'Add Customer or/and Barista!'
                context['error'] = error
                return render(request, 'coffeshop/create_buy_order.html', context)
            buy.id = buy.Check = pk
            cost = 0
            for order in orders:
                cost += Product.objects.get(id=order.Product.id).Price*order.Count
            buy.Cost = cost
            # print('-------------')
            # print(buy)
            # print('-------------')
            # print(buying)
            buy.save()
            return redirect('create-buy-customer', pk=buy.id)
        elif not orders:
            print('----3----')
            error = 'Add product!'
            context['error'] = error
            context['form2'] = form2
            return render(request, 'coffeshop/create_buy_order.html', context)
        else:
            print('----4----')
            return render(request, 'coffeshop/create_buy_order.html', context)
    return render(request, 'coffeshop/create_buy_order.html', context)


def create_buy_customer(request, pk):
    buy = get_object_or_404(Buying, id=pk)
    orders = Order.objects.filter(Buying=buy)
    form2 = BuyingForm(request.POST or None)
    context = {
        'form2': form2,
        'buy': buy,
        'orders': orders,
    }
    if request.method == 'POST':
        if form2.is_valid():
            print('--1--')
            print(buy)
            b = form2.save(commit=False)
            try:
                c = b.Customer
            except:
                print('error!1')
                error = 'Add Customer!'
                context['error'] = error
                return render(request, 'coffeshop/create_buy_customer.html', context)
            print(b)
            print(b.Customer)
            buy.Customer = b.Customer
            c = cost = 0
            for order in orders:
                cost += Product.objects.get(id=order.Product.id).Price*order.Count
                c += 1*order.Count
            p = Profile.objects.get(id=buy.Customer.id)
            p.score += c
            p.save()
            print(buy)
            print(buy.id)
            buy.save()
            return redirect('detail-buying', pk=buy.id)
        else:
            print('--2--')
            error = 'err!'
            context['error'] = error
            return render(request, 'coffeshop/create_buy_customer.html', context)
    return render(request, 'coffeshop/create_buy_customer.html', context)


def detail_buying(request, pk):  # detail buying, ready for paying
    buy = get_object_or_404(Buying, id=pk)    
    orders = Order.objects.filter(Buying=buy.id) 
    context = { 
        'buy': buy,
        'orders': orders,    
    }
    if request.method == 'POST':
        if not buy.Paid:
            buy.Paid = True
            buy.save()
            mes = 'Заказ оплачен!'
            context['mes'] = mes
            return render(request, 'coffeshop/partials/buying_detail.html', context)
        else:
            
            return redirect('create-buying')
    return render(request, 'coffeshop/partials/buying_detail.html', context)


def update_order(request, pk): # updage order, can change product and count
    order = Order.objects.get(id=pk)
    form = OrderForm(request.POST or None, instance=order)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('detail-order', pk=order.id)
    context = {
        'form': form,
        'order': order,
    }
    return render(request, 'coffeshop/partials/order_form.html', context)


def detail_order(request, pk):  # detail order,  display one order
    order = get_object_or_404(Order, id=pk)
    context = { 'order': order}
    return render(request, 'coffeshop/partials/order_detail.html', context)


def delete_order(request, pk):
    order = get_object_or_404(Order, id=pk)
    if request.method == 'POST':
        order.delete()
        return HttpResponse('')
    return HttpResponseNotAllowed(['POST'])


def create_order_form(request):  # form for create order
    form = OrderForm()
    context = {
        'form': form,
    }
    return render(request, 'coffeshop/partials/order_form.html', context)
    

def get_customer(request):
    pk = request.GET.get('cus')
    cus = get_object_or_404(Profile, id=pk)
    context = {
        'cus': cus,
    }
    return render(request, 'coffeshop/partials/get_customer.html', context)
