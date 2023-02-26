from django.urls import path
from . import views

urlpatterns = [
	path('', views.testdata, name="test"),
	path('controldevices/', views.devices, name="devices"),
	path('api/', views.apiOverview, name="api"),

	path('data-list/', views.dataList, name="lst"),
	path('data-detail/<str:id>/', views.dataDetail, name="det"),
	path('data-create/', views.dataCreate, name="create"),
	path('lights-data/', views.lightdata, name="light"),
	path('lights-update/', views.lightUpdate, name="lighjt"),

]
