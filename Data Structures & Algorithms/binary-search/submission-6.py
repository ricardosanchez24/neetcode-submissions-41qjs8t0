class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # sacar el numero de leementos en el array
        l = 0
        size_nums = len(nums) - 1
        
        # recorrer el array
        while l <= size_nums:
         # ir a la mitad del arreglo
            mid = (l + size_nums) // 2 
         # verificar si el numero en la mitad es target
            if nums[mid] == target:
         # si es asi retornar el indice del numero actual       
                return mid 
         
         # si no verificar si el numero actual es mayor o menor al target
         # si es menor descarta la parte izquierda y el numero actual
         # caso contrario descartar la parte derecha
            if  nums[mid] > target:
                size_nums = mid - 1
            else:
                l = mid + 1        
         
         # si no se encontro el numero retornar -1
        return -1 