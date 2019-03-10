from django.shortcuts import render,redirect

# add generic class views as needed, CRUD
from django.contrib.auth.forms import UserCreationForm # TODO custom form
from django.contrib.auth import logout
# project imports
from .forms import ProfileForm

# Create your views here.
# registration view
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile-update') # TODO useful registration success page
    else:
        form = UserCreationForm()

    args = {'form': form}
    return render(request, 'register.html', args)

# profile views

def profile_update_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST,instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('rooms')

    else:
        form = ProfileForm(instance=request.user)
        args = {'form':form}
        return render(request,'profile_edit.html',args)

def profile_view(request):
    args = dict(user=request.user)
    return render(request,'profile_view.html',args)

def logout_view(request):
    logout(request)
    return redirect('login')
