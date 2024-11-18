from rest_framework.decorators import api_view
from rest_framework.response import Response
from library.models import Person
from library.serializers import PersonSerializer

@api_view(['GET','POST','PUT'])
def index(request):
    courses={
            'course_name':'python',
            'learn':['Django','Flask','Fastapi'],
            'course_provider':'scaler'
        }
    if request.method == 'GET':
        print('GET')
        return Response(courses)

    elif request.method == 'POST':
        data = request.data
        print("data==================",data)
        print('POST')
        return Response(courses)
    elif request.method == 'PUT':
        print('PUT')
        return Response(courses)

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def person(request):
    if request.method == 'GET':
        objs =Person.objects.all()
        serializer= PersonSerializer(objs,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':  
        data =request.data
        serializer = PersonSerializer(data = data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'PUT':  
        data =request.data
        obj = Person.objects.get(id=data['id'])
        serializer = PersonSerializer(obj,data = data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'PATCH':  
        data =request.data
        obj = Person.objects.get(id=data['id'])
        serializer = PersonSerializer(obj,data = data,partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    else:
        data =request.data
        obj = Person.objects.get(id=data['id'])
        obj.delete()
        return Response({'message':'Person deleted'})