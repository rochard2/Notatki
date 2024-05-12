from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from notatki.forms import CommentForm
from notatki.models import Note


class NoteListView(ListView):
    queryset = Note.published.all()
    context_object_name = 'notes'
    paginate_by = 3
    template_name = 'notatki/post/list.html'


def note_detail(request, year, month, day, slug):
    note = get_object_or_404(Note, slug=slug, status="published",
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    return render(request, 'notatki/post/detail.html', {'note': note})
