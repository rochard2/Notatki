from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils.text import slugify
from django.views.generic import ListView

from notatki.models import Note
from notatki.forms import NoteForm


class NoteListView(ListView):
    queryset = Note.published.all().filter(priority__in=('high', 'medium', 'low')).order_by('priority')
    context_object_name = 'notes'
    paginate_by = 3
    template_name = 'notatki/post/list.html'


def note_detail(request, year, month, day, slug):
    note = get_object_or_404(Note, slug=slug, status="published",
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    return render(request, 'notatki/post/detail.html', {'note': note})


def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)

        if form.is_valid():
            note = form.save(commit=False)
            note.author = User.objects.get(id=1)
            note.slug = slugify(form.cleaned_data['title'])
            note.save()

            return render(request, 'notatki/create.html', {'form': form})

    else:
        form = NoteForm()

    return render(request, 'notatki/create.html', {'form': form})


def edit_note(request, year, month, day, slug):
    note = get_object_or_404(Note, slug=slug,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)

        if form.is_valid():
            form.save()
            return redirect(f'/{year}/{month}/{day}/{slug}')

    else:
        form = NoteForm(instance=note)

    return render(request, 'notatki/edit.html', {'form': form, 'note': note})
