from urllib import request
from django.shortcuts import render
from django.views import View
 

from helloapp.forms import ColorPickerForm


# Create your views here.
class ColorickerView(View):
    def get(self, request):
        form = ColorPickerForm()
        
        context = {
            'form': form,
            'red': 100,
            'green': 100,
            'blue': 100
        }
        return render(request, 'color_picker.html', context)
    
        
    def post(self, request):
        form = ColorPickerForm(request.POST)
        
        red = request.POST['red_amount']
        green = request.POST['green_amount']
        blue = request.POST['blue_amount']
        
        context = {
            'form': form,
            'red': red,
            'green': green,
            'blue': blue,
        }
        print(request)
        return render(request, 'color_picker.html', context)

