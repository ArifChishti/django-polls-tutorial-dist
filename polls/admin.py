from django.contrib import admin
from polls.models import Poll, Choice

# Register your models here.
class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3
class PollAdmin(admin.ModelAdmin):
#	fields = ['pub_date', 'question']
	fieldsets = [
		(None,	{'fields':['question']}),
		('Date Information', {'fields':['pub_date'], 'classes':['collapse']}),
	]
	list_display = ('question','pub_date','was_published_recently')
	inlines = [ChoiceInline]
	list_filter = ['pub_date']
	search_fields = ['question']
	

admin.site.register(Poll,PollAdmin)
#admin.site.register(Choice)
