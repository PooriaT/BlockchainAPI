from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import SearchAddressHistory, SearchTransactionHistory


#Registering data
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    username = serializers.CharField(
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(min_length=8, write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],
                                        validated_data['email'],
                                        validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']


#Searching address of BTC, RTH and BCH
class AddressSerializer(serializers.ModelSerializer):
    user = serializers.CharField(help_text="Don't Fill this item")
    coin = serializers.CharField()#.MultipleChoiceField(choices = ("btc", "eth","bch"))
    address = serializers.CharField()
    url = serializers.URLField(help_text="Don't Fill this item")
    request_status = serializers.CharField(help_text="Don't Fill this item")

    def create(self, validated_data):
        return SearchAddressHistory.objects.create(**validated_data)

    class Meta:
        model = SearchAddressHistory
        fields = ['user', 'coin', 'address', 'url', 'request_status']


#Searching Transactions of BTC, RTH and BCH
class TransactionSerializer(serializers.ModelSerializer):
    user = serializers.CharField(help_text="Don't Fill this item")
    coin = serializers.CharField()#MultipleChoiceField(choices = ("btc", "eth","bch"))
    hash = serializers.CharField()
    url = serializers.URLField(help_text="Don't Fill this item")
    request_status = serializers.CharField(help_text="Don't Fill this item")

    def create(self, validated_data):
        return SearchTransactionHistory.objects.create(**validated_data)


    class Meta:
        model = SearchTransactionHistory
        fields = ['user', 'coin', 'hash', 'url', 'request_status']


#Seach histroy of addresses and transactions serializer
class AddressHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchAddressHistory
        fields = ['user', 'coin', 'address', 'url', 'request_status', 'date_search']


class TransactionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchTransactionHistory
        fields = ['user', 'coin', 'hash', 'url', 'request_status', 'date_search']
