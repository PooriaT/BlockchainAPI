from django.db import models
from datetime import datetime

# Information related to users
class SearchAddressHistory(models.Model):
    user = models.CharField(max_length=60)
    coin = models.CharField(max_length=3)
    address = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    request_status = models.CharField(max_length=10)
    date_search = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.user

class SearchTransactionHistory(models.Model):
    user = models.CharField(max_length=60)
    coin = models.CharField(max_length=3)
    hash = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    request_status = models.CharField(max_length=10)
    date_search = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.user
