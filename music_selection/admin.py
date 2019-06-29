from django.contrib import admin

from .models import VerdictType, VerdictReason, User, Section

admin.site.register(VerdictType)
admin.site.register(VerdictReason)
admin.site.register(User)
admin.site.register(Section)
