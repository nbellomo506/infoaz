# Create your views here.
import requests
import json
import os.path
import random

from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import mixins
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
from django.core.mail import send_mail
from django.db import models
from django.db import IntegrityError
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

from .models import Azienda
from .serializers import AziendaSerializer

from .models import User
from .serializers import UserSerializer

from .models import DatiComune
from .serializers import DatiComuneSerializer

from .models import CostoSmaltimento
from .serializers import CostoSmaltimentoSerializer

from .models import EfficienzaQualitaDifferenziata
from .serializers import EfficienzaQualitaDifferenziataSerializer


from comuni_italiani.models import Comune

basedir = settings.MEDIA_ROOT
#basedir = "C:/Users/Administrator/OneDrive/infowaste-aziende/"
recipients = settings.RECIPIENTS

class RegisterUserView(CreateAPIView):
    queryset = get_user_model().objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterUserSerializer

def new_user(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    nome = body['nome']
    cognome = body['cognome']
    titolo = body['titolo']
    ragione_sociale = body['ragione_sociale']
    p_iva = body['p_iva']
    telefono = body['telefono']
    email = body['email']
    email2 = body['email2']
    password = body['password']


    user_obj = User.objects.filter(email = email)
    if len(user_obj) == 1:
        user_obj = user_obj[0]
        if user_obj.verified is False:

            User.objects.filter(email=user_obj.email,verified = False).delete()

            user = User.objects.create(
                                         nome = nome,
                                         cognome = cognome,
                                         titolo = titolo,
                                         ragione_sociale = ragione_sociale,
                                         p_iva = p_iva,
                                         telefono = telefono,
                                         email = email,
                                         email2 = email2,
                                         verification_code = ''.join(random.choice('0123456789ABCDEF') for i in range(5))
                                       )

            user.set_password(password)
            user.save()


            email_plaintext_message = "Si comunica che il codice di verifica relativo al suo account è: " + user.verification_code

            send_mail(
                # title:
                "Codice di Attivazione Account Bintobit Faidate",
                # message:
                email_plaintext_message,
                # from:
                "noreplay@bintobit.com",
                # to:
                [
                    user.email
                    #"assistenza@bintobit.com"
                ]
            )
            return JsonResponse(True,safe=False)

        if user_obj.verified is True:
            return JsonResponse(False,safe=False)

    if not user_obj:
            user = User.objects.create(
                                         nome = nome,
                                         cognome = cognome,
                                         titolo = titolo,
                                         ragione_sociale = ragione_sociale,
                                         p_iva = p_iva,
                                         telefono = telefono,
                                         email = email,
                                         email2 = email2,
                                         verification_code = ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(5))
                                       )

            user.set_password(password)
            user.save()

            email_plaintext_message = "Si comunica che il codice di verifica relativo al suo account è: " + user.verification_code

            send_mail(
                # title:
                "Codice di Attivazione Account Bintobit Faidate",
                # message:
                email_plaintext_message,
                # from:
                "noreplay@bintobit.com",
                # to:
                [
                    user.email
                    #"assistenza@bintobit.com"
                ]
            )
            return JsonResponse(True,safe=False)

