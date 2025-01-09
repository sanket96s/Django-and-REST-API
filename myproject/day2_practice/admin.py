from django.contrib import admin
from .models import Post,Book,Order,OrderItem

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','description','created_at')
    search_fields = ['title']
    list_filter = ['created_at']
    
admin.site.register(Post,PostAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ['title','author','price']
    search_fields = ['title','author']
    list_filter = ['published_date']
    
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]

admin.site.register(Book,BookAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem)