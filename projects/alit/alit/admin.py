from django.contrib import admin

# Register your models here.

from .models import Question, Answer, Algoset, Comment

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

class AlgoAdmin(admin.ModelAdmin):
    search_fields = ['title']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Algoset, AlgoAdmin)
admin.site.register(Comment)