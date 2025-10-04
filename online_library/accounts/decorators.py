from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def admin_required(view_func):
    """
    Decorator to require admin role for accessing a view
    """
    @wraps(view_func)
    @login_required
    def _wrapped_view(request, *args, **kwargs):
        if hasattr(request.user, 'profile') and request.user.profile.is_admin():
            return view_func(request, *args, **kwargs)
        else:
            messages.error(request, "You don't have permission to access this page. Admin access required.")
            return redirect('book-list')
    return _wrapped_view

def user_or_admin_required(view_func):
    """
    Decorator to require user or admin role for accessing a view
    """
    @wraps(view_func)
    @login_required
    def _wrapped_view(request, *args, **kwargs):
        if hasattr(request.user, 'profile'):
            return view_func(request, *args, **kwargs)
        else:
            messages.error(request, "Please complete your profile setup.")
            return redirect('book-list')
    return _wrapped_view