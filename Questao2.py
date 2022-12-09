#Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.

h_inicial = int(input("Qual a hora inicial? "))
m_inicial = int(input("Qual o minuto inicial? "))
h_final = int(input("Qual a hora final? "))
m_final = int(input("Qual o minuto final? "))

#Convertendo tudo para minutos
m_final = m_final + (h_final*60)
m_inicial = m_inicial + (h_inicial*60)

#Tempo total do jogo em minutos
time = m_final - m_inicial

#Condição caso o tempo total em minutos dê negativo ou igual a zero.
if(time <= 0):
    time = time + (24*60)

#Convertendo tudo para horas e o resto em minutos.
hora = time // 60
minuto = time % 60 

print(f"O JOGO DUROU {hora} HORA(S) E {minuto} MINUTO(S).")