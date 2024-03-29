from django.shortcuts import render,redirect
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm,ScanningForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):#registration page
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account has been created for {username}')
            return redirect('login')
    else:
        form=UserRegisterForm()
    return render(request,'users/registration.html',{'form':form})


def home(request):#homepage
    return render(request,'users/home.html')


@login_required

def profile(request):#profile page
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)

def scan(request):
    if request.method=='POST':
        s_form=ScanningForm(request.POST,request.FILES,instance=request.user.profile)
        if s_form.is_valid:
            s_form.save()
            messages.success(request,f'Your Scanning is complete')
            return redirect('Scanpage')
    else:
        s_form=ScanningForm()

    context={
        's_form':s_form
    }
    return render(request,'users/Scanning.html',context)









