
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 
from .serializers import WebsiteSerializer
from rest_framework import status
from .logic import websites_logic as wl
from django.db import transaction

@transaction.non_atomic_requests
@api_view(["GET", "POST"])
def single_website_view(request):
    if request.method == "GET":
        request_url= request.GET.get("url")
        if not request_url:
            return JsonResponse({"error": "Missing url or incorrect format on request parameters"}, status=status.HTTP_400_BAD_REQUEST)
        website = wl.get_website_by_url(request_url)
        if not website:
            return JsonResponse({"error": "Website does not exist"}, status=status.HTTP_404_NOT_FOUND)
        website_serializer = WebsiteSerializer(website)
        return JsonResponse(website_serializer.data, safe=False)
    elif request.method == "POST":
        request.data["categoria"] = "NO CALIFICADO"
        website_dto = JSONParser().parse(request)
        website_serializer = WebsiteSerializer(data=website_dto)
        if website_serializer.is_valid():
            website_serializer.save()
            return JsonResponse(website_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(website_serializer.errors, status=status.HTTP_400_BAD_REQUEST)        
    
    return JsonResponse(website_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