def controlloCodiceVerifica(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    email = body['email']
    codiceVerifica = body['codiceVerifica']

    user = User.objects.get(email = email)
    if user is not None:
        if user.verification_code == codiceVerifica:
            user.verified = True
            user.save()
            email_plaintext_message = "Si comunica che " + user.nome + " " + user.cognome + " ha inviato una richiesta di attivazione al servizio."

            send_mail(
                # title:
                "Richiesta Attivazione al Servizio CALCOLO PEF AZIENDE",
                # message:
                email_plaintext_message,
                # from:
                "noreplay@bintobit.com",
                # to:
                [
                    "assistenza@bintobit.com"
                ]
            )
            return JsonResponse(True,safe=False)

        else:
            return JsonResponse(False,safe=False)
    else:
        return JsonResponse(False,safe=False)

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

def dissociateUser(request):

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    user = body['user_id']
    azienda = body['azienda_id']

    if 'logged' in request.session is not None:
        if request.session['logged'] == True:
            if request.session['is_admin'] == True and request.session['is_staff'] == True and request.session['is_active'] == True:
                obj = User.objects.get(pk = user)
                obj.azienda_id = None
                obj.is_assigned = False
                obj.save()
                return JsonResponse("OK",content_type="application/json",safe=False)
        else:
            return JsonResponse("Not Allowed",content_type="application/json",safe=False)
    else:
        return JsonResponse("Not Logged",content_type="application/json",safe=False)

def deleteUser(request):

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    user = body['user_id']

    if 'logged' in request.session is not None:
        if request.session['logged'] == True:
            if request.session['is_admin'] == True and request.session['is_staff'] == True and request.session['is_active'] == True:
                obj = User.objects.get(pk = user).delete()
                return JsonResponse("OK",content_type="application/json",safe=False)
        else:
            return JsonResponse("Not Allowed",content_type="application/json",safe=False)
    else:
        return JsonResponse("Not Logged",content_type="application/json",safe=False)

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
                try:
                    os.mkdir(os.path.join(basedir, ragione_sociale))
                except:
                    print("cartella già esistente")

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

    if request.session['logged'] == True and request.session['user_id'] > 0 and request.session['azienda'] is not None:
        az = Azienda.objects.get(pk = request.session['azienda'])
        if az.report_is_sent == False:
            try:
                obj = DatiComune.objects.create(comune_id=comune, azienda_id=request.session['azienda'])
                obj.save()

                CostoSmaltimento.objects.create(
                    daticomune=obj,
                    anno='2023',
                    imp_smalt='Impianto1',
                    tipo_rifiuto='CER2000301',
                    tipo_costo='CTS',
                    tons=1000,
                    prezzo_unitario=10,
                    importo=10000,
                    tipoImpianto='TMB/TM',
                    gestoreImpianto='Gestore1',
                    note='Indifferenziato').save()

                CostoSmaltimento.objects.create(
                    daticomune=obj,
                    anno='2023',
                    imp_smalt='Impianto2',
                    tipo_rifiuto='CER2000108',
                    tipo_costo='CTR',
                    tons=1000,
                    prezzo_unitario=10,
                    importo=10000,
                    tipoImpianto='Compostaggio',
                    gestoreImpianto='Gestore2',
                    note='Frazione organica').save()

                CostoSmaltimento.objects.create(
                    daticomune=obj,
                    anno='2023',
                    imp_smalt='Impianto3',
                    tipo_rifiuto='CER200101',
                    tipo_costo='CTR',
                    tons=100,
                    prezzo_unitario=10,
                    importo=1000,
                    tipoImpianto='TMB/TM',
                    gestoreImpianto='Gestore3',
                    note='Carta').save()

                CostoSmaltimento.objects.create(
                    daticomune=obj,
                    anno='2023',
                    imp_smalt='Impianto4',
                    tipo_rifiuto='CER200102',
                    tipo_costo='CTR',
                    tons=100,
                    prezzo_unitario=10,
                    importo=1000,
                    tipoImpianto='TMB/TM',
                    gestoreImpianto='Gestore4',
                    note='Vetro').save()

                CostoSmaltimento.objects.create(
                    daticomune=obj,
                    anno='2023',
                    imp_smalt='Impianto5',
                    tipo_rifiuto='CER150102',
                    tipo_costo='CTR',
                    tons=100,
                    prezzo_unitario=10,
                    importo=1000,
                    tipoImpianto='TMB/TM',
                    gestoreImpianto='Gestore5',
                    note='Plastica').save()

                comune = str(obj.comune)
                azienda = str(obj.azienda)
                os.mkdir(os.path.join(basedir, azienda + '/' + comune))

                return HttpResponse("OK")

            except IntegrityError:  # Assuming a database-level unique constraint
                error = "Il comune inserito è già presente"
                return HttpResponse(error)

def askHelp(request):

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    message = body['message']
    section = body['section']

    if request.session['user_id'] > 0 and request.session['is_assigned'] == True and request.session['logged'] == True:

        try:
            user = User.objects.get(pk = request.session['user_id'])
            lista = recipients
            lista.append(user.email)
            print(lista)
            email_plaintext_message = user.nome+" "+user.cognome+" ha inviato un messaggio di help nella sezione " + section + ":\n" + message
            #email_plaintext_message = "{}?token={}".format('http://217.61.57.221/new_password' , reset_password_token.key)
            send_mail(
                # title:
                "Richiesta Assitenza - ",
                # message:
                email_plaintext_message,
                # from:
                "noreplay@bintobit.com",
                # to:
                lista
            )
            return HttpResponse("Messaggio Inviato")

        except Exception as e:
            print(e)
            return HttpResponse("Invio messaggio fallito")
    else:
        return HttpResponse("Accesso negato")


def save_dati_comune(request):

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    id = body['id']
    azienda = body['azienda']

    if 'logged' in request.session is not None:
        if request.session['logged'] == True:
            if 'user_id' and 'azienda' in request.session is not None:
                if azienda == request.session['azienda']:
                    az = Azienda.objects.get(pk = request.session['azienda'])
                    if az.report_attempts > 0 :
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
                            if body['ricavi_conai'] == 'IMPRESA':
                                list = ["RICREA / ACCIAIO","CiAl / ALLUMINIO","COMIECO / CARTA E CARTONE SELETTIVA","COMIECO / CARTA E CARTONE CONGIUNTA","BIOREPACK / BIOPLASTICA COMPOSTABILE","COREVE / VETRO","COREPLA / PLASTICA","CORIPET / PLASTICA","CONIP / PLASTICA","ALTRO"]
                                for consorzio in list:
                                    try:
                                        EfficienzaQualitaDifferenziata.objects.create(azienda = az, consorzio=consorzio)
                                    except Exception as e:
                                        print(e)
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
                            #obj.xcent_media_imp = body['xcent_media_imp']
                            #obj.xcent_media_imp_org = body['xcent_media_imp_org']
                            #obj.xcent_media_imp_cart = body['xcent_media_imp_cart']
                            #obj.xcent_media_imp_plastica = body['xcent_media_imp_plastica']
                            #obj.xcent_media_imp_metallo = body['xcent_media_imp_metallo']
                            #obj.xcent_media_imp_vetro = body['xcent_media_imp_vetro']
                            obj.idArera = body['idArera']
                            obj.current_section = body['current_section']
                            obj.completed = body['completed']

                            obj.save()
                            error = "OK"
                            return HttpResponse(error)

                        except DatiComune.DoesNotExist:

                            error = "Qualcosa è andato storto"

                            return HttpResponse("OK")

def update_compiling_section(request):
    try:
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        id = body['id']
        azienda = body['azienda']
        current_section = body.get('current_section')

        if 'logged' in request.session and request.session['logged']:
            if 'user_id' in request.session and 'azienda' in request.session:
                if azienda == request.session['azienda']:
                    try:
                        obj = DatiComune.objects.get(pk=id, azienda_id=azienda)
                        obj.current_section = current_section
                        obj.save()
                        return HttpResponse("OK")
                    except DatiComune.DoesNotExist:
                        return HttpResponse("Errore", status=404)

        return HttpResponse("Non autorizzato", status=401)

    except Exception as e:
        return HttpResponse(f"Error: {str(e)}", status=500)


def getEfficienzaQualitaDifferenziata(request):

    if 'logged' in request.session is not None and 'azienda' in request.session is not None:
        if request.session['logged'] == True:
            if 'email' in request.session is not None:
                qs = EfficienzaQualitaDifferenziata.objects.filter(azienda = Azienda.objects.get(pk = request.session['azienda']))
                serializer = EfficienzaQualitaDifferenziataSerializer(qs,many=True)
                return JsonResponse(serializer.data,content_type="application/json",safe=False)
            else:
                return JsonResponse(False,safe=False)
        else:
            return JsonResponse(False,safe=False)
    else:
        return JsonResponse(False,safe=False)

def saveEfficienzaQualitaDifferenziata(request):

    if 'logged' in request.session is not None and 'azienda' in request.session is not None:
        azienda = request.session['azienda']
        az = Azienda.objects.get(pk = azienda)
        comune = request.POST['comune']
        comune = Comune.objects.get(id = comune)
        comune = str(comune)
        if request.session['logged'] == True:
            if 'email' in request.session is not None:
                folderName = "EFFICIENZA E QUALITA' DIFFERENZIATA a-2"
                data = request.POST
                # Iterate through each key and its values
                for key, values in data.lists():
                    if key != 'comune':
                        obj = EfficienzaQualitaDifferenziata.objects.get(consorzio = key,azienda = azienda)
                        obj.quantita_in_ton = values[0]
                        if values[1] == "false":
                            obj.pretrattamento = False
                        else:
                            obj.pretrattamento = True
                        obj.save()
                try:
                    os.mkdir(os.path.join(basedir + '/' + az.ragione_sociale + '/'+ comune + '/' + folderName))
                except Exception as e:
                    print(e)
                for file in request.FILES:
                    folderfile = file.replace("/","-")
                    consorzio = file
                    file = request.FILES[file]
                    obj = EfficienzaQualitaDifferenziata.objects.get(consorzio = consorzio,azienda = azienda)
                    obj.prefatture_a_2 = file
                    obj.save()
                    try:
                        os.mkdir(os.path.join(basedir + '/' + az.ragione_sociale + '/' + comune + '/' +  folderName + '/' + folderfile))
                    except Exception as e:
                        print(e)
                    with open(basedir + '/' + az.ragione_sociale + '/' + comune + '/' + folderName + '/' + folderfile + '/' + file.name,'wb+') as destination:
                        for chunk in file.chunks():
                            destination.write(chunk)

                return JsonResponse(True,safe=False)
            else:
                return JsonResponse(False,safe=False)
        else:
            return JsonResponse(False,safe=False)
    else:
        return JsonResponse(False,safe=False)

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
                obj = DatiComune.objects.get(pk = id , azienda_id = azienda)
                az = Azienda.objects.get(pk = azienda)
                try:
                    if 'cont_commessa_anno_2' in request.FILES is not None:
                         file = request.FILES['cont_commessa_anno_2']
                         obj.cont_commessa_anno_2 = file.name
                         obj.save()
                         with open(basedir + '/' + az.ragione_sociale + '/' + str(obj.comune) + '/' + file.name,'wb+') as destination:
                             for chunk in file.chunks():
                                 destination.write(chunk)

                    if 'contratto_appalto' in request.FILES is not None:
                         file = request.FILES['contratto_appalto']
                         obj.contratto_appalto = file.name
                         obj.save()
                         with open(basedir + '/' + az.ragione_sociale + '/' + str(obj.comune) + '/' + file.name,'wb+') as destination:
                             for chunk in file.chunks():
                                 destination.write(chunk)

                    if 'pef_valid_ETC_a_2' in request.FILES is not None:
                         file = request.FILES['pef_valid_ETC_a_2']
                         obj.pef_valid_ETC_a_2 = file.name
                         obj.save()
                         with open(basedir + '/' + az.ragione_sociale + '/' + str(obj.comune) + '/' + file.name,'wb+') as destination:
                             for chunk in file.chunks():
                                 destination.write(chunk)

                    
                    if 'mud_a_2' in request.FILES is not None:
                         file = request.FILES['mud_a_2']
                         obj.mud_a_2 = file.name
                         obj.save()
                         with open(basedir + '/' + az.ragione_sociale + '/' + str(obj.comune) + '/' + file.name,'wb+') as destination:
                             for chunk in file.chunks():
                                 destination.write(chunk)

                    if 'mud_a_1' in request.FILES is not None:
                         file = request.FILES['mud_a_1']
                         obj.mud_a_1 = file.name
                         obj.save()
                         with open(basedir + '/' + az.ragione_sociale + '/' + str(obj.comune) + '/' + file.name,'wb+') as destination:
                             for chunk in file.chunks():
                                 destination.write(chunk)
                    

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

                 az = Azienda.objects.get(pk = request.session['azienda'])

                 if 'cespiti' in request.FILES is not None:

                     file = request.FILES['cespiti']
                     az.cespiti = file.name
                     az.save()
                     with open(basedir + '/' + az.ragione_sociale + '/' + file.name,'wb+') as destination:
                         for chunk in file.chunks():
                             destination.write(chunk)

                 if 'bilancio_depositato_anno1' in request.FILES is not None:

                     file = request.FILES['bilancio_depositato_anno1']
                     az.bilancio_depositato_anno1 = file.name
                     az.save()
                     with open(basedir + '/' + az.ragione_sociale + '/' + file.name,'wb+') as destination:
                         for chunk in file.chunks():
                             destination.write(chunk)

                 if 'bilancio_depositato_anno2' in request.FILES is not None:

                     file = request.FILES['bilancio_depositato_anno2']
                     az.bilancio_depositato_anno2 = file.name
                     az.save()
                     with open(basedir + '/' + az.ragione_sociale + '/' + file.name,'wb+') as destination:
                         for chunk in file.chunks():
                             destination.write(chunk)


                 if 'export_daticomuni' in request.FILES is not None:
                     az.export_daticomuni = request.FILES['export_daticomuni']
                     file = az.export_daticomuni
                     with open(basedir + '/' + az.ragione_sociale + '/' + file.name,'wb+') as destination:
                         for chunk in az.export_daticomuni.chunks():
                             destination.write(chunk)
                     #az.save()

            else:
                return JsonResponse("False",content_type="application/json",safe=False)

        else:
            return JsonResponse("False",content_type="application/json",safe=False)

    return JsonResponse("False",content_type="application/json",safe=False)

def update_report(request):


        if request.session['logged'] == True:
            if request.session['azienda'] > 0 and request.session['is_assigned'] == True:

                az = Azienda.objects.get(pk = request.session['azienda'])

                if az.report_attempts > 0:
                    az.report_is_sent = not az.report_is_sent

                    if az.report_is_sent == True:
                        az.report_attempts = az.report_attempts - 1
                        az.save()

                        user = User.objects.get(pk = request.session['user_id'])
                        email_plaintext_message = "Si comunica che " + user.nome + " " + user.cognome + " ha inviato il report relativo all'azienda " + az.ragione_sociale + ".\nQuesta azienda ha inviato il report " + str( 5 - az.report_attempts ) + " volte"
                        #email_plaintext_message = "{}?token={}".format('http://217.61.57.221/new_password' , reset_password_token.key)
                        send_mail(
                            # title:
                            "INVIO REPORT AZIENDE - " + az.ragione_sociale,
                            # message:
                            email_plaintext_message,
                            # from:
                            "noreplay@bintobit.com",
                            # to:
                            recipients
                        )

                    az.save()

            else:
                return JsonResponse("False",content_type="application/json",safe=False)

        else:
            return JsonResponse("False",content_type="application/json",safe=False)

        return JsonResponse("False",content_type="application/json",safe=False)

def get_costi_smaltimento(request):

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    id = body['id']


    if 'logged' and 'azienda' in request.session is not None:
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

def add_costi_smaltimento(request):
    try:
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        new_item = body.get('data', {})  # Adjusted to handle `data` wrapper

        # Extracting fields from the nested `data` dictionary
        daticomune = new_item.get('daticomune')
        imp_smalt = new_item.get('imp_smalt')
        tipo_rifiuto = new_item.get('tipo_rifiuto')
        tipo_costo = new_item.get('tipo_costo')
        anno = new_item.get('anno')
        tons = new_item.get('tons')
        prezzo_unitario = new_item.get('prezzo_unitario')
        importo = new_item.get('importo')
        tipoImpianto = new_item.get('tipoImpianto')
        gestoreImpianto = new_item.get('gestoreImpianto')
        partitaIvaGestoreImpianto = new_item.get('partitaIvaGestoreImpianto')
        comuneSedeImpianto = new_item.get('comuneSedeImpianto')
        impiantoDestinazione = new_item.get('impiantoDestinazione')
        note = new_item.get('note')

        # Check session validity
        if request.session.get('logged') and request.session.get('azienda'):
            if request.session['azienda'] > 0 and request.session.get('is_assigned', False):
                try:
                    qs = DatiComune.objects.get(pk=daticomune, azienda=request.session['azienda'])
                    serializer = DatiComuneSerializer(qs)

                    # Create the CostoSmaltimento object
                    obj = CostoSmaltimento.objects.create(
                        daticomune=qs,
                        imp_smalt=imp_smalt,
                        tipo_rifiuto=tipo_rifiuto,
                        tipo_costo=tipo_costo,
                        anno=anno,
                        tons=tons,
                        prezzo_unitario=prezzo_unitario,
                        importo=importo,
                        tipoImpianto=tipoImpianto,
                        gestoreImpianto=gestoreImpianto,
                        partitaIvaGestoreImpianto=partitaIvaGestoreImpianto,
                        comuneSedeImpianto=comuneSedeImpianto,
                        impiantoDestinazione=impiantoDestinazione,
                        note=note
                    )
                    obj.save()

                    return JsonResponse(serializer.data, content_type="application/json", safe=False)
                except DatiComune.DoesNotExist:
                    return JsonResponse({"error": "Impossibile stabilire il comune di riferimento"}, content_type="application/json", safe=False)

            return JsonResponse({"error": "Non sei ancora associato ad un'azienda"}, content_type="application/json", safe=False)

        return JsonResponse({"error": "Devi effettuare prima l'accesso"}, content_type="application/json", safe=False)

    except Exception as e:
        return JsonResponse({"error": str(e)}, content_type="application/json", safe=False)


def update_costi_smaltimento(request):
    try:
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        updated_item = body.get('data', {})  # Adjusted to handle `data` wrapper

        # Extracting fields from the nested `data` dictionary
        id = updated_item.get('id')
        daticomune = updated_item.get('daticomune')
        gestore = updated_item.get('gestore')
        imp_smalt = updated_item.get('imp_smalt')
        tipo_rifiuto = updated_item.get('tipo_rifiuto')
        tipo_costo = updated_item.get('tipo_costo')
        anno = updated_item.get('anno')
        tons = updated_item.get('tons')
        prezzo_unitario = updated_item.get('prezzo_unitario')
        importo = updated_item.get('importo')
        tipoImpianto = updated_item.get('tipoImpianto')
        gestoreImpianto = updated_item.get('gestoreImpianto')
        partitaIvaGestoreImpianto = updated_item.get('partitaIvaGestoreImpianto')
        comuneSedeImpianto = updated_item.get('comuneSedeImpianto')
        impiantoDestinazione = updated_item.get('impiantoDestinazione')
        note = updated_item.get('note')

        # Check session validity
        if request.session.get('logged') and request.session.get('azienda'):
            if request.session['azienda'] > 0 and request.session.get('is_assigned', False):
                try:
                    qs = DatiComune.objects.get(pk=daticomune, azienda=request.session['azienda'])
                    serializer = DatiComuneSerializer(qs)

                    try:
                        # Retrieve and update the CostoSmaltimento object
                        obj = CostoSmaltimento.objects.get(pk=id)
                        obj.daticomune = qs
                        obj.gestore = gestore
                        obj.imp_smalt = imp_smalt
                        obj.tipo_rifiuto = tipo_rifiuto
                        obj.tipo_costo = tipo_costo
                        obj.anno = anno
                        obj.tons = tons
                        obj.prezzo_unitario = prezzo_unitario
                        obj.importo = importo
                        obj.tipoImpianto = tipoImpianto
                        obj.gestoreImpianto = gestoreImpianto
                        obj.partitaIvaGestoreImpianto = partitaIvaGestoreImpianto
                        obj.comuneSedeImpianto = comuneSedeImpianto
                        obj.impiantoDestinazione = impiantoDestinazione
                        obj.note = note
                        obj.save()

                        return JsonResponse(serializer.data, content_type="application/json", safe=False)
                    except CostoSmaltimento.DoesNotExist:
                        return JsonResponse({"error": "CostoSmaltimento does not exist"}, content_type="application/json", safe=False)

                except DatiComune.DoesNotExist:
                    return JsonResponse({"error": "DatiComune does not exist"}, content_type="application/json", safe=False)

            return JsonResponse({"error": "No valid company assigned"}, content_type="application/json", safe=False)

        return JsonResponse({"error": "User not logged in"}, content_type="application/json", safe=False)

    except Exception as e:
        return JsonResponse({"error": str(e)}, content_type="application/json", safe=False)

def del_costi_smaltimento(request):

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    id = body['id']
    daticomune = body['daticomune']


    if 'logged' and 'azienda' in request.session is not None:
        if request.session['logged'] == True:
            if request.session['azienda'] > 0 and request.session['is_assigned'] == True:
                try:
                 qs = DatiComune.objects.get(pk = daticomune ,azienda = request.session['azienda'])
                 serializer = DatiComuneSerializer(qs)

                 obj = CostoSmaltimento.objects.get(pk = id)
                 obj.delete()


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

    if 'logged' in request.session is not None:
        if request.session['logged'] == True:
            return JsonResponse(True,safe=False)
        else:
            return JsonResponse(False,safe=False)
    else:
        return JsonResponse(False,safe=False)

def role(request):
    role='Normal'

    if 'logged' in request.session is not None:
        if request.session['logged'] == True:
            if request.session['is_staff'] == True and request.session['is_admin'] == True and request.session['is_active'] == True:
                role='Admin'

    return JsonResponse(role,safe=False)

def is_company_set(request):
    is_company_set = False

    if 'logged' in request.session is not None :
        if request.session['logged'] == True:
            qs = User.objects.get(pk = request.session['user_id'],verified=True)
            serializer = UserSerializer(qs)
            request.session['azienda'] = serializer.data['azienda']
            request.session['is_assigned'] = serializer.data['is_assigned']

            if request.session['azienda'] is not None and request.session['is_assigned'] is not None and request.session['is_assigned'] is True :
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
            else:
                return JsonResponse(False,content_type="application/json",safe=False)
        else:
            return JsonResponse(False,content_type="application/json",safe=False)
    else:
        return JsonResponse(False,content_type="application/json",safe=False)

def login(request):
    
    body = json.loads(request.body.decode('utf-8'))
    email, password = body['email'], body['password']

    # Authenticate user
    user = authenticate(email=email, password=password)

    if not user:
        return JsonResponse({'message': "Email o password errati."}, status=400)

    if user.verified and user.is_active:
        # If the user is associated with a company
        if user.azienda:
            request.session.update({
                'azienda': user.azienda.id
            })

        # Update session variables
        request.session.update({
            'logged': True,
            'user_id': user.id,
            'email': user.email,
            'verified': user.verified,
            'nome': user.nome,
            'cognome': user.cognome,
            'is_assigned': user.is_assigned,
            'is_admin': user.is_admin,
            'is_staff': user.is_staff,
            'is_active': user.is_active,
        })

        return JsonResponse({'message': "OK"}, status=200)

    elif not user.verified:
        return JsonResponse({'message': "Il tuo account non è stato verificato."}, status=403)

    else:
        return JsonResponse({'message': "Email o password errati."}, status=400)


    

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

    if 'verified' in request.session is not None:
        del request.session['verified']

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
    queryset = User.objects.filter(pk = -1)
    http_method_names = [ 'post']

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
