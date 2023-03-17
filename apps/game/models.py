from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse


class Room(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse("game:room", kwargs={"pk": self.pk})


# Create your models here.
class Word(models.Model):
    word = models.CharField(max_length=100, unique=True)
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    # created_at =

    def __str__(self) -> str:
        return f"{self.word}"

    __repr__ = __str__

    def clean(self):
        # Don't allow draft entries to have a pub_date.
        if not (self.word.isalpha()) or self.word is None:
            raise ValidationError("Enter right word!")
        if self.word.find("ь") != -1 or self.word.find("ъ") != -1 or self.word.find("ы") != -1:
            raise ValidationError("Enter right word without ь or ъ or ы!")
        last_word = Word.objects.filter(room_id=self.room_id).order_by("-pk").first()
        if last_word is not None and last_word.word[-1] != self.word[0]:
            raise ValidationError(f'Enter word begin with "{last_word.word[-1]}"')
