# Create your views here.
import requests
import json
import os

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
from django.core import serializers
from django.conf import settings

from .models import Azienda
from .serializers import AziendaSerializer

from .models import User
from .serializers import UserSerializer

from .models import DatiComune
from .serializers import DatiComuneSerializer

from .models import CostoSmaltimento
from .serializers import CostoSmaltimentoSerializer

from comuni_italiani.models import Comune
import xlwt

basedir = "C:/Users/Nicolas/OneDrive/infowaste-aziende-test/"
#basedir = "C:/Users/Administrator/OneDrive/infowaste-aziende/"


class RegisterUserView(CreateAPIView):
    queryset = get_user_model().objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterUserSerializer


def assign_azienda(request):

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    user = body['user_id']
    azienda = body['azienda_id']

    if 'logged' in request.session is not None:
        if request.session['logged'] == True:
            if request.session['is_admin'] == True and request.session['is_staff'] == True and request.session['is_active'] == True:
                obj = User.objects.get(pk = user)
                obj.azienda_id = azienda
                obj.is_assigned = True
                obj.save()
                return JsonResponse("OK",content_type="application/json",safe=False)
        else:
            return JsonResponse("Not Allowed",content_type="application/json",safe=False)

def savePEF(request):

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    pef = body['pef']
    azienda = body['azienda']

    if 'logged' in request.session is not None:
        if request.session['logged'] == True:
            if request.session['is_admin'] == True and request.session['is_staff'] == True and request.session['is_active'] == True:

                obj = Azienda.objects.get(pk = azienda)
                obj.pef_mis_o_ric = pef
                obj.save()
                return JsonResponse("OK",content_type="application/json",safe=False)
        else:
            return JsonResponse(False,content_type="application/json",safe=False)
    else:
        return JsonResponse(False,content_type="application/json",safe=False)

def add_azienda(request):

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    ragione_sociale = body['ragione_sociale']
    partita_iva = body['partita_iva']
    pef_mis_o_ric = body['pef_mis_o_ric']

    if 'logged' in request.session is not None:
        if request.session['logged'] == True:
            if request.session['is_admin'] == True and request.session['is_staff'] == True and request.session['is_active'] == True:

                os.mkdir(os.path.join(basedir, ragione_sociale))
                obj = Azienda.objects.create(ragione_sociale=ragione_sociale,partita_iva=partita_iva,pef_mis_o_ric=pef_mis_o_ric)
                obj.save()

                return JsonResponse("OK",content_type="application/json",safe=False)
        else:
            return JsonResponse(False,content_type="application/json",safe=False)
    else:
        return JsonResponse(False,content_type="application/json",safe=False)

def del_azienda(request):

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    azienda = body['id']

    if 'logged' in request.session is not None:
        if request.session['logged'] == True:
            if request.session['is_admin'] == True and request.session['is_staff'] == True and request.session['is_active'] == True:

                obj = Azienda.objects.get(pk = azienda).delete()
                return JsonResponse("Azienda eliminata",content_type="application/json",safe=False)
        else:
            return JsonResponse(False,content_type="application/json",safe=False)
    else:
        return JsonResponse(False,content_type="application/json",safe=False)

def add_comune_azienda(request):

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    comune = body['comune']

    if 'logged' in request.session is not None:
        if request.session['logged'] == True:
            if 'user_id' and 'azienda' in request.session is not None:
                try:
                    obj = DatiComune.objects.get(comune_id =  comune , azienda_id = request.session['azienda'])
                    error = "Il comune inserito è già presente"
                    return HttpResponse(error)

                except DatiComune.DoesNotExist:

                    obj = DatiComune.objects.create(comune_id =  comune , azienda_id = request.session['azienda'])
                    obj.save()
                    comune = str(obj.azienda)
                    azienda = str(obj.comune)
                    os.mkdir(os.path.join(basedir, comune+'/'+azienda))

                    return HttpResponse("OK")

