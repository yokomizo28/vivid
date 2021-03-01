from django import forms
from .models import Genre, Tag, Service
# from .widgets import CustomCheckboxSelectMultiple

class SearchForm(forms.Form):
    # title = forms.CharField(
    #     label='タイトル',
    #     required=False,
    # )

    #コンテンツ検索フォーム
    genres = forms.ModelMultipleChoiceField(
        required=False,#未選択を許可
        queryset=Genre.objects.order_by('pk'),
        widget=forms.CheckboxSelectMultiple(),
    )

    services = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Service.objects.order_by('pk'),
        widget=forms.CheckboxSelectMultiple(),
    )

    tags = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Tag.objects.order_by('pk'),
        widget=forms.CheckboxSelectMultiple(),
    )

