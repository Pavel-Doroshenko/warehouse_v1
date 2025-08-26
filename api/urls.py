from rest_framework.routers import DefaultRouter

from api.views import UserModelViewSet, WarehouseModelViewSet, ProductModelViewSet, CategoryModelViewSet, \
    BasketModelViewSet

router = DefaultRouter()
router.register('users', UserModelViewSet)
router.register('warehouse', WarehouseModelViewSet)
router.register('product', ProductModelViewSet)
router.register('category', CategoryModelViewSet)
router.register('basket', BasketModelViewSet)



urlpatterns = [

]

urlpatterns.extend(router.urls)