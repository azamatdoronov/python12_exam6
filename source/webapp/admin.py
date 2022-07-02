from django.contrib import admin

from webapp.models import Guestbook


class GuestbookAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'author', 'email', 'note', 'created_nt', 'update_nt']
    list_display_links = ['note']
    list_filter = ['status']
    search_fields = ['status']
    fields = ['status', 'note', 'created_nt', 'update_nt']
    readonly_fields = ['created_nt', 'update_nt']


admin.site.register(Guestbook, GuestbookAdmin)
