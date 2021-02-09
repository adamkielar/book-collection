from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register('books', views.BookViewSet)
router.register('list', views.BookView, basename='Book')

app_name = 'book'

urlpatterns = router.urls
