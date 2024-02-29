from django.shortcuts import render,redirect 
from django.http import HttpResponse

# Create your views here.

def sample(request):
    return HttpResponse("<H1>Hello World</H1> <br> This is Sample Page.")

def index(request):
    name = "jojo"
    age = 29
    return render(request,"index.html",{"name":name,"age":age})

def about(request):
    return render(request,"about.html")

def form(request):
    return render(request,"form.html")

def interest(request):
    return render(request,"interest.html")

def idol(request):
    return render(request,"idol.html")

def home(request):
    return render(request,"home.html")

def showMyData(request):
    stdId = '65342110269-2'
    name = 'วชิรวิทย์ ศรีสูงเนิน'
    address = '161 หมู่ 4 ต.โพนสา อ.ท่าบ่อ จ.หนองคาย'
    domicile = '161 หมู่ 4 ต.โพนสา อ.ท่าบ่อ จ.หนองคาย'
    gender = 'ชาย'
    weight = '75 กก.'
    height = '166 ซม.'
    color = 'สีฟ้า'
    food = 'หมูกระทะ'
    job = 'นักเรียนนักศึกษา'
    product = ['HONDA CBR650R', 'HONDA CB650R', 'KAWASAKI Z900', 'KAWASAKI NINJA ZX4R', 'HONDA CBR500R', 
                'HONDA CB500X', 'SUZUKI GSX-R1000 L9','KTM DUKE 690','SUZUKI GSX8S','YAMAHA R7']
    price = ['185,000','179,000','190,000','230,000','112,000','125,000','545,000','230,000','219,000','199,000']
    picture = ['cbr650r.jpg','cb650r.jpg','z900.jpg','zx4r.jpg','cbr500r.jpg','cb500x.png','gsxr.jpg','ktmduke690.jpg',
               'gsx8s.jpg','r7.png']
    products = zip(product, price, picture)
    return render(request, 'showMyData.html', {'stdId': stdId, 'name': name, 'address': address, 'domicile': domicile,
                                              'gender': gender, 'weight': weight, 'height': height,
                                              'color': color, 'food': food, 'job': job,
                                              'product': product,'price': price, 'picture': picture,'products': products})

