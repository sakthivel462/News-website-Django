from django.contrib import admin

# Register your models here.
from .models import News,Tag,Review,Magazine,MagazineSubscriber


admin.site.register(News)
admin.site.register(Tag)
admin.site.register(Review)
@admin.register(Magazine)
class MagazineAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_date']  # Shows these columns in admin list

@admin.register(MagazineSubscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['email', 'subscribed_at']