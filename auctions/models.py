from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=1024)
    starting_bid = models.IntegerField()
    img_url = models.URLField(max_length=1024)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_listing')

class Bid(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    current_bid = models.IntegerField()
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bid')

class Comments(models.Model):
    bid = models.ForeignKey(Bid, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(max_length=1024)