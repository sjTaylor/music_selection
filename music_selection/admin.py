from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import VerdictType, VerdictReason, User, Section
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
admin.site.register(VerdictType)
admin.site.register(VerdictReason)
admin.site.register(Section)
