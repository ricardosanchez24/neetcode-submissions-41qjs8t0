class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area_max = 0
        
        izq = 0
        der = len(heights) - 1

        while izq < der:
            valor_izq = heights[izq]
            valor_der = heights[der]

            distancia = der - izq

            valor_min = min(valor_izq,valor_der)
            area = valor_min * distancia
                
            area_max = max(area,area_max)  

            if valor_izq <= valor_der:
                izq += 1
            else:
                der -= 1      
        return area_max                   