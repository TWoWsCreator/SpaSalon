from django.contrib import admin

from reviews.models import Reviews

@ admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_published', 'name', 'review_text', 'rating')
    list_editable = ('is_published',)