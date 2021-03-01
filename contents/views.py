from django.shortcuts import render
# クラスベースビューを使えば、簡単にmodelからデータを取得してtemplateに埋め込める
from django.views import generic
from django.shortcuts import get_object_or_404

from .models import Content

class IndexView(generic.TemplateView):
    template_name = 'contents/index.html'

    def get_context_data(self, **kwargs):
        self.pk = get_object_or_404(Content, pk=self.kwargs['pk'])
        context = super().get_context_data(**kwargs)
        context['content'] = self.pk

        # その他シリーズ作品
        if(self.pk.series):
            context['series'] = Content.objects.exclude(pk=self.pk.pk).filter(series=self.pk.series)
        return context