def save_dati_comune(request):

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    id = body['id']
    azienda = body['azienda']

    if 'logged' in request.session is not None:
        if request.session['logged'] == True:
            if 'user_id' and 'azienda' in request.session is not None:
                if azienda == request.session['azienda']:
                    try:
                        obj = DatiComune.objects.get(pk =  id , azienda_id = azienda)
                        obj.ris_ula_o_ore = body['ris_ula_o_ore']
                        obj.tot_app = body['tot_app']
                        obj.app_servizi = body['app_servizi']
                        obj.app_rifiuti_diff = body['app_rifiuti_diff']
                        obj.app_rifiuti_indiff = body['app_rifiuti_indiff']
                        obj.app_igiene = body['app_igiene']
                        obj.altri_gestori_flag = body['altri_gestori_flag']
                        obj.altri_gestori = body['altri_gestori']
                        obj.appalto_attuale_data = body['appalto_attuale_data']
                        obj.impresa_op_com_data = body['impresa_op_com_data']
                        obj.valore_can = body['valore_can']
                        obj.adeg_contr_flag = body['adeg_contr_flag']
                        obj.ricavi_conai = body['ricavi_conai']
                        obj.impresa_cts_flag = body['impresa_cts_flag']
                        obj.impresa_ctr_flag = body['impresa_ctr_flag']
                        obj.spazz_e_ig_flag = body['spazz_e_ig_flag']
                        obj.serv_exra_arera_flag = body['serv_exra_arera_flag']
                        obj.serv_exra_arera = body['serv_exra_arera']
                        obj.lav_in_corso_flag = body['lav_in_corso_flag']
                        obj.lav_in_corso = body['lav_in_corso']
                        obj.var_gest_flag = body['var_gest_flag']
                        obj.var_gest = body['var_gest']
                        obj.miglior_qual_flag = body['miglior_qual_flag']
                        obj.miglior_qual = body['miglior_qual']
                        obj.costi_tqrif_flag = body['costi_tqrif_flag']
                        obj.costi_tqrif = body['costi_tqrif']
                        obj.ton_totali = body['ton_totali']
                        obj.ton_anno_1 = body['ton_anno_1']
                        obj.ton_anno_2 = body['ton_anno_2']
                        obj.ton_anno_3 = body['ton_anno_3']
                        obj.xcent_raccolta_diff = body['xcent_raccolta_diff']
                        obj.xcent_raccolta_anno_1 = body['xcent_raccolta_anno_1']
                        obj.xcent_raccolta_anno_2 = body['xcent_raccolta_anno_2']
                        obj.xcent_raccolta_anno_3 = body['xcent_raccolta_anno_3']
                        obj.xcent_media_imp = body['xcent_media_imp']
                        obj.xcent_media_imp_org = body['xcent_media_imp_org']
                        obj.xcent_media_imp_cart = body['xcent_media_imp_cart']
                        obj.xcent_media_imp_plastica = body['xcent_media_imp_plastica']
                        obj.xcent_media_imp_metallo = body['xcent_media_imp_metallo']
                        obj.xcent_media_imp_vetro = body['xcent_media_imp_vetro']
                        obj.completed = body['completed']

                        obj.save()
                        error = "OK"
                        return HttpResponse(error)

                    except DatiComune.DoesNotExist:

                        error = "Qualcosa è andato storto"

                        return HttpResponse("OK")

def del_comune_azienda(request):

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    comune_azienda = body['comune_azienda']

    if 'logged' in request.session is not None:
        if request.session['logged'] == True:
            if 'user_id' and 'azienda' in request.session is not None:
                try:
                    obj = DatiComune.objects.get(pk =  comune_azienda , azienda_id = request.session['azienda'])
                    obj.delete()
                    msg = "Il comune è stato eliminato"
                    return HttpResponse(msg)

                except DatiComune.DoesNotExist:

                    error = "Coune non trovato"
                    return HttpResponse(error)


def get_dati_comuni(request):

    if 'logged' in request.session is not None:
        if request.session['logged'] == True:
            if 'azienda' in request.session is not None:
                qs = DatiComune.objects.filter(azienda = request.session.get('azienda'))
                serializer = DatiComuneSerializer(qs, many=True)
                return JsonResponse(serializer.data,content_type="application/json",safe=False)
            else:
                return JsonResponse("No Company",content_type="application/json",safe=False)

        else:
            return JsonResponse("Not Logged",content_type="application/json",safe=False)

