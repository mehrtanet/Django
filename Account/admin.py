from Blog.admin import CommentshipInline , MembershipInline
from django.contrib.auth.models import Group 
from django.contrib import admin
from .models import Profile
admin.site.unregister(Group)



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['get_full_name','phone', 'n_code', 'gender','is_writer', 'get_date']
    list_filter = ['m_time', 'gender', 'is_writer']
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'phone', 'n_code' ]
    ordering = ['user__last_name', 'user__first_name', 'age']
    sortable_by = ['phone', 'n_code']
    list_editable = ['phone', 'n_code', 'gender', 'is_writer']
    inlines = [MembershipInline, CommentshipInline]






