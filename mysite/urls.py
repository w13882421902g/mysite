from django.contrib import admin
from django.urls import path

from app01 import views

urlpatterns = [
    #path('admin/', admin.site.urls),

    path('index/',views.index),

    path('user/lise/',views.user_list),

    path('user/add',views.user_add),

    path('tpl/',views.tpl),

    path('weather/',views.weather),

    path('login/',views.login),

    path('orm/',views.orm),

    path('info/list/', views.info_list),

    path('info/add/', views.info_add),

    path('info/delete/',views.info_delete),

]
