from django.shortcuts import render
from django.http import HttpResponse
import pyqrcode
import os
import random
from structure import *
# Create your views here.
APP_DIR = os.path.dirname(__file__) 

def namesFiles():
    chif = [1,2,3,4,5,6,7,8,9,0]
    lettr = ['a','A','b','B','c','C','d','D','e','E']
    chaine = ""
    for i in range(6):
        chx = random.randrange(0,9,3)
        chaine+= str(chif[chx])
        chaine+= str(lettr[(chx+3)%10])

    return chaine

def qrcode(request):
	nom_image = namesFiles()+".png"
	request.session['qr'] = nom_image
	big_code = pyqrcode.create('http://localhost:8080/presence', error='L', version=27, mode='binary')
	big_code.png(os.path.join(APP_DIR,'static','qr',nom_image), scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
	return render(request,'index.html',{'img':nom_image})

def presence(request):
	pp = presenceProf(img_qr=request.session['qr'],nom_prof = "Lys Pierre")
	pp.save()

	return HttpResponse("<p>Presence du professeur effectue! <a href='/generate'>Accueil</a></p>")

