from django.urls import path

from . import views

app_name = 'birthday'

urlpatterns = [
    # path('', views.birthday, name='create'),  # без CBV
    # path('list/', views.birthday_list, name='list'), # без CBV
    # path('<int:pk>/edit/', views.birthday, name='edit'),  # без CBV
    # path('<int:pk>/delete/', views.delete_birthday, name='delete'), # без CBV
    path('', views.BirthdayCreateView.as_view(), name='create'),  # CBV
    path('list/', views.BirthdayListView.as_view(), name='list'),  # CBV
    path('<int:pk>/', views.BirthdayDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', views.BirthdayUpdateView.as_view(), name='edit'),  # CBV
    path('<int:pk>/delete/', views.BirthdayDeleteView.as_view(), name='delete')  # CBV
]
