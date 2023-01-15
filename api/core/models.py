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

        user.set_password(password)
        user.save(using=self._db)
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
    bilancio_depositato_anno1 = models.FileField(default='', blank=True)
    bilancio_depositato_anno2 = models.FileField(default='', blank=True)
    ammortamenti = models.FileField(default='',blank=True)
    export_daticomuni = models.FileField(default='',blank=True)
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

    email_plaintext_message = "{}?token={}".format('http://localhost:3000/new_password' , reset_password_token.key)
    #email_plaintext_message = "{}?token={}".format('http://217.61.57.221/new_password' , reset_password_token.key)
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

class DatiComune(models.Model):

    comune = models.ForeignKey(comuni_italiani.Comune, default='', on_delete = models.SET_DEFAULT)
    azienda =  models.ForeignKey(Azienda, default='', on_delete = models.CASCADE)


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

    xcent_media_imp = models.FloatField(default = 0)
    xcent_media_imp_org = models.FloatField(default = 0)
    xcent_media_imp_cart = models.FloatField(default = 0)
    xcent_media_imp_plastica = models.FloatField(default = 0)
    xcent_media_imp_metallo = models.FloatField(default = 0)
    xcent_media_imp_vetro = models.FloatField(default = 0)

    cont_commessa_anno1 = models.FileField(default='', blank=True)
    cont_commessa_anno2 = models.FileField(default='', blank=True)
    contratto_appalto = models.FileField(default='', blank=True)
    ultimo_pef = models.FileField(default='', blank=True)



    completed = models.BooleanField(default = 0)

    def __str__(self):
        return f'{self.azienda},{self.comune}'

class CostoSmaltimento(models.Model):

    daticomune = models.ForeignKey(DatiComune, default='', on_delete=models.CASCADE)

    imp_smalt = models.CharField(default = '' ,max_length = 255)
    tipo_rifiuto = models.CharField(default = '' ,max_length = 255)

    scelte_tipo_costo = (
        ('CTS', 'CTS'),
        ('CTR', 'CTR')
    )
    tipo_costo = models.CharField(default='', max_length=3, choices=scelte_tipo_costo)

    scelte_anno = (
        ('2020', '2020'),
        ('2021', '2021')
    )
    anno = models.CharField(default='', max_length=4, choices=scelte_anno)
    tons = models.FloatField(default='NULL')
    prezzo_unitario = models.FloatField(default='NULL')
    importo = models.FloatField(default='NULL')
