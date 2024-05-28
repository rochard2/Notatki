from django import forms

from notatki.models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'body', 'priority', 'author', 'status']
