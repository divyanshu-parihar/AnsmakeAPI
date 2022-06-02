
import json
from django.http import JsonResponse
from django.shortcuts import render
from .models import Task
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt   
# Create your views here.
def ListAllTasks(request):
    query = Task.objects.all()
    queryList = serialize('json',query)
    queryList=json.loads(queryList)
    result = []

    for el in queryList:
        result.append({"id":el['pk'],'name':el['fields']['name'],'description':el['fields']['desc'],'email':el['fields']['email'],'createdAt':el['fields']['created_at']})

    return JsonResponse({'data':result},safe=False)

@csrf_exempt
def AddTask(request):
    if(request.method == "POST"):
        name = request.POST.get('name')
        desc = request.POST.get('description')
        email = request.POST.get('email') 
        if(name == None or desc == None or email == None):
            return JsonResponse({'response':"Invalid Fields"})
        try:
            task = Task(name=name,desc= desc,email = email)
            task.save()
            return JsonResponse({"response":"Task Added "})
        except:
            return JsonResponse({"response":"Database Failure"})
    else:
        return JsonResponse({"response":"Use Post request"})