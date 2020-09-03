from rest_framework import status
#from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
import math
from .models import getNumerosPrimos    

class NumerosPrimosAPI(APIView):
   
    def get(self, request, n):

        #np = getNumerosPrimos(n)
        #print(np)

        respuesta = self.Calc_Numeros_primos(n)
        if(respuesta != ""):
            return Response(respuesta,status=status.HTTP_200_OK)
        else:
            return Response("Sin Respuesta del servidor",status=status.HTTP_400_BAD_REQUEST)

    def Calc_Numeros_primos(self, n):
        x = []
        for numero in range(2, n):
            if all(numero % i != 0 for i in range(2, int(math.sqrt(numero))+1)):
                x.append(numero)
        return x

class NumerosPrimosGemelosAPI(APIView):

    def get(self, request, n):
        respuesta = self.Calc_Num_Primos_gem(n)
        if(respuesta != ""):
            return Response(respuesta,status=status.HTTP_200_OK)
        else:
            return Response("Sin Respuesta del servidor",status=status.HTTP_400_BAD_REQUEST)

    def Calc_Num_Primos_gem(self, n):
        
        l_aux = []
        res = []
        for numero in range(2, n):
            if all(numero % i != 0 for i in range(2, int(math.sqrt(numero))+1)):
                l_aux.append(numero)
            if(len(l_aux) == 2):                
                if(l_aux[0] < l_aux[1] and abs(l_aux[0] - l_aux[1]) == 2):
                    res.append("("+str(l_aux[0])+","+str(l_aux[1])+")")
                    l_aux.pop(0)
                else:
                    l_aux.pop(0)

        return res

        