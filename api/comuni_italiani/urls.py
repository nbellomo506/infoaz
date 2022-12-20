from django.urls import include, re_path

from . import views

app_name = 'comuni_italiani'

urlpatterns = [

    re_path(r'^elenco/comuni/provincia/(?P<codice>[0-9]+)/$',
        views.elenco_comuni_provincia, name="elenco_comuni_provincia"),
    re_path(r'^elenco/comuni/provincia/$',
        views.elenco_comuni_provincia, name="elenco_comuni_provincia_post"),

    re_path(r'^elenco/comuni/regione/(?P<codice>[0-9]+)/$',
        views.elenco_comuni_regione, name="elenco_comuni_regione"),
    re_path(r'^elenco/comuni/regione/$',
        views.elenco_comuni_regione, name="elenco_comuni_regione_post"),

    re_path(r'^elenco/comuni/citta_metro/(?P<codice>[0-9]+)/$',
        views.elenco_comuni_cittmetro, name="elenco_comuni_cittmetro"),
    re_path(r'^elenco/comuni/citta_metro/$',
        views.elenco_comuni_cittmetro, name="elenco_comuni_cittmetro_post"),

    re_path(r'^elenco/province/regione/(?P<codice>[0-9]+)/$',
        views.elenco_province_regione, name="elenco_province_regione"),
    re_path(r'^elenco/province/regione/$',
        views.elenco_province_regione, name="elenco_province_regione_post"),

    re_path(r'^elenco/province/$', views.elenco_province, name="elenco_province"),
    re_path(r'^elenco/regioni/$', views.elenco_regioni, name="elenco_regioni"),
    re_path(r'^elenco/citta_metro/$', views.elenco_citta_metro, name="elenco_citta_metro"),

    re_path(r'^ricerca/comune/$', views.ricerca_comune, name="ricerca_comune"),
    re_path(r'^ricerca/provincia/$', views.ricerca_provincia, name="ricerca_provincia"),
    re_path(r'^ricerca/regione/$', views.ricerca_regione, name="ricerca_regione"),
]
