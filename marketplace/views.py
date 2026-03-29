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
        # 1. Extract standard text data from request.POST
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        
        # 2.  Extract the uploaded file from request.FILES
        # Note: 'image' matches the name="image" attribute in your HTML form
        image = request.FILES.get('image') 

        # 3. Basic validation to ensure required fields aren't empty
        if title and description and price:
            # 4. Create and save the item to the database
            Item.objects.create(
                seller=request.user,
                title=title,
                description=description,
                price=price,
                image=image
            )
            # 5. Redirect back to the marketplace list after successful post
            return redirect('item_list') # Replace 'marketplace' with your actual URL name for the list view
        return render(request, 'marketplace/create_item.html')
