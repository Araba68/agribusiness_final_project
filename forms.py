from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile  # Make sure to import the Profile model
from django.core.exceptions import ValidationError

class SignInForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

# Buyer Sign Up Form
class BuyerSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("Username already taken. Please choose another.")
        return username

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            Profile.objects.create(user=user, role='buyer')
        return user

# Farmer Sign Up Form
class FarmerSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("Username already taken. Please choose another.")
        return username

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            Profile.objects.create(user=user, role='farmer')
        return user
    
class BuyerProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['contact_number', 'preferred_products', 'location']  # Adjust fields as needed

class FarmerProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['id_number', 'farm_products', 'farm_size', 'contact_number', 'preferred_products', 'location']  # Include all necessary fields