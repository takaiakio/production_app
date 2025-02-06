from django import forms

class ProductionForm(forms.Form):
    price = forms.FloatField(label="製品単価（円）", initial=3500)
    time_per_unit = forms.FloatField(label="1個あたりの作成時間（時間）", initial=2)
    threshold_hours = forms.FloatField(label="超過労働なしの最大労働時間（時間）", initial=8)
    income = forms.FloatField(label="年収（円）", initial=3000000)
    working_days = forms.IntegerField(label="1ヶ月の労働日数（日）", initial=22)
    life_loss_per_hour = forms.FloatField(label="1時間の超過労働で減る寿命（時間）", initial=1)
    max_hours = forms.FloatField(label="1日の最大労働時間（24時間以内）", initial=16)

