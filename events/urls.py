from rest_framework.routers import DefaultRouter
from .views import EventViewSet, RSVPViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'rsvp', RSVPViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = router.urls
