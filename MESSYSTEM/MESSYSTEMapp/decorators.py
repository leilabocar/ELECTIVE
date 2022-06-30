from django.http import HttpResponse
from django.shortcuts import redirect, render

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        
        if request.user.is_authenticated and request.user.userType == 'Admin':
            return redirect('Admin_Homepage')
        elif request.user.is_authenticated and request.user.userType == 'Student':
            return redirect('Student_History_Transaction')
        elif request.user.is_authenticated and request.user.userType == 'Adviser':
            return redirect('Distribution_and_Retrieval')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func