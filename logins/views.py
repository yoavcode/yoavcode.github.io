from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('home:index'))  # Redirect to a 'success' or another appropriate page
    else:
        form = UserCreationForm()
    return render(request, 'logins/login.html', {'form': form})
