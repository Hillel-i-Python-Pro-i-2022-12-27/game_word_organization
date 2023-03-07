from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView

from apps.game.models import Word, Room


class WordListView(ListView):
    model = Word


def index(request):
    return render(
        request=request,
        template_name="index.html",
    )


class RoomListView(ListView):
    model = Room
    queryset = Room.objects.all()


class RoomView(TemplateView):
    model = Word
    success_url = reverse_lazy("game:list")
    template_name = "game/word_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        room_id = context["pk"]

        room = Room.objects.filter(pk=room_id).get()
        context["title"] = room.name
        words = room.word_set.all()
        # words = Word.objects.all()
        context["words"] = words

        return context


class WordCreateView(CreateView):
    model = Word

    fields = ("word",)
    success_url = reverse_lazy("game:create")


class RoomCreate(CreateView):
    # form_class = RoomForm
    model = Room
    template_name = "game/room_create.html"
    fields = ("name",)
    success_url = reverse_lazy("game:list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["name"] =
        return context


# def create(request):
#     if request.method == "POST":
#         form = RoomForm(request.POST)
#     if form.is_valid():
#         form.save()
#         return redirect("game:list")
#     else:
#         form = RoomForm()
#
#         return render(request, "game/room_create.html", {"form": form})
