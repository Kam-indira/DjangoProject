from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Users.models import UserDetails
from Users.serializers import UserDetailsSerializer


# Create your views here.

@csrf_exempt
def userdetailsApi(request,id=0):
    if request.method=='GET':
        userdetails = UserDetails.objects.all()
        userdetails_serializer = UserDetailsSerializer(userdetails,many=True)
        return JsonResponse(userdetails_serializer.data,safe=False)

    elif request.method=='POST':
        userdetails_data = JSONParser().parse(request)
        userdetails_serializer = UserDetailsSerializer(data = userdetails_data)
        if userdetails_serializer.is_valid():            
            userdetails_serializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        return JsonResponse("Failed to Add.",safe=False)

    elif request.method=='PUT':
        userdetails_data = JSONParser().parse(request)
        userdetails = UserDetails.objects.get(id=userdetails_data['id'])
        userdetails_serializer = UserDetailsSerializer(userdetails,data=userdetails_data)
        if userdetails_serializer.is_valid():
            userdetails_serializer.save()
            return JsonResponse("Update Successfully!", safe=False)
        return JsonResponse("Failed to Update.",safe=False)
    
    elif request.method=='DELETE':
        userdetails = UserDetails.objects.get(id=id)
        userdetails.delete()
        return JsonResponse('Deleted Successfully!', safe=False)


    