from django.contrib import admin

# Register your models here.
from .models import Category,Tag,Service,Content,Genre

class AllAdmin(admin.ModelAdmin):
    # 一覧で表示される内容  を変更
    list_display = ('id', 'name')
    # 一覧で表示される内容  を変更 ※デフォルトは作成時間(created_at)でソート
    ordering = ('id',)

# contentの見え方
class ContentAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    ordering = ('id',)


# admin.site.register(Category)に引数を1つ追加
# 第二引数に追加するクラスで管理サイトでの見え方をカスタマイズする
admin.site.register(Category, AllAdmin)
admin.site.register(Tag, AllAdmin)
admin.site.register(Service, AllAdmin)
admin.site.register(Genre, AllAdmin)
admin.site.register(Content, ContentAdmin)
