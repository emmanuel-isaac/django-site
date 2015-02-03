from django.contrib import admin

from polls.models import Question
from polls.models import Choice

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
  fieldsets = [
	  (None, 				{'fields': ['question_text']}),
	  ('Date information', 	{'fields': ['pub_date']})
  ]

  list_display = ('question_text', 'pub_date')

  list_filter = ['pub_date']

  search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
