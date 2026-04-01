class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        list_s1 = [0] * 26
        list_ventana = [0] * 26
        mach = 0
        
        if len(s1) > len(s2):
            return False        

        for i in range(len(s1)):
             
            list_s1[ord(s1[i]) - ord('a')] += 1
            
            list_ventana[ord(s2[i]) - ord('a')] += 1

        for i in range(26):
            if list_s1[i] == list_ventana[i]:
                mach += 1   

        for i in range(len(s1),len(s2)):
            
            if mach == 26:
                return True
            
            caracter_index = ord(s2[i]) - ord('a')

            if list_s1[caracter_index] == list_ventana[caracter_index]:
                mach -= 1

            list_ventana[caracter_index] += 1

            if list_s1[caracter_index] == list_ventana[caracter_index]:
                mach += 1

            caracter_salida = ord(s2[i - len(s1)]) - ord('a')

            if list_s1[caracter_salida] == list_ventana[caracter_salida]:
                mach -= 1

            list_ventana[caracter_salida] -= 1

            if list_s1[caracter_salida] == list_ventana[caracter_salida]:
                mach += 1

            if mach == 26:
                return True    

        if mach == 26:
            return True              
        else:
            return False