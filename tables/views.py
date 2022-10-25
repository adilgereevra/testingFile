from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Model2 #, Trends, Events, Scenario
 
# получение данных из бд
def index(request):
    model1 = Model2.objects.all()
    # trend = Trends.objects.all()
    # event = Events.objects.all()
    # scenario = Scenario.objects.all()
    
    return render(request, "tables.html", {"Models": model1})#, {"Events": event}, {"Trends": trend},{"Scenario": scenario})
    
 
# сохранение данных в бд
def create(request):
    if request.method == "POST":
        model_cr = Model2()
        model_cr.model_name = request.POST.get("Model name")
        model_cr.model_location = request.POST.get("Model location")
        model_cr.model_file_name = request.POST.get("Model file name")
        model_cr.description = request.POST.get("Model description")
        model_cr.save()
    return HttpResponseRedirect("/")
 
# изменение данных в бд
def edit(request, id):
    try:
        model_ed = Model2.objects.get(id=id)
 
        if request.method == "POST":
            model_ed.model_name = request.POST.get("Model name")
            model_ed.model_location = request.POST.get("Model location")
            model_ed.model_file_name = request.POST.get("Model file name")
            model_ed.description = request.POST.get("Model description")
            model_ed.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"Model": model_ed})
    except Model2.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")
     
# удаление данных из бд
def delete(request, id):
    try:
        model_del = Model2.objects.get(id=id)
        model_del.delete()
        return HttpResponseRedirect("/")
    except Model2.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")