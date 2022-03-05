from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from coding_challenge.users.api.views import UserViewSet
from coding_challenge.ship_manager.api.views import ShipViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("ships", ShipViewSet)

app_name = "api"
urlpatterns = router.urls
