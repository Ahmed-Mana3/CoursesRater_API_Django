from django.contrib import admin
from .models import Course, Channel, Rate


class RateAdmin(admin.ModelAdmin):
    list_display = ['course', 'stars', 'user']
    search_fields = ['course', 'stars', 'user']
    list_filter = ['course', 'stars', 'user']
    

admin.site.register(Course)
admin.site.register(Channel)
admin.site.register(Rate, RateAdmin)
