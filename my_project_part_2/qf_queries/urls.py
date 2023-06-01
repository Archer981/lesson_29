# TODO здесь необходимо настроить urls приложения
from rest_framework import routers

from qf_queries.views import StoreView

router = routers.SimpleRouter()
router.register('qf_queries', StoreView)

urlpatterns = [

]
urlpatterns += router.urls
