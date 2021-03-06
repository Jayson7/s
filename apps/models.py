from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
import cloudinary
from cloudinary.models import CloudinaryField


class Categories(models.Model):
    Choices = {
        ("food", "food"),
        ("clothes", "clothes"),
        ("shoes", "shoes"),
    }
    category = models.CharField(choices=Choices, default="selcect a category", max_length=40)

    # stringify output
    def __str__(self):
        return self.category
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Category"
        


# products
class Product(models.Model):
    name = models.CharField(max_length=400)
    main_price = models.PositiveIntegerField()
    discounted_price = models.PositiveIntegerField()
    view_count = models.PositiveIntegerField(default=0)
    file = CloudinaryField('image')
    
    # stringify output
    def __str__(self):
        return self.name

# cart item
class CartItem(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE ) 
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product")
    amount = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True) 
    quantity = models.PositiveBigIntegerField(default=1)
   
    
    
    # stringify output
    def __str__(self):
       
        return str(self.product)
    
    # grand total
class GrandTotal(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE ) 
    total = models.PositiveIntegerField(default=0)
    
    def __str__(self):
           
        return str(self.total)
     
   


    
    # contact model 
class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=11)
    email = models.EmailField()
    message = models.TextField()
    
    def __str__(self):
           
        return str(self.first_name)

countries_available = [
    ("Nigeria", "Nigeria"),
    ("Sudan", "Sudan"),
    ("Congo", "Congo"),
    ("Senegal", "Senegal"),
    ("Algeria", "Algeria"),
    ("Madascar", "Madascar"),
    ("Gambia", "Gambia"),
    ("Kenya", "Kenya"),
    ("Benin Republic", "Benin Republic"),
    ("Togo", "Togo"),
    
]
class CustomerProfile(models.Model):
    
    
    delivery_phone_number = models.IntegerField()
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_image = CloudinaryField('image')
    date_joined = models.DateField(auto_now_add=True)
    
    address = models.CharField(max_length = 500)
    closest_landmark = models.CharField(max_length=300)
    country = models.CharField(choices=countries_available, max_length=100)    
    postal_code = models.PositiveIntegerField()
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    
    def __str__(self):
           
        return str(self.first_name)
         
    
     
