from django.shortcuts import render
from .forms import ProductionForm
import numpy as np

def index(request):
    result = None
    if request.method == "POST":
        form = ProductionForm(request.POST)
        if form.is_valid():
            # 入力値取得
            price = form.cleaned_data['price']
            time_per_unit = form.cleaned_data['time_per_unit']
            threshold_hours = form.cleaned_data['threshold_hours']
            income = form.cleaned_data['income']
            working_days = form.cleaned_data['working_days']
            life_loss_per_hour = form.cleaned_data['life_loss_per_hour']
            max_hours = form.cleaned_data['max_hours']

            # 1時間あたりの寿命価値
            life_value = income / 2080  # 1年間の労働時間を2080時間と仮定

            # 可能な生産数の範囲
            x_range = np.arange(0, (max_hours / time_per_unit) + 1, 1)

            best_x = 0
            max_revenue = float('-inf')

            for x in x_range:
                H = x * time_per_unit  # 総労働時間
                life_loss = max(0, H - threshold_hours) * life_loss_per_hour
                cost_of_life_loss = life_loss * life_value
                revenue = x * price - cost_of_life_loss  # 売上（超過労働による寿命損失を引く）

                if revenue > max_revenue:
                    max_revenue = revenue
                    best_x = x

            # 月の売上
            monthly_revenue = best_x * price * working_days - cost_of_life_loss * working_days

            result = {
                'x_opt': round(best_x),
                'daily_revenue': round(max_revenue/100)*100,
                'monthly_revenue': round(monthly_revenue/100)*100
            }
    else:
        form = ProductionForm()

    return render(request, "index.html", {"form": form, "result": result})




