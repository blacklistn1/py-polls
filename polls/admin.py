from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 5


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'pub_date', 'was_published_recently']
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Publication', {'fields': ['pub_date'], 'classes': ['collapse']})
    ]
    list_filter = ['pub_date']
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
