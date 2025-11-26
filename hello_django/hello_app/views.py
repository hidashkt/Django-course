from django.shortcuts import render
from django.http import HttpResponse

def print_hello(request):
    movie_data={
        'movies':[
            {
                'title':'thalavara',
                'year':2025,
                'summary':'A movie of arjun ashokan',
               
            },
            {
                'title':'Lokah chapter Chandra',
                'year':2025,
                'summary':'A movie of superpowers',
                
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
                
            },
        ]

    }
    
    return render(request,'index.html',movie_data)
