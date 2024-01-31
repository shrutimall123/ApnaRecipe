from django.shortcuts import render,redirect
from recipes.models import recipe
from django.views.generic import TemplateView

# Create your views here.


class Home(TemplateView):
    context = {}
    template_name = 'home/home.html'

    def get(self, request, *args, **kwargs):
        user = request.user.id
        if user:
            return redirect('userhome')
        data = recipe.objects.all()
        self.context['data'] = data
        return render(request,self.template_name , self.context)
    
    
def dynamic_home(request):
        context = {
        'message': 'Welcome to the dynamic home page!',
        # Add other dynamic data as needed
        }
        return render(request, 'your_app/home.html', context)
    

def services(request):
    return render(request, 'home/services.html') 

def contactus(request):
    return render(request,'home/contactus.html')

def gallery(request):
     return render(request,'home/gallery.html')
