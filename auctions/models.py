from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Auction(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=1024)
    starting_bid = models.IntegerField()
    img_url = models.CharField(max_length=1024)
    #owner = models.ForeignKey('User')

class Bids(models.Model):
    #title = models.ForeignKey("Auction", on_delete=models.CASCADE)
    #starting_bid = models.ForeignKey("Auction.starting_bid", on_delete=models.CASCADE)
    current_bid = models.IntegerField()
    #bidder = models.ForeignKey(User, on_delete=models.CASCADE)

class Comments(models.Model):
    #author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=1024)
    #auction = models.ForeignKey()