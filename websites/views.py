
from email.mime import application
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from .serializers import WebsiteSerializer
from rest_framework import status
from .logic import websites_logic as wl
from users.logic import users_logic as ul
from django.db import transaction
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

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
        try:
            auth = request.META.get("HTTP_AUTHORIZATION")
            if not auth:
                return JsonResponse({"ERROR": "User must be authenticated"}, status=status.HTTP_401_UNAUTHORIZED)
            else:
                auth = auth.split(" ")[1]
                ul.get_user_by_token(auth)
                request.data["url"] = "https://" + request.data["url"]
                request.data["categoria"] = "NOT RATED"
                request.data["gradoVeracidadPromedio"] = 0.0
                request.data["calificacionPromedio"] = 0.0
                request.data["autor"] = None
                request.data["fecha"] = None
                request.data["disenoPromedio"] = 0.0
                request.data["usabilidadPromedio"] = 0.0
                website_serializer = WebsiteSerializer(data=request.data)
                if website_serializer.is_valid():
                    website_serializer.save()
                    return JsonResponse(website_serializer.data, status=status.HTTP_201_CREATED)
                return JsonResponse(website_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except (Token.DoesNotExist, User.DoesNotExist):
            return JsonResponse({"ERROR": "Token bad request"}, status=status.HTTP_400_BAD_REQUEST)       
    
    return JsonResponse(website_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def multiple_website_view(request):
    if request.method == "GET":
        request_urls = request.GET.getlist('url')
        if not request_urls:
            return JsonResponse({"error": "Missing url or incorrect format on request parameters"}, status=status.HTTP_400_BAD_REQUEST)
        websites = wl.get_multiple_websites_by_urls(request_urls)
        websites_serializer = WebsiteSerializer(websites, many=True)
        return JsonResponse(websites_serializer.data, safe=False)