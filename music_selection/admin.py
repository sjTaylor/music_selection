from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import ResponseType, Response, User, Section, SongSuggestion, Concert, SongJudgement
from .forms import CustomUserChangeForm, CustomUserCreationForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['username', 'section']
    fieldsets = UserAdmin.fieldsets + (
        ('Music Stuff', {'fields': ('section',)}),
    )


admin.site.register(User, CustomUserAdmin)
admin.site.register(ResponseType)
admin.site.register(Response)
admin.site.register(Section)
admin.site.register(SongSuggestion)
admin.site.register(Concert)
admin.site.register(SongJudgement)
