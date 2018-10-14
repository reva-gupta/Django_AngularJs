from django.conf.urls import include, url
from .views import IndexView
from rest_framework_nested import routers
from authentication.views import AccountViewSet

router = routers.SimpleRouter()
router.register('accounts', AccountViewSet)

urlpatterns = [
    url('api/v1/', include(router.urls)),
    url('', IndexView.as_view(), name='index'),
]
