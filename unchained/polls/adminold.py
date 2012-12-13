from polls.models import Poll
from polls.models import Choice
from django.contrib import admin
class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Prompt',               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['davidCustom']}),
		('Empty Set', {'fields': []}),
    ]

admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
#Now let's register multiple choices for this poll

