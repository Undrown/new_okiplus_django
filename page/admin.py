from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Page


# Register your models here.
# Apply summernote to all TextField in model.

class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'


admin.site.register(Page, SomeModelAdmin)
