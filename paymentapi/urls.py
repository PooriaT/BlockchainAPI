from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
#router.register(r'register', views.RegisterView)

# router.get_api_root_view().cls.__name__ = "Root API name"
router.get_api_root_view().cls.__doc__ = """
                                         Register new user: /register/
                                         login: /api-auth/login/
                                         logout: /api-auth/logout/
                                         Submitting new address: /address/
                                         Submitting new transaction: /transaction/
                                         viewing the histroy search of addresses: /address/history/
                                         viewing the histroy search of transactions: /transaction/history/
                                          """


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('address/', views.AddressInfoView.as_view()),
    path('address/history/', views.AddressHistoryView.as_view()),
    path('transaction/', views.TransactionInfoView.as_view()),
    path('transaction/history/', views.TransactionHistoryView.as_view()),
    path('register/', views.RegisterView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
