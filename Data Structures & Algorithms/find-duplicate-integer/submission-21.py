# Segunda version
'''
Pasos del agoritmo con dos punteros

1- guardar la longitud del array
2- iniciar un contador
3- iniciar dos punteros uno en la posicion 0 y otro en 1
4- recorrer la lista, hasta que los punteros se encuentren
5- verificar que los dos numeros en las posiciones son diferentes
    si cumple la condicion: avanzan los punteros
    si no: retorna el numero duplicado
6- verificar que los punteros no se desborden    
7- retornar null     
'''
# Continuar
# Segunda version
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        low = 0
        fast = 0

        while True:

            low = nums[low]
            fast = nums[nums[fast]]
            
            if low == fast:
                break      

        low2 = 0
        while low != low2:   

            low = nums[low]
            low2 = nums[low2] 
        return low            