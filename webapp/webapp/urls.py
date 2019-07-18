from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('jewelleryBill.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
   
    ] +staticfiles_urlpatterns()


