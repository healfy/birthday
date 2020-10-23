"""birthday URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from app import views as v
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v.IndexView.as_view()),
    path('post/create/', v.PostCreateView.as_view()),
    path('post/<int:pk>/', v.SinglePost.as_view(), name='post_detail'),
    path('post/list/', v.PostListView.as_view(), name='list'),
    path('login/', v.LoginFormView.as_view()),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
