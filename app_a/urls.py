from django.urls import path
from . import views

urlpatterns = [

    path('index/', views.index),
    # path('save/', views.save ),
    path('save/', views.save, name='save'),
    #path('update/', views.update),
    path('update/', views.update),
    path('delete/', views.delete),

]
