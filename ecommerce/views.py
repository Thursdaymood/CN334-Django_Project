from django.shortcuts import render
from django.http import HttpResponse



def ecommerce_index_view(request):
    # index page
    student = ["6410742511", "Sasipa", "Boon-umchu"]
    
    return HttpResponse(f"Welcome to {student[0]} {student[1]} {student[2]} views!")


def item_view(request, item_id):
    context_data = {
        "item_id": item_id
    }
    return render(request, 'index', context = context_data)

# HW3 
# homepage
def homepage_view(request):
    data = {}
    return render(request, 'homepage.html', context = data)

# contacts
def contacts_view(request):
    data = {}
    return render(request, 'contacts.html', context = data)

# checkout
def checkout_view(request):
    data = {}
    return render(request, 'checkout.html', context = data)

# products
def products_view(request):
    data = {}
    return render(request, 'products.html', context = data)

#categories
def categories_view(request):
    data = {}
    return render(request, 'categories.html', context = data)