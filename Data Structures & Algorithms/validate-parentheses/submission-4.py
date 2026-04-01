class Solution:
    def isValid(self, s: str) -> bool:
        parejas = {')':'(','}':'{',']':'['}
        pila = []
        cima = None

        if len(s) <= 1:
            return False

        for i in range(len(s)):
            if s[i] in parejas.values():
                pila.append(s[i])
                continue
            if pila != []:
                cima = pila[-1]

            if s[i] in parejas.keys():
                if not pila:
                    return False
                    
                if cima == parejas[s[i]]:
                    pila.pop()
                else:
                    return False
        if not pila:
            return True
        else:
            return False                   