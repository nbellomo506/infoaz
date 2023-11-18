from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import RegisterUserView, login,logout,add_comune_azienda,role,is_company_set,get_company_data,assign_azienda,get_aziende,get_utenti, CurrentLoggedInUser,get_dati_comuni,is_logged


from .views import UserViewSet,get_user_data,new_user
from .views import AziendaViewSet,savePEF,add_azienda,upload_company_files,del_azienda,update_report,deleteUser,dissociateUser
from .views import DatiComuneViewSet,get_dati_comune,del_comune_azienda,save_dati_comune,upload_comune_files,askHelp
from .views import CostoSmaltimentoViewSet,get_costi_smaltimento,add_costi_smaltimento,update_costi_smaltimento,del_costi_smaltimento
from .views import ChangePasswordView,controlloCodiceVerifica


router = DefaultRouter()

#router.register(r'utenti', UserViewSet)
#router.register(r'aziende', AziendaViewSet)
#router.register(r'dati_comuni', DatiComuneViewSet)
#router.register(r'costi_smaltimento', CostoSmaltimentoViewSet)


urlpatterns = [
        path("", include(router.urls)),
        path('change-password', ChangePasswordView.as_view(), name='change-password'),
        path('login', login),
        path('logout', logout),
        path('new_user', new_user),
        path("controlloCodiceVerifica", controlloCodiceVerifica),
        path('askHelp', askHelp),
        path('get_utenti', get_utenti),
        path('add_comune_azienda', add_comune_azienda),
        path('del_comune_azienda', del_comune_azienda),
        path('save_dati_comune', save_dati_comune),
        path('upload_comune_files', upload_comune_files),
        path('assign_azienda', assign_azienda),
        path('deleteUser', deleteUser),
        path('dissociateUser', dissociateUser),
        path('add_azienda', add_azienda),
        path('del_azienda', del_azienda),
        path('get_company_data', get_company_data),
        path('upload_company_files', upload_company_files),
        path('update_report', update_report),
        path('get_dati_comune', get_dati_comune),
        path('get_costi_smaltimento', get_costi_smaltimento),
        path('add_costi_smaltimento', add_costi_smaltimento),
        path('update_costi_smaltimento', update_costi_smaltimento),
        path('del_costi_smaltimento', del_costi_smaltimento),
        path('savePEF', savePEF),
        path('get_user_data', get_user_data),
        path('is_logged', is_logged),
        path('role', role),
        path('is_company_set', is_company_set),
        path('get_dati_comuni', get_dati_comuni),
        path('get_aziende', get_aziende),
        path('register', RegisterUserView.as_view(), name="register"),
        path('user', CurrentLoggedInUser.as_view({'get': 'retrieve'}), name="current_user")
    ]
