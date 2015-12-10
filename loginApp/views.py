from django.shortcuts import render

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from .models import UserPermited

# Create your views here.
   
class ObtainPass(ObtainAuthToken):

    def post(self, request):
        result = None
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        if user:
            permited = bool(UserPermited.objects.filter(username=user.username))
            token, created = Token.objects.get_or_create(user=user)
            result = {
                'user': user.username,
                'name' : user.name,
                'email' : user.email,
                'token' : token.key if token else ''
            }
        else :
            result = {'permited': False}

        return Response(result)
