# ルートのURLconf,ここから各アプリのurlsモジュールに向ける
# django.urls から、他のURLconfを参照する為のinclude()のインポートを追加
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

# include()
# Djangoがinclude()にたどり着いたら、
# そのポイントまでに一致したURLの部分を除き、残りの文字列をincludeされたURLconfに渡す
urlpatterns = [
    # urlpatternをincludeするときはinclude()を使う
    # admin.site.urlsは例外

    # path()
    # 第一引数：urlとマッチング
    # 第二引数：処理の引き渡し先
    path('admin/', admin.site.urls),

    # ルートのURLconfでは基本的に他のURLconfを参照するのでinclude()で参照
    # topアプリのURLconfを参照
    path('vivid/', include('top.urls')),
    path('vivid/search/',include('search.urls')),
    path('vivid/contents/',include('contents.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
