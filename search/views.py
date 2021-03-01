from django.shortcuts import render
from django.db.models import Q
from django.views import generic

from .forms import SearchForm
from .models import Content

# 必要に応じて
# フォームコンポーネントにフォーム処理の依頼
# モデルコンポーネントにデータベース処理の依頼
# テンプレートコンポーネントにhtmlの生成を依頼
# 遷移先を判断し、ルーティングに処理を移譲


# コンテンツ一覧を表示
class IndexView(generic.ListView):
    model = Content
    template_name = 'search/index.html'

    # テンプレートにformを渡す
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = SearchForm(self.request.GET or None)
        return context

    # タグの選択に応じて結果を表示
    def get_queryset(self):
        queryset = super().get_queryset()
        self.form = form = SearchForm(self.request.GET or None)
        if form.is_valid():
            genres = form.cleaned_data.get('genres')
            services = form.cleaned_data.get('services')
            tags = form.cleaned_data.get('tags')
            # title = form.cleaned_data.get('title')
            if genres:
                for genre in genres:
                    queryset = queryset.filter(genres=genre)
            if services:
                for service in services:
                    queryset = queryset.filter(services=service)
            if tags:
                for tag in tags:
                    queryset = queryset.filter(tags=tag)
            # if title:
            #     for word in title.split():
            #         queryset = queryset.filter(Q(title__icontains=word))
            queryset = queryset.order_by('?') \
                .prefetch_related('genres')\
                .prefetch_related('services')\
                .prefetch_related('tags')
        # 項目未選択時はlistを表示しない
        else:
            queryset = queryset.none()
        # count = queryset.count()
        return queryset