def get_dati_comune(request):

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    id = body['id']

    if 'logged' in request.session is not None:
        if request.session['logged'] == True:
            if request.session['azienda'] > 0 and request.session['is_assigned'] == True:
                try:
                 qs = DatiComune.objects.get(pk = id ,azienda = request.session['azienda'])
                 serializer = DatiComuneSerializer(qs)
                 return JsonResponse(serializer.data,content_type="application/json",safe=False)
                except DatiComune.DoesNotExist:
                 return JsonResponse(False,content_type="application/json",safe=False)

            else:
                return JsonResponse(False,content_type="application/json",safe=False)

        else:
            return JsonResponse(False,content_type="application/json",safe=False)

def upload_comune_files(request):

    azienda = str(request.FILES['azienda'])
    id = str(request.FILES['id'])

    id = int(id)
    azienda = int(azienda)

    if request.session['logged'] == True:
        if 'user_id' and 'azienda' in request.session is not None:
            if azienda == request.session['azienda']:

                print("vada")
                try:
                    obj = DatiComune.objects.get(pk = id , azienda_id = azienda)
                    az = Azienda.objects.get(pk = azienda)

                    print(settings.MEDIA_ROOT)
                    settings.MEDIA_ROOT = basedir + az.ragione_sociale + '/' + str(obj.comune)
                    print(settings.MEDIA_ROOT)

                    if 'cont_commessa_anno1' in request.FILES is not None:
                         obj.cont_commessa_anno1 = request.FILES['cont_commessa_anno1']
                         obj.save()

                    if 'cont_commessa_anno2' in request.FILES is not None:

                         obj.cont_commessa_anno2 = request.FILES['cont_commessa_anno2']
                         obj.save()

                    if 'contratto_appalto' in request.FILES is not None:

                         obj.contratto_appalto = request.FILES['contratto_appalto']
                         obj.save()

                    if 'ultimo_pef' in request.FILES is not None:

                         obj.ultimo_pef = request.FILES['ultimo_pef']
                         obj.save()

                    error= "OK"
                    return HttpResponse(error)

                except DatiComune.DoesNotExist:

                    error = "Qualcosa è andato storto"
                    return HttpResponse(error)


            else:
                return HttpResponse("company not match")
        else:
            return HttpResponse("user and company not defined")
    else:
        return HttpResponse("not logged")


def upload_company_files(request):

    if 'logged' in request.session is not None:
        if request.session['logged'] == True:
            if request.session['azienda'] > 0 and request.session['is_assigned'] == True:

                 obj = Azienda.objects.get(pk = request.session['azienda'])
                 print(settings.MEDIA_ROOT)
                 settings.MEDIA_ROOT = basedir + obj.ragione_sociale
                 print(settings.MEDIA_ROOT)

                 if 'ammortamenti' in request.FILES is not None:
                     obj.ammortamenti = request.FILES['ammortamenti']
                     obj.save()

                 if 'bilancio_depositato_anno1' in request.FILES is not None:

                     obj.bilancio_depositato_anno1 = request.FILES['bilancio_depositato_anno1']
                     obj.save()

                 if 'bilancio_depositato_anno2' in request.FILES is not None:

                     obj.bilancio_depositato_anno2 = request.FILES['bilancio_depositato_anno2']
                     obj.save()


            else:
                return JsonResponse("False",content_type="application/json",safe=False)

        else:
            return JsonResponse("False",content_type="application/json",safe=False)

    return JsonResponse("False",content_type="application/json",safe=False)



def get_costi_smaltimento(request):

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    id = body['id']

    if 'logged' in request.session is not None:
        if request.session['logged'] == True:
            if request.session['azienda'] > 0 and request.session['is_assigned'] == True:
                try:
                 qs = DatiComune.objects.get(pk = id ,azienda = request.session['azienda'])
                 serializer = DatiComuneSerializer(qs)
                 qs = CostoSmaltimento.objects.filter(daticomune = id)
                 serializer = CostoSmaltimentoSerializer(qs,many=True)
                 return JsonResponse(serializer.data,content_type="application/json",safe=False)
                except DatiComune.DoesNotExist:
                 return JsonResponse(False,content_type="application/json",safe=False)

            else:
                return JsonResponse("No Company",content_type="application/json",safe=False)

        else:
            return JsonResponse("Not Logged",content_type="application/json",safe=False)

