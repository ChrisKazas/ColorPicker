from django.urls import path

from helloapp.views import ColorickerView

urlpatterns = [
    path('', ColorickerView.as_view(), name='paint')
]