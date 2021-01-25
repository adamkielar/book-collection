from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register('books', views.BookViewSet)

app_name = 'book'

urlpatterns = router.urls
