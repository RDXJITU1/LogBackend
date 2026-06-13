from django.shortcuts import render

from django.http import JsonResponse
import json

def register(request):
    if request.method == "POST":
        data = json.loads(request.body)

        userName = data.get("userName")
        password = data.get("password")

        # yahan database insert karo

        return JsonResponse({
            "msg": "success",
            "userName": userName
        })

    return JsonResponse({"error": "Invalid request"})
