from django.contrib import admin

from .models import Survey, Question, Choice


class QuestionChoiceInline(admin.StackedInline):
    model = Choice


class SurveyQuestionInline(admin.StackedInline):
    model = Question


class SurveyAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')
    inlines = (SurveyQuestionInline, )


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text')
    inlines = (QuestionChoiceInline, )


admin.site.register(Question, QuestionAdmin)
admin.site.register(Survey, SurveyAdmin)
