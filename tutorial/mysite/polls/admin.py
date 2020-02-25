from django.contrib import admin
from . import models

"""This is ordinary admin register"""
# admin.site.register([models.Question, models.Choice])


"""changing the Question model column order in admin"""
# class QuestionField(admin.ModelAdmin):
#     fields = ['publication_date', 'question_text']
# admin.site.register(models.Question, QuestionField)

"""Inline model"""

""" Stacked Inline takes much place"""
# class ChoiceStackedInline(admin.StackedInline):
class ChoiceTabularInline(admin.TabularInline):
    model = models.Choice
    extra = 1  # default value will be 3


""" create field set category """
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('calender', {'fields': ['publication_date']}),
        ('question text', {'fields': ['question_text']})
    ]
    inlines = [ChoiceTabularInline]
    list_display = ['question_text', 'publication_date', 'was_published_recently']
    list_filter = ['publication_date']
    search_fields = ['publication_date', 'question_text']


admin.site.register(models.Question, QuestionAdmin)
admin.site.register([models.Publication, models.Article, models.Student, models.Blog, models.Entry, models.Author])
