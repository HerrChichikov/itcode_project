from django.urls import path
from core import views

app_name = 'core'

urlpatterns = [

    path('publications/', views.PublicationList.as_view(), name='publications'),
    path('publication_detail/<int:pk>', views.PublicationDetail.as_view(), name='publication_detail'),
    path('publication_create', views.PublicationCreate.as_view(), name='publication_create'),
    path('publication_update/<int:pk>', views.PublicationUpdate.as_view(), name='publication_update'),
    path('publication_delete/<int:pk>', views.PublicationDelete.as_view(), name='publication_delete'),

    path('persons/', views.PersonList.as_view(), name='persons'),
    path('person_detail/<int:pk>', views.PersonDetail.as_view(), name='person_detail'),
    path('person_create', views.PersonCreate.as_view(), name='person_create'),
    path('person_update/<int:pk>', views.PersonUpdate.as_view(), name='person_update'),
    path('person_delete/<int:pk>', views.PersonDelete.as_view(), name='person_delete'),
    path('', views.get_main_page, name='main'),
]
