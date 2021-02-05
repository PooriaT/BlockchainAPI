from django.contrib import admin
from .models import SearchAddressHistory, SearchTransactionHistory

# Register your models here.
admin.site.register(SearchAddressHistory)
admin.site.register(SearchTransactionHistory)
