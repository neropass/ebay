from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Auction(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=1024)
    starting_bid = models.IntegerField()
    img_url = models.URLField(max_length=1024)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Bids(models.Model):
    title = models.ForeignKey(Auction, on_delete=models.CASCADE)
    starting_bid = models.ForeignKey(Auction, on_delete=models.CASCADE)
    current_bid = models.IntegerField()
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)

class Comments(models.Model):
    bid_id = models.ForeignKey(Bids, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=1024)