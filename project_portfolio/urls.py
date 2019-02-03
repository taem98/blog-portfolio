"""blog_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
import blog.views
import portfolio.views
from django.conf import settings # 외우기
from django.conf.urls.static import static #얘도 외우기

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.read, name='read'),
    path('blog/', include('blog.urls')),
    path('portfolio/', portfolio.views.portfolio, name='portfolio'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #외우는 게 답 병렬 더하기

#병렬적으로 더하는 게 싫다면 아래의 방식으로 더해줘도 괜찮음
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
