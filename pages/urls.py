# pages/urls.py
# from django.urls import path
# from .views import home_page_view


# pages/urls.py
from django.urls import path
from .views import  aboutPageView , homepageview ,baseview# new


urlpatterns = [
    path("", baseview.as_view()),  # new
    path("home/", homepageview.as_view() ,name="home"),  # new
    path("about/", aboutPageView.as_view(),name="about"),   # new
]
   