from rest_framework.routers import SimpleRouter
from unsaTur import views

urlpatterns = []
router = SimpleRouter()

router.register(r'atr', views.AtrViewSet, 'Atr')
router.register(r'list', views.ListViewSet, 'List')
router.register(r'tipatr', views.TipatrViewSet, 'Tipatr')
router.register(r'usucab', views.UsucabViewSet, 'Usucab')
router.register(r'zontur', views.ZonturViewSet, 'Zontur')
router.register(r'zonturlist', views.ZonturListViewSet, 'ZonturList')
router.register(r'zonturcom', views.ZonturcomViewSet, 'Zonturcom')
router.register(r'zonturhor', views.ZonturhorViewSet, 'Zonturhor')



urlpatterns += router.urls