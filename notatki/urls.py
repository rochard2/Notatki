from django.urls import path

from notatki import views

app_name = 'notatki'

urlpatterns = [
    # path('', views.post_list, name='post_list'),
    path('', views.NoteListView.as_view(), name='note_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', views.note_detail, name='note_detail'),
    path('create_temp/', views.create_note, name='create_temp')
]
