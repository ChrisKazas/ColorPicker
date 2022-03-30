from django import forms


# 
class ColorPickerForm(forms.Form):
    red_amount = forms.IntegerField(label="Red Value", min_value=0, max_value=255, required='true')
    blue_amount = forms.IntegerField(label="Blue Value", min_value=0, max_value=255, required='true')
    green_amount = forms.IntegerField(label="Green Value", min_value=0, max_value=255, required='true')
    
    
    
    
    
    
    
    
    