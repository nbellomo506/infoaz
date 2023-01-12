from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import RegisterUserView, login,logout,add_comune_azienda,role,is_company_set,get_company_data,assign_azienda,get_aziende,get_utenti, CurrentLoggedInUser,get_dati_comuni,is_logged


from .views import UserViewSet,get_user_data
from .views import AziendaViewSet,savePEF
from .views import DatiComuneViewSet,get_dati_comune
from .views import CostoSmaltimentoViewSet,get_costi_smaltimento
from .views import ChangePasswordView


router = DefaultRouter()

router.register(r'utenti', UserViewSet)
router.register(r'aziende', AziendaViewSet)
router.register(r'dati_comuni', DatiComuneViewSet)
router.register(r'costi_smaltimento', CostoSmaltimentoViewSet)


urlpatterns = [
        path("", include(router.urls)),
        path('change-password', ChangePasswordView.as_view(), name='change-password'),
        path('login', login),
        path('logout', logout),
        path('get_utenti', get_utenti),
        path('add_comune_azienda', add_comune_azienda),
        path('assign_azienda', assign_azienda),
        path('get_company_data', get_company_data),
        path('get_dati_comune', get_dati_comune),
        path('get_costi_smaltimento', get_costi_smaltimento),
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
