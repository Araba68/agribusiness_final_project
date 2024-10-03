from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.utils.crypto import get_random_string
from django.contrib.auth.decorators import login_required
from .models import Profile, Farmer, Buyer  # Ensure Buyer is imported if it exists
from .forms import BuyerProfileForm, FarmerProfileForm

def home(request):
    return render(request, 'portal/index.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            profile = Profile.objects.get(user=user)  # Get the profile associated with the user
            
            if profile.role == 'farmer':
                return redirect('farmer_dashboard')  # Redirect farmers to their dashboard
            else:
                return redirect('buyer_dashboard')  # Redirect buyers to their dashboard
        else:
            messages.error(request, "Invalid username or password")
            return redirect('signin')

    return render(request, 'portal/signin.html')

# Buyer Sign Up View
def signup_buyer(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists. Please choose another one.")
            return redirect('signup_buyer')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('signup_buyer')

        if len(password) < 8:
            messages.error(request, "Password must be at least 8 characters long.")
            return redirect('signup_buyer')

        # Create the user
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=fname,
            last_name=lname
        )
        
        # Send activation email
        activation_link = f"http://localhost:8000/activate/{get_random_string(32)}/"
        send_mail(
            'Activate Your Account',
            f'Click this link to activate your account: {activation_link}',
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )

        messages.success(request, "Signup successful! Please check your email to activate your account.")
        return redirect('signin')

    return render(request, 'portal/signup_buyer.html')

# Farmer Sign Up View
def signup_farmer(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists. Please choose another one.")
            return redirect('signup_farmer')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('signup_farmer')

        if len(password) < 8:
            messages.error(request, "Password must be at least 8 characters long.")
            return redirect('signup_farmer')

        # Create the user
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=fname,
            last_name=lname
        )
        
        # Send activation email
        activation_link = f"http://localhost:8000/activate/{get_random_string(32)}/"
        send_mail(
            'Activate Your Account',
            f'Click this link to activate your account: {activation_link}',
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )

        messages.success(request, "Signup successful! Please check your email to activate your account.")
        return redirect('signin')

    return render(request, 'portal/signup_farmer.html')

@login_required
def farmer_dashboard(request):
    profile = Profile.objects.get(user=request.user)
    buyers = Buyer.objects.all()  # Fetch all buyers
    # Fetch transaction data for the chart
    labels = ["January", "February", "March"]  # Example labels
    data = [10, 20, 30]  # Example data points; replace with real data

    return render(request, 'portal/farmer_dashboard.html', {
        'profile': profile,
        'buyers': buyers,
        'labels': labels,
        'data': data,
    })


@login_required
def buyer_dashboard(request):
    profile = Profile.objects.get(user=request.user)
    
    # Fetch the list of farmers (you may need to adjust the queryset)
    farmers = Farmer.objects.all()  # This could be filtered based on your application's logic

   
    # Prepare the data for rendering
    context = {
        'profile': profile,
        'farmers': farmers,
        
        }
   

    return render(request, 'portal/buyer_dashboard.html', context)
@login_required
def update_farmer_profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        profile.farm_size = request.POST['farm_size']
        profile.location = request.POST['location']
        profile.id_number = request.POST['id_number']
        profile.farm_products = request.POST['farm_products']
        profile.save()
        messages.success(request, "Profile updated successfully!")
        return redirect('farmer_dashboard')
    
    return render(request, 'update_profile.html', {'profile': profile})

@login_required
def update_buyer_profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        profile.contact_info = request.POST['contact_info']  # Adjust field names as per your Profile model
        profile.preferred_products = request.POST['preferred_products']  # Adjust accordingly
        profile.location = request.POST['location']
        profile.id_number = request.POST['id_number']
        profile.save()
        messages.success(request, "Profile updated successfully!")
        return redirect('buyer_dashboard')  # Redirect to the buyer dashboard after updating
    
    return render(request, 'update_buyer_profile.html', {'profile': profile})  # Adjust the template name accordingly

def contact_admin(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        send_mail(
            'Farmer Query',
            query,
            'mkulimapp@gmail.com',  # Replace with your email
            ['admin@example.com'],  # Replace with the admin's email
            fail_silently=False,
        )
        messages.success(request, 'Your query has been submitted successfully.')
        return redirect('farmer_dashboard')
    
    return redirect('farmer_dashboard')  # Redirect if accessed via GET

def access_finances(request):
    return render(request, 'portal/access_finances.html')  # Create this template accordingly
