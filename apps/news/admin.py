from django import forms
from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin

from news.models import NewsPost, WhatWeAreReading


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


class NewsPostAdmin(SummernoteModelAdmin):
    form = NewsPostForm
    list_display = ['title', 'site', 'is_cover_story', 'active', 'has_topics']
    list_editable = ['is_cover_story', 'active']
    readonly_fields = ['site', ]
    summernote_fields = ['body', ]

admin.site.register(NewsPost, NewsPostAdmin)


admin.site.register(WhatWeAreReading)


# class WhatWeAreReadingPost(forms.ModelForm):
#     model = WhatWeAreReading
#     fields = [
#         'title',
#         'body',
#         'source',
#         'published_date',
#     ]

# class WhatWeAreReadingAdmin(SummernoteModelAdmin):
#     form = WhatWeAreReadingPost
#     list_display = ['title']
#     list_editable = ['title', 'body', 'source', 'published_date',]

# admin.site.register(WhatWeAreReadingPost, WhatWeAreReadingAdmin)
