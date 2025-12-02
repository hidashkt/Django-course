from django.shortcuts import render
from .models  import MovieInfo,Directors
from .forms import MovieForm
from django.shortcuts import redirect


# Create your views here.

def create(request):
    if request.POST:
         form=MovieForm(request.POST,request.FILES)
         if form.is_valid:
              form.save()
    else:
         form=MovieForm 
    return render(request,'create.html',{'form':form})

def list(request):
        
        movie_set=MovieInfo.objects.all()
        return render(request,'list.html',{'movies':movie_set})
        
               

def edit(request,pk):
    instance_to_be_edited=MovieInfo.objects.get(pk=pk)
    if request.POST:
          frm=MovieForm(request.POST,instance=instance_to_be_edited)

          if frm.is_valid():
                instance_to_be_edited.save()
                
    else:
                frm=MovieForm(instance=instance_to_be_edited)
    
    return render(request,'create.html',{'form':frm})

def delete(request,pk):
        instance=MovieInfo.objects.get(pk=pk)
        instance.delete()
        movie_set=MovieInfo.objects.all()
        return render(request,'list.html',{'movies':movie_set})