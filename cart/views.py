from django.shortcuts import render


def view_cart(request):
    context = {}
    return render(request, 'view_cart.html', context)