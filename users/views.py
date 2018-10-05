from django.shortcuts import render, redirect
from django.contrib import messages
from .form import UserRegisterForm

def register(request):
	if request.method == 'POST':  #check if the request is post
		form = UserRegisterForm(request.POST) #if it is post then create new form
		if form.is_valid():  #check if the form is valid
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, 'Account creater for {}!'.format(username))
			return redirect('blog-home')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form': form})
