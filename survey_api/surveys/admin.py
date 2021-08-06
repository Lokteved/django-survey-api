from django.contrib import admin

from .models import Survey, Question


class SurveyQuestionInline(admin.StackedInline):
    model = Question


class SurveyAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')
    inlines = (SurveyQuestionInline, )


admin.site.register(Survey, SurveyAdmin)
