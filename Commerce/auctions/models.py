from django.contrib.auth.models import AbstractUser
from django.db import models
    
# Listings model
class Listings(models.Model):
    choices = [(None, "Choose Category"), ("Toys", "Toys"), ("Electronics", "Electronics"), ("Fashion", "Fashion"), ("Home", "Home"), ("Arts and Crafts", "Arts and Crafts"), ("Books", "Books"), ("Vehicles", "Vehicles")] # change choose category to no category ... add more categories...
    title = models.CharField(max_length = 64)
    description = models.TextField()
    starting_bid = models.IntegerField()
    image = models.URLField(blank=True)
    category = models.CharField(max_length = 64, default = None, choices = choices)
    time_created = models.DateTimeField(auto_now_add = True)
    active = models.BooleanField(default = True)
    
    def __str__(self):
        return f"{self.title.capitalize()} (Starting Bid: {self.starting_bid})"
    
    class Meta: 
        verbose_name_plural = 'Listings'

# Users model
class User(AbstractUser):
    watchlist = models.ManyToManyField(Listings, blank=True, related_name="wishlist_users", default = None)
    
    class Meta: 
        verbose_name_plural = 'Users'
        
# Model that tells the owner of each listing       
class ListingOwners(models.Model):
    listing = models.ForeignKey(Listings, on_delete = models.CASCADE, related_name = "owner")
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "listings")
    
    class Meta: 
        verbose_name_plural = 'ListingOwners'
    
# Bids model  
class Bids(models.Model):
    amount = models.IntegerField()
    listing = models.ForeignKey(Listings, on_delete=models.CASCADE, related_name="bids")
    bidders = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids_made")
    
    class Meta: 
        verbose_name_plural = 'Bids'
        
    def __str__(self):
        return f"${self.amount} Bid on {self.listing} by {self.bidders}"
    
# Comments model   
class Comments(models.Model):
    comment = models.TextField()
    listing = models.ForeignKey(Listings, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    
    class Meta: 
        verbose_name_plural = 'Comments'
