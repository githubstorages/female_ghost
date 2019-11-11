"""kankan path Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a path to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a path to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a path to urlpatterns:  path('blog/', include('blog.urls'))
"""

import os

from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings

from rest_framework.permissions import AllowAny
from rest_framework.documentation import include_docs_urls

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .lib.checkers import uptime, health_check

from .lib.endpoints import GoogleEndpointSchemaGenerator

DEBUG = True

CORS_ORIGIN_ALLOW_ALL = True  # So we do not need to keep adding CORS ORIGIN when we have new frontend service/s

urlpatterns = [
    path('femaleghostcharm/', admin.site.urls),
    path('uptime/', uptime),
    path('healthcheck/', health_check),


]


if settings.DEBUG:
    schema_view = get_schema_view(
        openapi.Info(
            title="API Documentation",
            default_version='',
            description='',
            terms_of_service="#",
            contact=openapi.Contact(email='manila@unnotech.com'),
            license=openapi.License(name='BSD License'),
        ),
        f'http://{os.environ.get("OPENAPI_HOST")}',
        public=True,
        generator_class=GoogleEndpointSchemaGenerator,
        permission_classes=(AllowAny,),
    )
    api_docs = [
        re_path('docs/',
            include_docs_urls(title='API Docs',
                              permission_classes=(AllowAny,))),
        re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0),
            name='schema-json'),
        re_path(r'^swagger/$',
            schema_view.with_ui('swagger', cache_timeout=0),
            name='schema-swagger-ui'),
        re_path(r'^redoc/$',
            schema_view.with_ui('redoc', cache_timeout=0),
            name='schema-redoc')
    ]
    urlpatterns += api_docs


