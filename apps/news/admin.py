from django import forms
from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin

from news.models import NewsPost, WhatWeAreReading


class WhatWeAreReadingInline(admin.StackedInline):
    model = NewsPost.reading_links.through

# class AuthorAdmin(admin.ModelAdmin):
#     inlines = [ WhatWeAreReadingInline, ]

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

# https://stackoverflow.com/questions/30472741/inlinemodeladmin-not-showing-up-on-admin-page
# https://stackoverflow.com/questions/40153093/django-admin-tabular-inline-add-more-not-showing
class NewsPostAdmin(SummernoteModelAdmin):
    inlines = [WhatWeAreReadingInline,]
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
#         'source',
#         'link',
#         'published_date',
#     ]

# class WhatWeAreReadingAdmin(SummernoteModelAdmin):
#     form = WhatWeAreReadingPost
#     list_display = ['title']
#     list_editable = ['title', 'source', 'link', 'published_date',]

# admin.site.register(WhatWeAreReadingPost, WhatWeAreReadingAdmin)
