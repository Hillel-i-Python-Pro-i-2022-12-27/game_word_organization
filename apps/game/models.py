from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.
class Word(models.Model):
    word = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return f"{self.word}"

    __repr__ = __str__

    def clean(self):
        # Don't allow draft entries to have a pub_date.
        if not (self.word.isalpha()) or self.word is None:
            raise ValidationError('Enter right word!')
        if self.word.find("ь") != -1 or self.word.find("ъ") != -1 or self.word.find("ы") != -1:
            raise ValidationError('Enter right word without ь or ъ or ы!')
        last_word = Word.objects.order_by("-pk").first()
        if last_word is not None and last_word.word[-1] != self.word[0]:
            raise ValidationError(f'Enter word begin with "{last_word.word[-1]}"')


class Room(models.Model):
    room_number = models.SmallIntegerField(max_length=100, unique=True)
    main_player = models.CharField(max_length=100, unique=True)
    other_player = models.SmallIntegerField(max_length=100, unique=True)
