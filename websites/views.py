from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 
from .serializers import WebsiteSerializer
from rest_framework import status
from .logic import websites_logic as wl
# Create your views here.


@csrf_exempt
@api_view(['GET', 'POST', 'PUT'])
def multiple_website_view(request):
    if request.method == "GET":
        websites = wl.get_websites()
        website_serializer = WebsiteSerializer(websites, many=True)
        return JsonResponse(website_serializer.data, safe=False)
    elif request.method == "POST":
        website_dto = JSONParser().parse(request)
        website_serializer = WebsiteSerializer(data=website_dto)
        if website_serializer.is_valid():
            website_serializer.save()
            return JsonResponse(website_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(website_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(["PUT", "DELETE", "GET"])
def single_website_view(request, pk):
    if request.method == "GET":
        website = wl.get_websites_by_name(pk)
        website_serializer = WebsiteSerializer(website, many=True)
        return JsonResponse(website_serializer.data, safe=False)
    return JsonResponse(website_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    """
    if request.method == "PUT":
        website_dto = JSONParser().parse(request)
        website = wl.get_website(pk)
        website_serializer = WebsiteSerializer(website, data=website_dto)
        if website_serializer.is_valid():
            website_serializer.save()
            return JsonResponse(website_serializer.data)
        return JsonResponse(website_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        """