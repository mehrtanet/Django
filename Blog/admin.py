from .models import Post, Comment
from django.contrib import admin 

#we need use MembershipInline ,becuse we have field(author) with manytomany relationship.
class MembershipInline(admin.TabularInline):
    model = Post.author.through
    extra = 3


class CommentshipInline(admin.TabularInline):
    model = Comment
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['get_image', 'title', 'state', 'category', 'get_edit_date', 'get_date']
    list_filter = ['state', 'category', 'author', 'm_time']
    search_fields = ['title', 'u_des', 'co_des'] 
    list_editable = ['title', 'state', 'category']
    inlines = [MembershipInline, CommentshipInline]
    exclude = ('author',) #forMembershipInline
    
  
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'user', 'state', 'get_date']
    list_filter = ['state', 'm_time']
    search_fields = ['post__title', 'user__user__first_name','user__user__last_name']
    list_editable = ['state']
    readonly_fields = ['post', 'user', 'message']
    


 
  



