"""metrology_journal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    #Calculation of losses
    path('', include('accounts.urls')),
    path('oks/', include('journal_oks.urls')),
    path('rtp/', include('journal_rtp.urls')),
    path('rmo/', include('journal_rmo.urls')),
    path('koff/', include('journal_koff.urls')),
    path('koff_s/', include('journal_koff_s.urls')),
    path('pgk/', include('journal_pgk.urls')),
    
    #raports
    path('raports/', include('raports.urls')),

    #autorization
    path('admin/', admin.site.urls),
    # path('login/', include('accounts.urls')),
    path('', include('django.contrib.auth.urls')),
    # url(r'^/login/$', 'django.contrib.auth.views.login'),
    


]
