
import math

def resolver_equacao_2_grau():
    #print("Calculadora de Equação do 2º Grau (ax² + bx + c = 0) ")
    a = float(input("Digite  a: "))
    b = float(input("Digite  b: "))
    c = float(input("Digite  c: "))
    
    if a == 0:
        print("isso não é uma equação do 2º grau.")
        return
    
    if b == 0 or c == 0:
        print("Erro: A equação é incompleta. Este algoritmo aceita apenas equações completas (b ≠ 0 e c ≠ 0).")
        return
    delta = (b ** 2) - (4 * a * c)
    print(f"\nDelta (Δ) = {delta}")

    if delta < 0:
        print("A equação não possui raízes reais, pois Delta é negativo.")

    elif delta == 0:
        x = -b / (2 * a)
        print(f"A equação possui duas raízes reais e iguais.")
        print(f"x1 = x2 = {x:.2f}")
 
    else:
        raiz_delta = math.sqrt(delta)
        x1 = (-b + raiz_delta) / (2 * a)
        x2 = (-b - raiz_delta) / (2 * a)
        print("A equação possui duas raízes reais e distintas.")
        print(f"x1 = {x1:.2f}")
        print(f"x2 = {x2:.2f}")

if __name__ == "__main__":
    resolver_equacao_2_grau()