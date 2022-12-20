from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import RegisterUserView, login, CurrentLoggedInUser, export_aziende


from .views import UserViewSet
from .views import AziendaViewSet
from .views import DatiComuneViewSet
from .views import CostoSmaltimentoViewSet
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
        path('export_aziende', export_aziende),
        path('register', RegisterUserView.as_view(), name="register"),
        path('user', CurrentLoggedInUser.as_view({'get': 'retrieve'}), name="current_user")
    ]
