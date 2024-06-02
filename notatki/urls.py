from django.urls import path

from notatki import views

app_name = 'notatki'

urlpatterns = [
    # path('', views.post_list, name='post_list'),
    path('', views.NoteListView.as_view(), name='note_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', views.note_detail, name='note_detail'),
    path('create/', views.create_note, name='create'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/edit', views.edit_note, name='edit'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/delete', views.delete_note, name='delete'),
]
