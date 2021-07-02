from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from tensorflow.keras.models import load_model
import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from django.template.context_processors import csrf
from datetime import date
import requests
import pandas as pd
def home(request):
    c = {}
    c.update(csrf(request))
    return render(request,'index.html',c)
def model_predict(image_path,model):
    image = load_img(image_path,target_size=(224,224))
    image = img_to_array(image)
    image = image/255
    image = np.expand_dims(image,axis=0)
    result = np.argmax(model.predict(image))
    return result
def weather(city,request):
    url = 'http://api.openweathermap.org/data/2.5/weather?zip={},in&appid=""
    r = requests.get(url.format(city)).json()
    city_weather = [
        r["main"]["temp"],
        r["weather"][0]["main"],
        r["weather"][0]["description"],
        r["main"]["humidity"]
    ]
    return city_weather
def output(crop,soil,temp,cond):
    t = date.today().month
    data=pd.read_csv(".\static\Book1.csv")
    a=int(data[data['Crop']==crop.lower()].index.values)
    if (t>=data['month1'][a]) and (t<=data['month2'][a]):
        if soil in list(data['soil'][a].split(',')):
            if temp>(data['temp2'][a]):
                if ((cond!="rain") and (cond!="clouds")):
                    d=((temp-data['temp2'][a]))/10
                    if soil=='clay':
                        return ((data['water'][a])*1.5)+d
                    elif soil=="black":
                        return ((data['water'][a])*0.9)+d
                    elif soil=="red":
                        return ((data['water'][a])*1.1)+d
                    else:
                        return (data['water'][a])+d
                else:
                    return 1
            else:
                if ((cond!="rain") and (cond!="clouds")):
                    d=((temp-data['temp2'][a]))/10
                    if soil=='clay':
                        return ((data['water'][a])*1.5)+d
                    elif soil=="black":
                        return ((data['water'][a])*0.9)+d
                    elif soil=="red":
                        return ((data['water'][a])*1.1)+d
                    else:
                        return (data['water'][a])+d
                else:
                    return 1
        else:
            return 2
    else:
            return 0
def result(request):
    if request.method == 'POST':    
        c = {}
        c.update(csrf(request))
        f=request.FILES['image']
        fs=FileSystemStorage()
        file=fs.save(f.name,f)
        path1=fs.url(file)
        path='.'+path1
        print(path)
        crops=str(request.POST['crops'])
        city=str(request.POST['city'])
        city_weather=weather(city,request)
        #file_url = default_storage.url(file_name_2)
        model = load_model('.\models\SoilNet_93_86.h5')
        result=model_predict(path,model)
        r={0:"alluvial",1:"black",2:"red",3:"clay"}
        temp = float(city_weather[0])-273.15
        s=output(crops,r[result],temp,(city_weather[1]).lower())
        if not ((s==0) or (s==1) or (s==2)):
            s=round(s,3)
        context={'c':c,'crop':s,'soil':r[result],'plant':crops.upper(),'temp':round(temp,2),
                'des':city_weather[2],'hum':city_weather[3]}
        return render(request,'Black.html',context)
