from django import forms

from .models import Customer


class RegisterCustomerAPIForm(forms.ModelForm):
    """顧客登録APIのバリデーションForm"""

    class Meta:
        model = Customer
        fields = ('name', 'email', 'age')


class RegisterCustomerAndLogAPIForm(forms.ModelForm):
    """顧客登録+初回訪問記録登録APIのバリデーションForm"""

    note = forms.CharField()
    amount = forms.IntegerField()

    class Meta:
        model = Customer
        fields = ('name', 'email', 'age')
