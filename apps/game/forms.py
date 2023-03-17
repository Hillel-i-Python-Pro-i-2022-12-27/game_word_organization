from django.forms import (
    ModelForm,
    # CharField,
    # HiddenInput,
)

from apps.game.models import Room, Word


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ["name"]


class WordForm(ModelForm):
    class Meta:
        model = Word
        fields = ("word",)
