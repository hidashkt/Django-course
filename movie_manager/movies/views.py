from django.shortcuts import render

# Create your views here.

def create(request):
    if request.POST:
        print(request.POST.get('title'))
        print(request.POST.get('year'))
        print(request.POST.get('summary'))

    return render(request,'create.html')

def list(request):
        
        movie_data={
        'movies':[
            {
                'title':'thalavara',
                'year':2025,
                'summary':'A movie of arjun ashokan',
                'img':'thaalvara.jpg'
               
            },
            {
                'title':'Lokah chapter Chandra',
                'year':2025,
                'summary':'A movie of superpowers',
                'img':'lokah.jpg'
                
            },
            {
                'title':'Ponman',
                'year':2024,
                'summary':'A movie of debts',
               
            },
            {
                'title':'Dude',
                'year':2025,
                
                
            },
            {
                'title':'Banglore Days',
                'year':2019,
                'summary':'A good movie',
                
            },
            {
                'title':'padakkalam',
                'year':2025,
                'summary':'A movie of past game chaturanga and its curse',
                'img':'padakkalam.jpg'
                
            },
        ]

    }
        return render(request,'list.html',movie_data)
        
               

def edit(request):
    return render(request,'edit.html')