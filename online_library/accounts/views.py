from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f"Welcome {user.username}! Your account has been created with 'User' role. You can now browse books and write reviews.")
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

@login_required
def custom_logout(request):
    """
    Custom logout view that handles POST requests and provides user feedback
    """
    if request.method == 'POST':
        username = request.user.username
        logout(request)
        messages.success(request, f"Goodbye {username}! You have been successfully logged out.")
        return redirect('/')
    else:
        # If accessed via GET, redirect to home page
        return redirect('/')
