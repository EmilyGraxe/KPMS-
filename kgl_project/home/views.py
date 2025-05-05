
from django.shortcuts import render, redirect  # Import render and redirect for rendering templates and redirecting users
from django.contrib.auth import authenticate, login, logout # Import authenticate and login for user authentication
from django.contrib.auth.decorators import login_required , permission_required # Import login_required decorator for protecting views
from django.contrib.auth.mixins import LoginRequiredMixin  # Import LoginRequiredMixin for class-based views
from django.views import View  # Import View for class-based views
from django.contrib.auth.models import User  # Import User model for user authentication
from django.contrib.auth import get_user_model  # Import get_user_model for getting the custom user model
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TrustedCustomerForm
from .models import CustomUser, TrustedCustomer 


# Step 1: Show User ID page
@login_required
def enter_user_id(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        try:
            user = CustomUser.objects.get(user_id=user_id)
            request.session['user_id'] = user.user_id  # Store for PIN step
            return redirect('enter_passcode')
        except CustomUser.DoesNotExist:
            messages.error(request, "Invalid User ID")
    return render(request, 'registration/login.html')

# Step 2: Show PIN entry page
def enter_passcode(request):
    
    # if not user_id:
    #     return redirect('enter_user_id')  # safety check
   
    if request.method == 'POST':
        password = request.POST.get('password')  # Get password from the request
        user_id = request.session.get('user_id')  # Get user_id from session
       
        if user_id:
            user = authenticate(request, user_id=user_id, password=password)  # Authenticate user with user_id and password
            if user is not None:
                login(request, user)  # Log in the user
                if user.role == 'manager':  # Check if the user is a manager
                    return redirect('homepage')  # Redirect to manager dashboard
                elif user.role == 'attendant':  # Check if the user is an attendant
                    return redirect('homepage')
                elif user.role == 'director':  # Check if the user is a director
                    return redirect('homepage')
            else:
                messages.error(request, "Invalid credentials")  # Show error message for invalid credentials
        else:
            messages.error(request, "Session expired. Please enter your User ID again.")  # Show error message for expired session
    # if not user_id:
        return redirect('enter_user_id')  # Redirect to User ID entry page if user_id is not found in session
    return render(request, 'registration/pin.html') # Render the Password entry template


@permission_required('home.add_TrustedCustomer',raise_exception=True)
def registerTrustedCustomer(request):

    if request.method == 'POST':
        form = TrustedCustomerForm(request.POST)
        if form.is_valid():
            trustedCustomer = form.save(commit=False)
            trustedCustomer.created_by = request.user
            trustedCustomer.save()
            return redirect('trusted_customer_list')
    else:
        form = TrustedCustomerForm()
    return render(request, 'registration/TrustedCustomer.html',{'form': form})

def trustedCustomer_list(request):
    customers = TrustedCustomer.objects.all().order_by('-created_at')
    return render(request, 'trustedCustomer_list.html', {'customers': customers})

def logout_view(request):
    logout(request)
    return redirect('enter_user_id')


@login_required
def homepage(request):
    return render(request, 'layout.html')

