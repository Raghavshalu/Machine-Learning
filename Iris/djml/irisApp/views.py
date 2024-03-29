from django.shortcuts import render
from django.http import HttpResponse

from joblib import load
# model=load('./savedModels/model.joblib')
model=load(('./savedModels/model.joblib'))
# Create your views here.
def predictor(request):
    return render(request,'main.html')

def formInfo(request):
    sepal_length=request.GET['sepal_length']
    sepal_width=request.GET['sepal_width']
    petal_length=request.GET['petal_length']
    petal_width=request.GET['petal_width']
    y_pred=model.predict([[sepal_length,sepal_width,petal_length,petal_width]])
    if y_pred[0]==0:
        y_pred='Setosa'
    elif y_pred[0]==1:
        y_pred='verscicolor'
    else:
        y_pred='virginica'
    return render(request,'result.html',{'result':y_pred})