from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from rest_framework.views import APIView
from .models import User
from .serializer import UserSerializer
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class UserList(APIView):
    
    def get(self, request):
        user = User.objects.all()

        serializer = UserSerializer(user, many=True)
        
        return JsonResponse({
            'error': False,
            'data': serializer.data,
        })

    def post(self, request):
        
        payload = request.data

        serializer = UserSerializer(data={
            'name': payload['name'],
            'username': payload['username'],
            'password': make_password(password=payload['password']),
        })
        
        if serializer.is_valid():
            serializer.save()
            
            return JsonResponse({
                'error': False,
                'data': serializer.data,
                'message': "User save successfully"
            })
        else:
            return JsonResponse({
                'error': True,
                'data': None,
                'message': serializer.errors
            })
            