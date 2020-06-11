from django.shortcuts import render

# Create your views here.


def schedule(request):
    datas = {
        
    }
    return render(request, 'schedule.html', datas)



def speakers(request):
    datas = {
        
    }
    return render(request, 'speakers.html', datas)

def tickets(request):
    datas = {
        
    }
    return render(request, 'tickets.html', datas)
