from django.db import models
from django.contrib.auth.models import AbstractUser
from urllib.parse import urlparse, parse_qs


class Instrumentation(models.Model):
    instrumentation = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.instrumentation


class SongSuggestion(models.Model):

    link = models.CharField(max_length=400)
    song_name = models.CharField(max_length=40)
    composer = models.CharField(max_length=400)
    series = models.CharField(max_length=40)
    instrumentation = models.ForeignKey(Instrumentation, on_delete=models.CASCADE)
    medley_song_links = models.CharField(max_length=4000)
    sheet_music_link = models.CharField(max_length=400)

    def __str__(self):
        return '%s FROM %s BY %s' % (self.song_name, self.series, self.composer)

    def is_youtube_link(self):
        return 'youtube.com' in self.link or '//youtu.be' in self.link

    def get_youtube_id(self):
        if self.is_youtube_link():
            parsed_link = urlparse(self.link)
            if 'youtube.com' in self.link:
                return parse_qs(parsed_link.query)['v']
            else:
                return parsed_link.path[1:]
        else:
            return None


class Section(models.Model):
    section_name = models.CharField(max_length=50, verbose_name="Section of the band (e.g. Brass)", unique=True)
    slug = models.SlugField(max_length=20, unique=True)

    def __str__(self):
        return self.section_name


class User(AbstractUser):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.username + " (" + str(self.section) + ")"


class VerdictType(models.Model):
    VERDICT_CHOICES = [
        ("Yes", "Yes"),
        ("Maybe", "Maybe"),
        ("No", "No"),
        ("N/A", "N/A"),
    ]
    decision = models.CharField(max_length=10, choices=VERDICT_CHOICES, unique=True)

    def __str__(self):
        return self.decision


class VerdictReason(models.Model):
    verdict_type = models.ForeignKey(VerdictType, on_delete=models.CASCADE)
    short_text = models.CharField(max_length=20, verbose_name="Reason for response (e.g. Fun or un-playable)")

    def __str__(self):
        return '%s - %s' % (self.verdict_type, self.short_text)


class Verdict(models.Model):
    response = models.ForeignKey(VerdictType, on_delete=models.CASCADE)
    short_reason = models.ForeignKey(VerdictReason, on_delete=models.CASCADE)
    comments = models.CharField(max_length=5000)


class SongJudgement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    response = models.ForeignKey(Verdict, on_delete=models.CASCADE)
    song = models.ForeignKey(SongSuggestion, on_delete=models.CASCADE)


class Concert(models.Model):
    year = models.IntegerField()
    concert_label = models.SlugField(verbose_name="Label for concert (e.g. fall, a-fest, fall-electronics, etc.)",
                                     max_length=50)

    def __str__(self):
        return '%d: %s' % (self.year, self.concert_label)


class SuggestionDecision(models.Model):
    DECISION_TYPES = [
        ("Delay Decision", "Delay Decision"),
        ("Next Semester", "Next Semester"),
        ("Accept", "Accept"),
        ("Reject", "Reject"),
        ("In Progress", "In Progress"),
    ]
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE)
    suggestion = models.ForeignKey(SongSuggestion, on_delete=models.CASCADE)
    decision = models.CharField(max_length=20, choices=DECISION_TYPES, default="In Progress")
    comments = models.CharField(max_length=1000, default='')

