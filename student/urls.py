from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
# from .views import RegistrationView

from . import views
from rest_framework.schemas import get_schema_view
schema_view = get_schema_view(title='Pastebin API')

router = DefaultRouter()
#router.register(prefix='list', viewset=RegistrationView, base_name='Registration')
router.register(r'student', views.StudentViewSet)
router.register(r'exam', views.ExamViewSet)
router.register(r'grade', views.GradeViewSet)
router.register(r'payment', views.PaymentViewSet)

urlpatterns = [
    url(r'^schema/$', schema_view),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]