"""
URL configuration for django_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('api/', include('polls.api_urls')),   
    path('accounts/', include('accounts.urls')),  # Include accounts URLs
]

from django_app import views

#custom error handler
handler404 ='django_app.views.handler404'


# Get list of Questions
# curl -X GET http://127.0.0.1:8000/api/questions/
# Create a new question
# curl -X POST http://127.0.0.1:8000/api/questions/ \
#      -H 'Content-Type: application/json' \
#      -d '{"question_text": "New Question?", "pub_date": "2024-10-16T12:00:00Z"}'