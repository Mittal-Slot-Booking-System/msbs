from django.shortcuts import render,HttpResponse
from .models import FileUp
# Create your views here.
def index(request):
    if request.method =="POST":
        file2 = request.FILES["file"]
        document=FileUp.objects.create(file=file2)
        document.save()
        return HttpResponse("your file is saved")
    return render(request, 'index.html')