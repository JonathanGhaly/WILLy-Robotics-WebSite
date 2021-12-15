from django.http import HttpResponse
from django.shortcuts import redirect
"""
 Decoratores (authenticate)

"""


def unauthenticated_user(view_fun):
    """ check if user is authenticated

        :type view_fun: View functon   

        :param view_fun: render the checked function

        :rtype: function
    """
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('table')
        else:
            return view_fun(request, *args, **kwargs)
    return wrapper_func


def allowed_user(allowed_roles=[]):
    """ Allow sepcific group to access pages

        :type allowed_roles: Group

        :param allowed_roles: the allowed role
    """
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page')
        return wrapper_func
    return decorator
