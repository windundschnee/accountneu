from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from .models import Recipe, Ingredient, Instruction


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        exclude=[]



InstructionFormSet = inlineformset_factory(Recipe, Instruction, form=RecipeForm, extra=3, can_delete=True)
