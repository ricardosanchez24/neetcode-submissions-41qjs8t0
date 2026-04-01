class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area_max = 0
        
        izq = 0
        der = len(heights) - 1

        while izq < der:

            distancia = der - izq

            valor_min = min(heights[izq],heights[der])
            area = valor_min * distancia
                
            area_max = max(area,area_max)  

            if heights[izq] <= heights[der]:
                izq += 1
            else:
                der -= 1      
        return area_max                   