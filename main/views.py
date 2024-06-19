from django.http import HttpResponse
from django.shortcuts import render
from django.template import context
from django.urls import path

from goods.models import Categories

def index(request) :

    context = {
        "title": "Euggen-Shop",
        "content": "Магазин одягу EUGGEN",
        
        
        }

    return render(request, "main/index.html", context)


    



def about(request):

    context = {
        "title": "Euggen-Shop Про нас",
        "content": "Про нас",
        "text_on_page": "Дуже класний у нас інтернет магазин!....",
    }

    return render(request, "main/about.html", context)