def get_aziende(request):

    if 'logged' in request.session is not None:
        if request.session['logged'] == True:
            if request.session['is_admin'] == True and request.session['is_staff'] == True and request.session['is_active'] == True:

                qs = Azienda.objects.all()
                serializer = AziendaSerializer(qs, many=True)
                return JsonResponse(serializer.data,content_type="application/json",safe=False)
        else:
            return JsonResponse("Not Allowed",content_type="application/json",safe=False)

def get_utenti(request):

    if 'logged' in request.session is not None:
        if request.session['logged'] == True:
            if request.session['is_admin'] == True and request.session['is_staff'] == True and request.session['is_active'] == True:

                qs = User.objects.all()
                serializer = UserSerializer(qs, many=True)
                return JsonResponse(serializer.data,content_type="application/json",safe=False)
        else:
            return JsonResponse("Not Allowed",content_type="application/json",safe=False)

def is_logged(request):
    is_logged = False

    if 'logged' in request.session is not None:
        if request.session['logged'] == True:
            is_logged = True
    return JsonResponse(is_logged,safe=False)

def role(request):
    role='Normal'

    if 'logged' in request.session is not None:
        if request.session['logged'] == True:
            if request.session['is_staff'] == True and request.session['is_admin'] == True and request.session['is_active'] == True:
                role='Admin'

    return JsonResponse(role,safe=False)

def is_company_set(request):
    is_company_set = False

    if 'logged' in request.session is not None:
        if request.session['logged'] == True:
            qs = User.objects.get(pk = request.session['user_id'])
            serializer = UserSerializer(qs)
            request.session['azienda'] = serializer.data['azienda']
            request.session['is_assigned'] = serializer.data['is_assigned']

            if request.session['azienda'] > 0 and request.session['is_assigned'] == True:
                is_company_set = True


    return JsonResponse(is_company_set,safe=False)

def get_company_data(request):

    if 'logged' in request.session is not None:
        if request.session['logged'] == True:
            if 'azienda' in request.session is not None:
                qs = Azienda.objects.get(pk = request.session['azienda'])
                serializer = AziendaSerializer(qs)
                return JsonResponse(serializer.data,content_type="application/json",safe=False)
            else:
                return JsonResponse(False,content_type="application/json",safe=False)
        else:
            return JsonResponse(False,content_type="application/json",safe=False)
    else:
        return JsonResponse(False,content_type="application/json",safe=False)

def get_user_data(request):

    if 'logged' in request.session is not None:
        if request.session['logged'] == True:
            if 'user_id' in request.session is not None:
                qs = User.objects.get(pk = request.session['user_id'])
                serializer = UserSerializer(qs)
                return JsonResponse(serializer.data,content_type="application/json",safe=False)

def login(request):

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)



    email = body['email']
    password = body['password']

    #request.session.flush()

    user = authenticate(email=email, password=password)

    if user is not None:

        #login(request,user)
        user = get_user_model().objects.filter(email=email).first()

        if user.azienda is not None:
            request.session['azienda'] = user.azienda.id

        request.session['logged'] = True
        request.session['nome'] = user.nome
        request.session['cognome'] = user.cognome
        request.session['user_id'] = user.id
        request.session['is_assigned'] = user.is_assigned
        request.session['is_admin'] = user.is_admin
        request.session['is_staff'] = user.is_staff
        request.session['is_active'] = user.is_active

        message="SI"

    else:
        message="NO"
    return HttpResponse(message)

def logout(request):

    request.session['logged'] = False

    if 'logged' in request.session is not None:
        del request.session['logged']

    if 'user_id' in request.session is not None:
        del request.session['user_id']

    if 'azienda' in request.session is not None:
        del request.session['azienda']

    if 'nome' in request.session is not None:
        del request.session['nome']

    if 'cognome' in request.session is not None:
        del request.session['cognome']

    if 'is_admin' in request.session is not None:
        del request.session['is_admin']

    if 'is_staff' in request.session is not None:
        del request.session['is_staff']

    if 'is_active' in request.session is not None:
        del request.session['is_active']

    return HttpResponse("Arrivederci")


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
