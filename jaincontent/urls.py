from django.conf.urls import url
from .views import  RegisterView, CategoryView, GetAllCategories

urlpatterns = [

   url(r'^get_categories/', GetAllCategories.as_view(), name='get_categories'),
   url(r'^category/', CategoryView.as_view(), name='category'),
    url(r'^register/', RegisterView.as_view(), name='register'),
]
