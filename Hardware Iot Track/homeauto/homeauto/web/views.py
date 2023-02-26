
from django.shortcuts import render
from django.http import JsonResponse

from .models import data,lights
from django.views.decorators.cache import never_cache

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DataSerializer,Lightserializer
@never_cache


def testdata(request):
    return render( request,'dashboard.html')

def devices(request):
    return render( request,'devices.html')













@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/data-list/',
		'Detail View':'/data-detail/<str:pk>/',
		'Create':'/data-create/',
		'Update':'/data-update/<str:pk>/',
		'Delete':'/data-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def dataList(request):
	datas = data.objects.all().order_by('-id')
	serializer = DataSerializer(datas, many=True)
	return Response(serializer.data)



@api_view(['GET'])
def dataDetail(request, id):
	datas =data.objects.get(id=id)
	serializer = DataSerializer(datas, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def dataCreate(request):
	serializer = DataSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def dataUpdate(request, id):
	data = data.objects.get(id=id)
	serializer = DataSerializer(instance=data, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def dataDelete(request, pk):
	data = data.objects.get(id=pk)
	data.delete()

	return Response('Item succsesfully delete!')

@api_view(['GET'])
def lightdata(request):
	datas = lights.objects.filter().latest('id')
	serializer =Lightserializer(datas, many=False)

	return Response(serializer.data)

@api_view(['POST'])
def lightUpdate(request):
	serializer = Lightserializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)



