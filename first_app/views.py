from django.shortcuts import render

# Create your views here.
clicked = 0

def index(request) : # 'request' name is convention. It can be some other name too.

    global clicked
    clicked = clicked + 1
    my_dict = { 'inject_var' : "You visited this page {} times.".format(clicked)}
    evenOrOdd = clicked % 2
    my_dict['evenOrOdd'] = evenOrOdd
    fruitList = ['Mango', 'Banana',  'Apple','Gauva']
    my_dict['fruits'] = fruitList
    return render(request,'index.html',context=my_dict)



def help(request) : # 'request' name is convention. It can be some other name too.
    return render(request,'help.html')