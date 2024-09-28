from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Profile Model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ROLE_CHOICES = [
        ('farmer', 'Farmer'),
        ('buyer', 'Buyer'),
    ]
    role = models.CharField(max_length=6, choices=ROLE_CHOICES)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    preferred_products = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    id_number = models.CharField(max_length=50, blank=True, null=True)  # Added field
    farm_products = models.TextField(blank=True, null=True)  # Added field
    farm_size = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Added field
    def __str__(self):
        return self.user.username

# Signal to create a Profile instance when a User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # Create a Profile instance for the new user
        Profile.objects.create(user=instance)

# Signal to save the Profile instance when the User is saved
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    # Save the associated Profile instance whenever the User is saved
    instance.profile.save()

# Farmer Model
class Farmer(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    contact_info = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)
    
   
    def __str__(self):
        return f"{self.profile.user.username} - {self.location}"
    
 
class Buyer(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    preferred_products = models.TextField()

    def __str__(self):
        return self.profile.user.username

# Product Model
class Product(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    available_quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    
    
    
    print(Farmer.objects.all())