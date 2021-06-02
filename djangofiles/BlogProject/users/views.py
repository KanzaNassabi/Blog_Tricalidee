from django.shortcuts import render, redirect, get_object_or_404
from rolepermissions.roles import assign_role
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from blog.models import Tag
 
def register(request):
    tags = Tag.objects.all()
    if request.method == 'POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            email = form.cleaned_data.get('email')
            type = form.cleaned_data.get('type')
            userProfile =  user.profile
            userProfile.type=type
            userProfile.save()
            if type =="Admin":
                assign_role(user,'admin')
            elif type =="Author":
                assign_role(user,'author')
            else:
                assign_role(user,'registreduser')
            messages.success(request, f'Your account has been created. You are now enable to Log In')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form': form,'tags':tags})

@login_required(login_url='login')
def profile(request):
    myprofile = request.user.profile 
    type = myprofile.type
    tags = Tag.objects.all()
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            newtype = p_form.cleaned_data.get('type')
            image = p_form.cleaned_data.get('image') 
            if newtype.lower() != type.lower():
                myprofile.set_change_role()
                myprofile.type = type
                myprofile.new_type = newtype
                myprofile.image=image
                myprofile.save()
                u_form.save()
                #p_form.save()
                messages.success(request, f'Your account has been updated!')
                messages.info(request, f'Request for new role sent for approbation')

            else :
                u_form.save()
                p_form.save()
                messages.success(request, f'Your account has been updated!')

            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form' : u_form,
        'p_form' : p_form,
        'tags'   : tags
    }
    return render(request, 'users/profile.html', context)
