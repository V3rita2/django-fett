from rest_framework import routers
from .api import TrackViewset


router = routers.DefaultRouter()
router.register('api/tracks', TrackViewset, 'tracks')

urlpatterns = router.urls