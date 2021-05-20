from django.urls import path

from bt.views import WormList

urlpatterns = [
    path('inside/', WormList.as_view())
    ]