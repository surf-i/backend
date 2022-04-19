from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from .serializers import ReviewSerializer
from .logic import users_logic as ul
from websites.logic import websites_logic as wl

#TODO: Test
@api_view(["POST"])
def add_review_view(request):
    if request.method == "GET":
        website = wl.get_websites_by_url(request.POST["url"])
        user = ul.get_user_by_email(request.POST["user_email"])
        print(request)
        print(request.POST)
        print(website)
        print(user)
        #request.POST["website"] = website.id
        #request.POST["user"] = user.id
        request_dto = JSONParser().parse(request.POST["review"])
        request_serializer = ReviewSerializer(data=request_dto, context={"website": website, "user": user})
        