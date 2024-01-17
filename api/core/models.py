from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from comuni_italiani import models as comuni_italiani
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail
import datetime

# Create your models here.
class CustomUserManager(BaseUserManager):

    def create_user(self,nome,cognome,titolo,ragione_sociale,p_iva,telefono,email,email2,password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            nome=nome,
            cognome=cognome,
            telefono=telefono,
            email2=email2,
            titolo=titolo,
            ragione_sociale=ragione_sociale,
            p_iva=p_iva

        )

        user.request_date = datetime.datetime.now()
        user.set_password(password)
        user.save(using=self._db)
        email_plaintext_message = "Si comunica che " + user.nome + " " + user.cognome + " ha inviato una richiesta di attivazione al servizio."
        #email_plaintext_message = "{}?token={}".format('http://217.61.57.221/new_password' , reset_password_token.key)
        send_mail(
            # title:
            "Richiesta Attivazione al Serivzio",
            # message:
            email_plaintext_message,
            # from:
            "noreplay@bintobit.com",
            # to:
            [
                "nbellomo506@gmail.com",
                #"assistenza@bintobit.com"
            ]
        )
        #CODICE DI VERIFICA UTENTE
        email_plaintext_message = "Si comunica che il codice di verifica relativo al suo account è: " + user.verification_code

        send_mail(
            # title:
            "Codice di Attivazione Account Bintobit Aziende",
            # message:
            email_plaintext_message,
            # from:
            "noreplay@bintobit.com",
            # to:
            [
                "nbellomo506@gmail.com",
                #"assistenza@bintobit.com"
            ]
        )
        return user

    def create_superuser(self, email, password=None):

        user = self.model(
            email=self.normalize_email(email),
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class Azienda(models.Model):

    ragione_sociale = models.CharField(max_length = 255,default='')
    partita_iva = models.CharField(max_length = 11,default='')
    bilancio_depositato_anno1 = models.CharField(max_length= 512,default='',blank=True)
    bilancio_depositato_anno2 = models.CharField(max_length= 512,default='',blank=True)
    cespiti = models.CharField(max_length = 512,default='',blank=True)
    export_daticomuni = models.CharField(max_length= 512,default='',blank=True)
    report_attempts = models.IntegerField(default = 5)
    report_is_sent = models.BooleanField(default = False)

    scelte_pef = (
        [('CALCOLATO', 'CALCOLATO'),
        ('MISURATO', 'MISURATO')]
    )
    pef_mis_o_ric = models.CharField(default='', max_length=16, choices=scelte_pef)
    def __str__(self):
        return self.ragione_sociale


class User(AbstractUser, PermissionsMixin):
    email = models.CharField(max_length= 200, unique = True)
    email2 = models.CharField(max_length= 200, default = '',null=True, blank=True)
    azienda =  models.ForeignKey(Azienda, default = '', null=True, blank=True,on_delete=models.SET_DEFAULT)
    nome = models.CharField(max_length= 25, default='')
    cognome = models.CharField(max_length= 25,default='')
    password = models.CharField(max_length= 200)

    username = None
    scelte_titolo = (
        ('ambiente', 'ambiente'),
        ('consulente', 'consulente'),
        ('amministrazione', 'amministrazione'),
        ('logistica', 'logistica'),
    )
    titolo = models.CharField(max_length = 255, default='',choices=scelte_titolo)

    ragione_sociale = models.CharField(max_length = 255, default='')
    p_iva = models.CharField(max_length = 11, default='')
    telefono = models.CharField(max_length = 20, default='')
    request_date = models.DateTimeField(default = datetime.datetime.now())

    verification_code = models.CharField(default = 0, max_length=5)
    verified = models.BooleanField(default=False)

    is_assigned = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    objects = CustomUserManager()
    #azienda = models.ForeignKey(Azienda, default='', on_delete= models.CASCADE)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return f'{self.nome} {self.cognome}'

    def save(self, *args, **kwargs):
         if not self.email2:
              self.email2 = None
         super(User, self).save(*args, **kwargs)

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "Utilizzare il seguente link per il ripristino della password:\n"
    email_plaintext_message += "{}?token={}".format('https://aziende.bintobit.com/new_password' , reset_password_token.key)
    send_mail(
        # title:
        "Richiesta recupero password {title}".format(title="Infowaste Modulo Aziende"),
        # message:
        email_plaintext_message,
        # from:
        "noreplay@bintobit.com",
        # to:
        [reset_password_token.user.email]
    )

class Report(models.Model):

    azienda =  models.ForeignKey(Azienda, default = '', null=True, blank=True,on_delete=models.SET_DEFAULT)
    user_sent_id = models.ForeignKey(User, default = '', null=True, blank=True,on_delete=models.SET_DEFAULT)
    request_date = models.DateTimeField(default = datetime.datetime.now())


class DatiComune(models.Model):

    comune = models.ForeignKey(comuni_italiani.Comune, default='', on_delete = models.SET_DEFAULT)
    azienda =  models.ForeignKey(Azienda, default='', on_delete = models.CASCADE)
    current_section = models.IntegerField(default=1)

    scelte_pef = (
        [('CALCOLATO', 'CALCOLATO'),
        ('MISURATO', 'MISURATO')]
    )
    pef_mis_o_ric = models.CharField(default='', max_length=16, choices=scelte_pef)

    scelte_unita = (
        [('ULA', 'ULA'),
        ('ORE LAVORATE', 'ORE LAVORATE')]
    )
    ris_ula_o_ore = models.CharField(default = '' ,blank = True,max_length = 16 ,choices=scelte_unita)

    tot_app = models.FloatField(default = 0)
    app_servizi = models.FloatField(default = 0)
    app_rifiuti_diff = models.FloatField(default = 0)
    app_rifiuti_indiff = models.FloatField(default = 0)
    app_igiene = models.FloatField(default = 0)

    altri_gestori_flag = models.BooleanField(default = False)
    altri_gestori = models.CharField(max_length = 512,default = '',blank=True)

    appalto_attuale_data = models.DateField(default="1970-01-01")
    impresa_op_com_data = models.DateField(default="1970-01-01")

    valore_can = models.FloatField(default = 0)
    adeg_contr_flag = models.BooleanField(default = False)

    scelte_conai = (
        [('IMPRESA', 'IMPRESA'),
        ('COMUNE', 'COMUNE')]
    )
    ricavi_conai = models.CharField(default = 'IMPRESA',max_length = 16,choices=scelte_conai)

    impresa_cts_flag = models.BooleanField(default = False)
    impresa_ctr_flag = models.BooleanField(default = False)

    spazz_e_ig_flag = models.BooleanField(default = False)

    serv_exra_arera_flag = models.BooleanField(default = False)
    serv_exra_arera = models.CharField(max_length = 512,default = '',blank=True)

    lav_in_corso_flag = models.BooleanField(default = False)
    lav_in_corso = models.CharField(max_length = 512,default = '',blank=True)

    var_gest_flag = models.BooleanField(default = False)
    var_gest = models.CharField(max_length = 512,default = '',blank=True)

    miglior_qual_flag = models.BooleanField(default = False)
    miglior_qual = models.CharField(max_length = 512,default = '',blank=True)

    costi_tqrif_flag = models.BooleanField(default = False)
    costi_tqrif = models.FloatField(default = 0)

    #dati tecnici

    ton_totali = models.FloatField(default = 0)
    ton_anno_1 = models.FloatField(default = 0)
    ton_anno_2 = models.FloatField(default = 0)
    ton_anno_3 = models.FloatField(default = 0)

    xcent_raccolta_diff = models.FloatField(default = 0)
    xcent_raccolta_anno_1 = models.FloatField(default = 0)
    xcent_raccolta_anno_2 = models.FloatField(default = 0)
    xcent_raccolta_anno_3 = models.FloatField(default = 0)

    cont_commessa_anno1 = models.CharField(max_length = 512,default = '',blank = True)
    cont_commessa_anno2 = models.CharField(max_length = 512,default = '',blank = True)
    contratto_appalto = models.CharField(max_length = 512,default = '',blank = True)
    ultimo_pef = models.CharField(max_length = 512,default = '',blank = True)

    idArera = models.CharField(default="",max_length=128,blank=True)


    completed = models.BooleanField(default = 0)

    def __str__(self):
        return f'{self.azienda},{self.comune}'


class EfficienzaQualitaDifferenziata(models.Model):

    azienda =  models.ForeignKey(Azienda, default = '', null=True,blank=True,on_delete=models.CASCADE)

    consorzio = models.CharField(max_length=1025,blank=True)
    pretrattamento = models.BooleanField(default = False)
    quantita_in_ton = models.FloatField(default = 0)
    prefatture_a_2 = models.CharField(max_length=1024,blank=True)

    class Meta:
        unique_together = (('azienda','consorzio'))

    def __str__(self):
        return f'AZIENDA : {self.azienda}, CONSORZIO : {self.consorzio}'


class CostoSmaltimento(models.Model):

    daticomune = models.ForeignKey(DatiComune, default='', on_delete=models.CASCADE)

    imp_smalt = models.CharField(default = '' ,max_length = 255)
    tipo_rifiuto = models.CharField(default = '' ,max_length = 255)

    scelte_tipo_costo = (
        ('CTS', 'CTS'),
        ('CTR', 'CTR')
    )
    tipo_costo = models.CharField(default='', max_length=3, choices=scelte_tipo_costo)

    scelte_gestore = (
        [('GESTORE', 'GESTORE'),
        ('COMUNE', 'COMUNE')]
    )
    gestore = models.CharField(default='', max_length=16, choices=scelte_gestore)

    scelte_anno = (
        ('2022', '2022'),
        ('2023', '2023')
    )
    anno = models.CharField(default='', max_length=4, choices=scelte_anno)
    tons = models.FloatField(default='NULL')
    prezzo_unitario = models.FloatField(default='NULL')
    importo = models.FloatField(default='NULL')

    tipoImpianto = models.CharField(max_length = 256,default=None,null=True)
    gestoreImpianto = models.CharField(max_length = 256,default=None,null=True)
    partitaIvaGestoreImpianto = models.CharField(max_length = 11,default=None,null=True)
    comuneSedeImpianto = models.CharField(max_length = 128,default=None,null=True)
    impiantoDestinazione = models.CharField(max_length = 512,default=None,null=True)
    note = models.CharField(max_length = 1024,default=None,null=True)
