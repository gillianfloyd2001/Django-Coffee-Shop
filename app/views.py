from django.shortcuts import render, redirect
from models import Coffee, Transaction
from datetime import datetime

# Create your views here.


def home(request):
    return render(request, "app/coffee_list.html", {"coffees": Coffee.object.all()})


def transaction_detail(request, id):
    return render(
        request,
        "app/transaction_detail.html",
        {"transaction": Transaction.objects.get(id=id)},
    )


def buy_coffee(request, id):
    if request.method == "POST":
        coffee = Coffee.objects.get(id=id)
        transaction = coffee.transaction_set.create(
            time=datetime.now(), pre_tax=coffee.price, tax=coffee.price * 0.07
        )
        return redirect("transaction_detail", transaction_id)

