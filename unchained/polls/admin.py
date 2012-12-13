from polls.models import Poll
from polls.models import Choice
from django.contrib import admin

#can be stacked or tabular (tabular is more horizontal space)
class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 4
	
class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
	#this is for what information is displayed when viewing all polls
    list_display = ('question', 'pub_date')
	#this shows a popup filter that allows you to sort by published aate
    list_filter = ['pub_date']
    #search fields (it will query all of these using a LIKE command, and you can specify several
    search_fields = ['question']

	
admin.site.register(Poll, PollAdmin)
#admin.site.register(Choice)
#Now let's register multiple choices for this poll

