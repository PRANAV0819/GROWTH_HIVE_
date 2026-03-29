from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Item


@login_required
def item_list(request):
    items = Item.objects.all().order_by('-created_at')
    return render(request, 'lostfound/item_list.html', {'items': items})


@login_required
def report_item(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        status = request.POST['status']

        Item.objects.create(
            title=title,
            description=description,
            status=status,
            reported_by=request.user
        )

        return redirect('lostfound_list')

    return render(request, 'lostfound/report_item.html')