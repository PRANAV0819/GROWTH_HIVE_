from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Resource


@login_required
def resource_list(request):
    resources = Resource.objects.all()
    return render(request, 'resources/resource_list.html', {'resources': resources})


@login_required
def upload_resource(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        file = request.FILES['file']

        Resource.objects.create(
            title=title,
            description=description,
            file=file,
            uploaded_by=request.user
        )

        return redirect('resource_list')

    return render(request, 'resources/upload_resource.html')
