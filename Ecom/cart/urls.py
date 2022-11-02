from django.urls import path

from . import views
urlpatterns = [
    path("", views.index, name="cartindex"),
    path('signin/', views.signin, name="cartisignin"),
    path('login/', views.login, name="cartlogin"),
    path('about/', views.about, name="cartabout"),
    path('grv/', views.grieve, name="cartgrieve"),
    path('contact/',views.contact,name="cartcontact"),
     path('help/',views.help,name="carthelp"),
     path('logout/',views.index,name="logout"),
      path('ptracker/',views.loctrac,name="carttracker"),
      path('pview',views.prodview,name="prodview"),
      path('search',views.search,name="search"),
      path('offer',views.offers,name="cartoffers"),
      
      
     
     


]
