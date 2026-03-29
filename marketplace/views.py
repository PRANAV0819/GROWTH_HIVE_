from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Item


@login_required
def item_list(request):
    items = Item.objects.all()
    return render(request, 'marketplace/item_list.html', {'items': items})


@login_required
def create_item(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        price = request.POST['price']

        Item.objects.create(
            title=title,
            description=description,
            price=price,
            seller=request.user
        )

        return redirect('item_list')

    return render(request, 'marketplace/create_item.html')