from rest_framework.routers import DefaultRouter
from .views import AccountViewSet

router = DefaultRouter()
router.register(prefix='list', viewset=AccountViewSet, base_name='Accounts')



