from django.shortcuts import render
from .models  import MovieInfo,Directors
from .forms import MovieForm

# Create your views here.

def create(request):
    form=MovieForm()
    if request.POST:
         form=MovieForm(request.POST)
         if form.is_valid:
              form.save()
    else:
         form=MovieForm 
    return render(request,'create.html',{'form':form})

def list(request):
        
        movie_set=MovieInfo.objects.all()
        return render(request,'list.html',{'movies':movie_set})
        
               

def edit(request):
    return render(request,'edit.html')