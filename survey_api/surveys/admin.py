from django.contrib import admin
from django.db import models

from .models import Answer, Respondent, Response, Survey, Question


class SurveyQuestionInline(admin.StackedInline):
    model = Question


class ResponseAnswerInline(admin.StackedInline):
    model = Answer


class ResponseAdmin(admin.ModelAdmin):
    inlines = (ResponseAnswerInline, )


class SurveyAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')
    inlines = (SurveyQuestionInline, )


admin.site.register(Survey, SurveyAdmin)
admin.site.register(Response, ResponseAdmin)
admin.site.register(Respondent)
