from django.shortcuts import render, redirect
from django.contrib import messages
from .form import UserRegisterForm

def register(request):
	if request.method == 'POST':  #check if the request is post
		form = UserRegisterForm(request.POST) #if it is post then create new form
		if form.is_valid():  #check if the form is valid
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, 'Your account has been created! You are now able to log in'.format(username))
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form': form})  #in render fild first param always must be request


def profile(request):
	return render(request, 'users/profile.html')