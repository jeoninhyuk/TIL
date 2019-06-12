from .models import Board, Comment
# Register your models here.

class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at', 'updated_at')

admin.site.register(Board, BoardAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'created_at', 'updated_at')

admin.site.register(Comment, CommentAdmin)
