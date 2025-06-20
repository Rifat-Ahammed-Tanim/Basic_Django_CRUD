from django.shortcuts import render, redirect
from .models import *
# CRUD (Create, Read, Update, Delete) operations in Django

# Create view function
def create(request):
    if request.method == 'POST':

        data = CrudModel(
        name = request.POST.get('name'),
        image = request.FILES.get('image'),
        )
        data.save()
        return redirect('read')
    return render(request, 'create.html')


# Read view function
def read(request):
    data = CrudModel.objects.all()
    context = {
        'data': data
    }
    return render(request, 'read.html', context)


# Update view function
def update(request, id):
    data = CrudModel.objects.get(id=id)
    if request.method == 'POST':
        data.name = request.POST.get('name')
        if request.FILES.get('image'):          # Check if a new image is uploaded
            data.image = request.FILES.get('image')
        data.save()
        return redirect('read')
    context = {
        'data': data
    }
    return render(request, 'update.html', context)

# Delete view function
def delete(request, id):
    CrudModel.objects.get(id=id).delete()
    return redirect('read')
