from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, FormView

from apps.game.forms import WordForm
from apps.game.models import Word, Room

User = get_user_model()


class WordListView(ListView):
    model = Word


def index(request):
    return render(
        request=request,
        template_name="index.html",
    )


@method_decorator(login_required, name="dispatch")
class RoomListView(ListView):
    model = Room
    queryset = Room.objects.all()


@method_decorator(login_required, name="dispatch")
class RoomView(FormView):
    success_url = reverse_lazy("game:list")
    template_name = "game/word_list.html"
    form_class = WordForm

    def get_success_url(self):
        return reverse_lazy("game:room", kwargs={"pk": self.kwargs.get("pk")})

    def get_initial(self):
        initial = super().get_initial()
        room_id = self.kwargs.get("pk")
        player = self.request.user
        initial["player"] = player
        initial["room"] = room_id

        # initial["word"] = "hello world!"
        return initial

    def form_valid(self, form):
        form.instance.room_id = self.kwargs.get("pk")
        form.instance.player = self.request.user
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        room_id = self.kwargs["pk"]
        room = Room.objects.filter(pk=room_id).get()
        word_form = WordForm

        context["title"] = room.name
        words = room.word_set.all().order_by("-pk")

        context["words"] = words
        context["word_form"] = word_form

        return context


@method_decorator(login_required, name="dispatch")
class WordCreateView(CreateView):
    model = Word

    fields = ("word",)
    success_url = reverse_lazy("game:create")


@method_decorator(login_required, name="dispatch")
class RoomCreate(CreateView):
    # form_class = RoomForm
    model = Room
    template_name = "game/room_create.html"
    fields = ("name",)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["name"] =
    #     return context
