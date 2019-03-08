from django.shortcuts import render,redirect

# add generic class views as needed, CRUD
from django.views.generic import (ListView,)

# project imports
from .models import Image
from .forms import  ImageForm

# Create your views here.
def ImageCreateView(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('images') # TODO create an images landing page
    else:
        form = ImageForm()

    args = {'form': form}
    return render(request, 'images/image_form.html', args)

class ImageListView(ListView):
    model = Image
