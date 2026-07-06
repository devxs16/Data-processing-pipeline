from django.shortcuts import render
import pandas as pd

def home(request):

    df = pd.read_csv("../cleaned_transactions.csv")

    context = {
        "filename": "cleaned_transactions.csv",
        "rows": len(df),
        "columns": len(df.columns),
    }

    return render(request, "dashboard/home.html", context)


def process(request):

    file = request.GET.get("file")

    if not file:
        file = "transactions.xlsx"

    return render(request, "dashboard/process.html", {"file": file})