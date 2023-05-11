


from rest_framework.routers import DefaultRouter
from .views import ItemView

router = DefaultRouter()
router.register(r'', ItemView, 'Item')
urlpatterns = router.urls