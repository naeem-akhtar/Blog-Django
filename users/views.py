from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm

# registeration
def register(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			# print(form.cleaned_data)
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}! You can now log in.')
			return redirect('login')
	else:
		form = UserRegistrationForm()
	return render(request, 'users/register.html', {'form':form})

# Whenever user try to acess profile he/she must be logined
@login_required
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(
			request.POST, 
			instance=request.user
		)
		p_form = ProfileUpdateForm(
			request.POST, 
			request.FILES, 
			instance=request.user.profile
		)
		if u_form.is_valid and p_form.is_valid:
			u_form.save()
			p_form.save()
			messages.success(request, f'Account updated for {request.user.username}!')
			return redirect('profile')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)
	context = {
		'u_form': u_form,
		'p_form': p_form
	}
	return render(request, 'users/profile.html', context)
	
