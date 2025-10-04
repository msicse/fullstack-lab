def user_role_context(request):
    """
    Context processor to add user role information to all templates
    """
    context = {}
    if request.user.is_authenticated and hasattr(request.user, 'profile'):
        context['user_role'] = request.user.profile.role
        context['is_admin'] = request.user.profile.is_admin()
        context['is_user'] = request.user.profile.is_user()
    else:
        context['user_role'] = None
        context['is_admin'] = False
        context['is_user'] = False
    
    return context