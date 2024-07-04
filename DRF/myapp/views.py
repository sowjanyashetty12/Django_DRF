from django.shortcuts import render 
from django.http import JsonResponse
from .models import Drinks
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status

@api_view(['GET',"POST"])
def drinklist(request):
    if request.method=="GET":
    #get all drinks
    #serialize them
    #return json
        drink_list=Drinks.objects.all()
        serializeddata=DrinkSerializer(drink_list,many=True)
        # return JsonResponse(serializeddata.data , safe=False)
        return JsonResponse({"drinks":serializeddata.data} )
    if request.method=='POST':
        #take data from request
        #serialize them and save serialized data
        datatoserialize=request.data
        serializeddata=DrinkSerializer(data=datatoserialize)
        if serializeddata.is_valid():
            serializeddata.save()
            return Response(serializeddata.data)
@api_view(['GET','PUT','DELETE'])
def get_drink(request,id):
    try:
        drink = Drinks.objects.get(pk=id)
    except Drinks.DoesNotExist:
        return Response({'error': 'Drink not found'}, status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        drink=Drinks.objects.get(pk=id)
        serializeddata=DrinkSerializer(drink)
        return Response(serializeddata.data)
    elif request.method=="PUT":
        datatoadd=request.data 
        serializeddata=DrinkSerializer(drink,data=datatoadd)
        if serializeddata.is_valid():
            serializeddata.save()
            return Response(serializeddata.data)   
        return Response(serializeddata.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="DELETE":
        drink.delete()
        return Response( status=status.HTTP_204_NO_CONTENT)
