from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from .serializers import ReviewSerializer
from .logic import users_logic as ul
from .logic import metadata_logic as ml
from websites.logic import websites_logic as wl
from django.http.response import JsonResponse
from rest_framework import status
from django.contrib.auth.models import User

@api_view(["POST"])
def add_review_view(request):
    if request.method == "POST":
        auth = request.META.get("HTTP_AUTHORIZATION")
        if not auth:
            return JsonResponse({"ERROR: User must be authenticated"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            auth = auth.split(" ")[1]
            print(auth)
            user = ul.get_user_by_token(auth)
        try:
            website = wl.get_website_by_url(request.data["url"])
            request.data["review"]["website"] = website.id
            request.data["review"]["usuario"] = user.id
            request_serializer = ReviewSerializer(data=request.data["review"], context={"website": website, "user": user})
            if request_serializer.is_valid():
                request_serializer.save()
                ml.update_metadata(request_serializer.validated_data, website)
                return JsonResponse(request.data, status=status.HTTP_201_CREATED)
            return JsonResponse(request_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        except User.DoesNotExist:
            return JsonResponse({"error": "User does not exist"}, status=status.HTTP_400_BAD_REQUEST)