from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):

    context = {
        'variable1':"Kapil is hustler",
        'variable2':"Kapil make something unique"
    }
    return render(request, 'index.html', context)
    # return HttpResponse("This is homepage")

def about(request):
    return render(request, 'about.html',)
    #  return HttpResponse("This is about page") 

def services(request):
    return render(request, 'services.html', )
    # return HttpResponse("This is services page") 

def contact(request):
    return render(request, 'contact.html', )
    # return HttpResponse("This is contact page") 