from django.forms import ModelForm

from apps.game.models import Room


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ["name"]
