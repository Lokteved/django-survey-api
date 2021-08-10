from django.contrib import admin

from .models import Answer, Respondent, SurveyResponse, Survey, Question


class SurveyQuestionInline(admin.StackedInline):
    model = Question


class ResponseAnswerInline(admin.StackedInline):
    model = Answer


class SurveyResponseAdmin(admin.ModelAdmin):
    inlines = (ResponseAnswerInline, )


class SurveyAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')
    inlines = (SurveyQuestionInline, )


admin.site.register(Survey, SurveyAdmin)
admin.site.register(SurveyResponse, SurveyResponseAdmin)
admin.site.register(Respondent)
