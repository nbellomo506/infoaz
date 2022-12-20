# Create your views here.
import requests
import json


from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from django.contrib.auth import authenticate
from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view
from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.viewsets import ModelViewSet
from django.db.models import Q
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.sessions.models import Session
from .serializers import RegisterUserSerializer, UserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from .serializers import ChangePasswordSerializer

from .models import Azienda
from .serializers import AziendaSerializer

from .models import User
from .serializers import UserSerializer

from .models import DatiComune
from .serializers import DatiComuneSerializer

from .models import CostoSmaltimento
from .serializers import CostoSmaltimentoSerializer

import xlwt

class RegisterUserView(CreateAPIView):
    queryset = get_user_model().objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterUserSerializer

#@api_view(['POST'])
def export_aziende(request):

    print(request.FILES)
    print(request.POST)

    return HttpResponse("message")

#@api_view(['POST'])
def login(request):

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    email = body['email']
    password = body['password']

    #request.session.flush()

    user = authenticate(email=email, password=password)
    print(request.user.is_authenticated)

    if user is not None:
        print(email)
        print(password)
        message="SI"
        #login(request,user)
        user = get_user_model().objects.filter(email=email).first()

        if 'azienda' in request.session is not None:
            print(request.session['azienda'])

        request.session['azienda'] = user.azienda.id
        request.session.modified = True
    else:
        message="NO"
    return HttpResponse(message)


class CurrentLoggedInUser(ModelViewSet):
    queryset = get_user_model().objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        user_profile = self.queryset.get(email=request.user.email)

        serializer = self.get_serializer(user_profile)
        return Response({'user': serializer.data})


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.order_by('id')

class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AziendaViewSet(viewsets.ModelViewSet):
    serializer_class = AziendaSerializer
    queryset = Azienda.objects.order_by('id')


class DatiComuneViewSet(viewsets.ModelViewSet):
    serializer_class = DatiComuneSerializer
    queryset = DatiComune.objects.all()


class CostoSmaltimentoViewSet(viewsets.ModelViewSet):
    serializer_class = CostoSmaltimentoSerializer
    queryset = CostoSmaltimento.objects.all()

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['daticomune']
