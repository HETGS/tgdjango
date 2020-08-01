from django.urls import path

from . import views

urlpatterns = [
    path('<ind:id>', views.ExtractionView.as_view(), name='extraction'),
    ]
