
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 
from .serializers import WebsiteSerializer
from rest_framework import status
from .logic import websites_logic as wl
from .models import Website

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

@api_view(["GET"])
def single_website_view(request, pk):
    if request.method == "GET":
        try:
            url = "http://" + pk
            website = wl.get_website_by_url(url)
            website_serializer = WebsiteSerializer(website)
            return JsonResponse(website_serializer.data, safe=False)
        except Website.DoesNotExist:
            return JsonResponse({"error": "Website does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except KeyError:
            return JsonResponse({"error": "Missing url on request body"}, status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse(website_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
