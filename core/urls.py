from django.urls import path
from core import views

app_name = 'core'

urlpatterns = [
    path('', views.get_main_page, name='main'),

    path('publications/', views.PublicationList.as_view(), name='publications'),
    path('publication_detail/<int:pk>', views.PublicationDetail.as_view(), name='publication_detail'),
    path('publication_create', views.PublicationCreate.as_view(), name='publication_create'),
    path('publication_update/<int:pk>', views.PublicationUpdate.as_view(), name='publication_update'),
    path('publication_delete/<int:pk>', views.PublicationDelete.as_view(), name='publication_delete'),
    path('publication_like/<int:pk>', views.publication_like, name="publication_like"),
    path('publication_comment/<int:pk>', views.PublicationCommentCreate.as_view(), name="publication_comment"),
    path('publication_comment_delete/<int:pk>', views.PublicationCommentDelete.as_view(), name='publication_comment_delete'),

    path('persons/', views.PersonList.as_view(), name='persons'),
    path('person_detail/<int:pk>', views.PersonDetail.as_view(), name='person_detail'),
    path('person_create', views.PersonCreate.as_view(), name='person_create'),
    path('person_update/<int:pk>', views.PersonUpdate.as_view(), name='person_update'),
    path('person_delete/<int:pk>', views.PersonDelete.as_view(), name='person_delete'),

    path('register/', views.RegisterUser.as_view(), name='register'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('profiles/', views.ProfileList.as_view(), name='profiles'),
    path('user_update/', views.UserUpdate.as_view(), name='user_update'),
    path('user_profile/<int:pk>', views.ProfileDetail.as_view(), name='user_profile'),
    path('user_profile_create', views.ProfileCreate.as_view(), name='user_profile_create'),
    path('user_profile_update', views.ProfileUpdate.as_view(), name='user_profile_update'),
    path('user_profile_delete/<int:pk>', views.ProfileDelete.as_view(), name='user_profile_delete'),
    path('user_profile_change_role/<int:pk>', views.ProfileChangeRole.as_view(), name='user_profile_change_role'),

    path('logout/', views.logout_user, name='logout'),
]
