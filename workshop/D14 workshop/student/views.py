from django.shortcuts import render

# Create your views here.
index = { '정운지': 26, '박수현': 27, '김준석': 27, '김호영': 26, '강민수': 29, '김예랑': 26, '박성주': 30 }
 
def info(request):
    name = index.keys()
    return render(request, 'info.html', {'name': name})
    
def student_detail(request, st_name):
    name = st_name
    age = index.get(st_name)
    return render(request, 'student_detail.html', {'name': name, 'age': age})