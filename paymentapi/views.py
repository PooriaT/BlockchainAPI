from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer, AddressSerializer, TransactionSerializer, AddressHistorySerializer, TransactionHistorySerializer
from .models import SearchAddressHistory, SearchTransactionHistory
from django.http import HttpResponseRedirect
import requests


#Registering UserViewSet
class RegisterView(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    #queryset = User.objects.all().order_by('username')
    serializer_class = RegisterSerializer
    http_method_names = ['post']
    def post(self, request, format=None):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Address info view
class AddressInfoView(APIView):
    """
    API endpoint that shows all the transactions related to the specific address.
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AddressSerializer

    http_method_names = ['post']

    def post(self, request, format=None):
        data = request.data.copy()
        data['user'] = request.user.username
        url = "https://api.bitaps.com/" +  str(request.data['coin']) + "/v1/blockchain/" + "address/transactions/" + str(request.data['address'])
        data['url'] = url
        req_stat = requests.get(url).status_code
        if req_stat == 200:
            data['request_status'] = 'Valid'
        else:
            data['request_status'] = 'Invalid'

        serializer = AddressSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            #return HttpResponseRedirect(url)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Transaction info view
class TransactionInfoView(APIView):
    """
    API endpoint that shows the specific transactions
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TransactionSerializer
    http_method_names = ['post']

    def post(self, request, format=None):
        data = request.data.copy()
        data['user'] = request.user.username
        url = "https://api.bitaps.com/" +  str(request.data['coin']) + "/v1/blockchain/" + "transaction/" + str(request.data['hash'])
        data['url'] = url
        req_stat = requests.get(url).status_code
        if req_stat == 200:
            data['request_status'] = 'Valid'
        else:
            data['request_status'] = 'Invalid'

        serializer = TransactionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            #return HttpResponseRedirect(url)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Representing all the history of Address search by the specific user
class AddressHistoryView(APIView):
    """
    API endpoint that shows history of address search.
    """
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get']

    def get(self, request, format=None):
        searchAddHis = SearchAddressHistory.objects.filter(user=request.user.username)
        serializer = AddressHistorySerializer(searchAddHis, many=True)
        return Response(serializer.data)

# Representing all the history of Transaction search by the specific user
class TransactionHistoryView(APIView):
    """
    API endpoint that shows history of address search.
    """
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get']

    def get(self, request, format=None):
        searchTranHis = SearchTransactionHistory.objects.filter(user=request.user.username)
        serializer = TransactionHistorySerializer(searchTranHis, many=True)
        return Response(serializer.data)
