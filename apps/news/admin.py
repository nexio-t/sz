from django import forms
from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin

from news.models import NewsPost, WhatWeAreReading


class WhatWeAreReadingInline(admin.StackedInline):
    model = NewsPost.reading_links.through
    max_num = 3

class NewsPostForm(forms.ModelForm):
    model = NewsPost
    fields = [
        'title',
        'body',
        'source',
        'is_cover_story',
        'publish_date',
        'topics',
        'active',
    ]
    class Meta:
        widgets = {'reading_links': forms.HiddenInput()}

class NewsPostAdmin(SummernoteModelAdmin):
    inlines = [WhatWeAreReadingInline,]
    form = NewsPostForm
    list_display = ['title', 'site', 'is_cover_story', 'active', 'has_topics']
    list_editable = ['is_cover_story', 'active']
    readonly_fields = ['site', ]
    summernote_fields = ['body', ]
    

admin.site.register(NewsPost, NewsPostAdmin)
admin.site.register(WhatWeAreReading)