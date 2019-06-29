from django.db import models
from django.contrib.auth.models import AbstractUser


class Instrumentation(models.Model):
    instrumentation = models.CharField(max_length=200, unique=True)


class SongSuggestion(models.Model):

    song_name = models.CharField(max_length=40)
    composer = models.CharField(max_length=400)
    series = models.CharField(max_length=40)
    instrumentation = models.ForeignKey(Instrumentation, on_delete=models.CASCADE)
    link = models.CharField(max_length=400)
    medley_song_links = models.CharField(max_length=4000)
    sheet_music_link = models.CharField(max_length=400)
    suggestion_time = models.DateField(verbose_name="Most recent date song was suggested")


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
        ("YES", "Yes"),
        ("MAYBE", "Maybe"),
        ("NO", "No"),
        ("N/A", "N/A"),
    ]
    decision = models.CharField(max_length=10, choices=VERDICT_CHOICES, unique=True)
    # ranking = models.IntegerField(verbose_name="A rating of how positive the verdict is?")

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


class SuggestionDecision(models.Model):
    DECISION_TYPES = [
        ("PUNT", "Delay Decision"),
        ("NEXT", "Next Semester"),
        ("ACCEPT", "Accept"),
        ("REJECT", "Reject"),
        ("UNK", "In Progress")
    ]
    SEMESTER_TYPES = [
        ("F", "Fall"),
        ("S", "Spring")
    ]
    decision = models.CharField(max_length=10, choices=DECISION_TYPES)
    semester = models.CharField(max_length=10, choices=SEMESTER_TYPES)
    year = models.IntegerField()
    comments = models.CharField(max_length=1000)
    suggestion = models.ForeignKey(SongSuggestion, on_delete=models.CASCADE)

