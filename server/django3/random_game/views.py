from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, "index.html")

def today_beer(request):
    beer_list = [
        {"name" : "에델바이스" , "scr" : "https://helpx.adobe.com/content/dam/help/en/photoshop/using/quick-actions/remove-background-after-qa1.png"},
        {"name" : "테라" , "scr" : "https://m.hitejinro.com/assets/images/brand/beer/terra/img_terra.jpg"},
        {"name" : "호가든" , "scr" : "https://img.etnews.com/photonews/2004/1296720_20200428102815_010_0001.jpg"}
    ]
    
    context = {
        "beer" : random.choice(beer_list)
    }
    
    return render(request, "today_beer.html", context)

def lotto(request):
    lotto_list = []
    
    lotto_result_list = [
        {"lotto":[1,2,3,4,5,6],"result" : "1등 - 10억"},
        {"lotto":[1,2,3,4,5,6],"result" : "1등 - 10억"},
        {"lotto":[1,2,3,4,5,6],"result" : "1등 - 10억"},
        {"lotto":[1,2,3,4,5,6],"result" : "1등 - 10억"},
        {"lotto":[1,2,3,4,5,6],"result" : "1등 - 10억"},
    ]
    
    for _ in range(5):
        lotto = random.sample(range(1,46),6)
        lotto_list.append(lotto)
    
    context ={
        "lotto_list" : lotto_list,  
    }
    
    return render(request, "lotto.html" , context)