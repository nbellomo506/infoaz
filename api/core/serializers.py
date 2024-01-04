from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from django.conf import settings

from .models import User
from .models import Azienda
from .models import CostoSmaltimento
from .models import DatiComune
from .models import EfficienzaQualitaDifferenziata

from comuni_italiani.models import Comune
from comuni_italiani.models import Provincia
from comuni_italiani.models import Regione


class RegisterUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=get_user_model().objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = get_user_model()
        fields = ('nome','cognome','titolo','ragione_sociale','p_iva','telefono','email','email2','password','verification_code','verified')
        extra_kwargs = {
            'nome': {'required': True},
            'cognome': {'required': True},
            'titolo': {'required': True},
            'password': {'write_only': True, 'min_length': 8},
            'email2' : {'allow_blank':True}
            }

    def create(self, validated_data):
        user = self.Meta.model.objects.create(
            email=validated_data['email'],
            nome=validated_data['nome'],
            cognome=validated_data['cognome'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

    class Meta:
        model = get_user_model()
        fields = ('id','nome','cognome','azienda','titolo','ragione_sociale','p_iva','telefono','email','email2','password','request_date','is_assigned','verified')


        extra_kwargs = {
            'nome': {'required': True},
            'cognome': {'required': True},
            'titolo': {'required': True},
            'password': {'write_only': True, 'min_length': 8},
            'email2' : {'allow_blank':True}
            }

class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class AziendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Azienda
        fields = ("id","report_is_sent","report_attempts","ragione_sociale", "partita_iva","bilancio_depositato_anno1","bilancio_depositato_anno2","cespiti","export_daticomuni","pef_mis_o_ric")

class DatiComuneSerializer(serializers.ModelSerializer):
    nome_regione = serializers.StringRelatedField(source='comune.provincia.regione.name')
    nome_provincia = serializers.StringRelatedField(source='comune.provincia.name')
    nome_comune = serializers.StringRelatedField(source='comune.name')

    nome_azienda = serializers.StringRelatedField(source='azienda.ragione_sociale')

    class Meta:
        model = DatiComune
        fields = ("id","current_section","azienda","nome_azienda","comune","nome_regione","nome_provincia","nome_comune","ris_ula_o_ore","tot_app","app_servizi","app_rifiuti_diff","app_rifiuti_indiff","app_igiene",
                    "altri_gestori_flag",
                    "altri_gestori",
                    "appalto_attuale_data",
                    "impresa_op_com_data",
                    "valore_can",
                    "adeg_contr_flag",
                    "ricavi_conai",
                    "impresa_cts_flag",
                    "impresa_ctr_flag",
                    "spazz_e_ig_flag",
                    "serv_exra_arera_flag",
                    "serv_exra_arera",
                    "lav_in_corso_flag",
                    "lav_in_corso",
                    "var_gest_flag",
                    "var_gest",
                    "miglior_qual_flag",
                    "miglior_qual",
                    "costi_tqrif_flag",
                    "costi_tqrif",
                    "ton_totali",
                    "ton_anno_1",
                    "ton_anno_2",
                    "ton_anno_3",
                    "xcent_raccolta_diff",
                    "xcent_raccolta_anno_1",
                    "xcent_raccolta_anno_2",
                    "xcent_raccolta_anno_3",
                    "xcent_media_imp",
                    "xcent_media_imp_org",
                    "xcent_media_imp_cart",
                    "xcent_media_imp_plastica",
                    "xcent_media_imp_metallo",
                    "xcent_media_imp_vetro",
                    "cont_commessa_anno1",
                    "cont_commessa_anno2",
                    "contratto_appalto",
                    "ultimo_pef",
                    "completed"
                    )

class EfficienzaQualitaDifferenziataSerializer(serializers.ModelSerializer):

    class Meta:
        model = EfficienzaQualitaDifferenziata
        fields = ("azienda","consorzio","pretrattamento","quantita_in_ton","prefatture_a_2")

class CostoSmaltimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostoSmaltimento
        fields = ("id", "daticomune" ,"imp_smalt", "tipo_rifiuto","tipo_costo","anno","tons","prezzo_unitario","importo")
