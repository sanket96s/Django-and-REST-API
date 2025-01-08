from django.contrib import admin
from .models import Book,User,Post,Product,Member,Boook

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','published_date')
    search_fields = ('title','author')
    list_filter = ['published_date']

admin.site.register(Book,BookAdmin)
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Product)
admin.site.register(Member)
admin.site.register(Boook)