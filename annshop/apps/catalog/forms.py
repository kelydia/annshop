# encoding: utf-8
from django import forms
from .models import Product


class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = []

    # 为admin模型字段添加自定义验证
    def clean_price(self):
        if self.cleaned_data['price'] <= 0:
            raise forms.ValidationError('价格必须大于0')
        return self.cleaned_data['price']
