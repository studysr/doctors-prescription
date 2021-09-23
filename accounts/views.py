from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect


def signup(request):
	if request.method == 'POST':
		if request.POST['password1'] == request.POST['password2']:
			try:
				user = User.objects.get(username=request.POST['username'])
				return render(request, 'accounts/signup.html', {'error':'Username has already been taken.'})
			except User.DoesNotExist:
				user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
				auth.login(request,user)
				return redirect('create')
		else: 
			return render(request, 'accounts/signup.html', {'error':'password much match.'})
	else:
		return render(request, 'accounts/signup.html')


def login(request):
	if request.method == 'POST':
		user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
		if user is not None:
			auth.login(request, user)
			return redirect('create')
		else:
		 return render(request, 'accounts/login.html', {'error':'username or password is incorrect.'})
	else:
		return render(request, 'accounts/login.html')




from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return render(request, 'accounts/logout.html')
    


def login_popup(request):
	if request.method == 'POST':
		user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
		if user is not None:
			auth.login(request, user)
			return redirect('create')
		else:
		 return render(request, 'prescription/pop_login.html', {'error':'username or password is incorrect.'})
	else:
		return render(request, 'prescription/pop_login.html')
