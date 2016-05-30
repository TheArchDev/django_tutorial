from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    # inclusion of associated Choice object entries
    inlines = [ChoiceInline]

    # determines column headers in 'change list' page
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # filter sidebar by publication date
    list_filter = ['pub_date']
    # search capability
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
