from rest_framework import routers
from django.urls import path, include

from config.yasg import urlpatterns as swagger
from .views import ClientViewSet, MailingListViewSet, MessageViewSet, OperatorCodeViewSet

router = routers.SimpleRouter()
router.register(r'clients', ClientViewSet)
router.register(r'mailings', MailingListViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'codes', OperatorCodeViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]

urlpatterns += swagger
