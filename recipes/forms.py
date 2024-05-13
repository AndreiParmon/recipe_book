from django import forms
from .models import Recipe, Category


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'cooking_steps', 'cooking_time', 'image', 'ingredients']
        widgets = {
            'cooking_steps': forms.Textarea(attrs={'rows': 6}),
        }

    category = forms.ModelChoiceField(queryset=Category.objects.all())

    def __init__(self, *args, **kwargs):
        """
         Обновление стилей формы под Bootstrap
         """
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Категория не выбрана"
