from django.contrib import admin

from .models import Choice,Question

admin.site.site_header = "Pollster Admin"
admin.site.site_title = "Pollster Admin area"
admin.site.index_title = "Welcome to Pollster Admin"

# Register your models here.

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets= [ 
        (None, {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines =[ChoiceInLine]

# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)