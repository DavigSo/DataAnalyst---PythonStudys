# Levando em consideração a velocidade máxima permiritda de 80km em uma determinada rua. Crie um programa que recebe do usuario um valor que representa a velocidadde e com base nessa velocidade diga se ele tomou uma multa leve, grave ou gravissima. levando em consideração quie  se a pessoa estiver abaixo da velocidade maxima seu programa deve exibir "não houve multa", caslo esteja entre 11 a 20km acima da velocidade maxima, exibir; "levou multa grave". e caso esteja acima de 20km acima da velocidade maxima, exciba: "levou multa gravissima"

velocidade = int(input("Informe a velocidade: "))
if velocidade <= 80:
    print("Não houve multa")
elif velocidade >= 81 and velocidade <= 90:
    print("levou multa leve")
elif velocidade >= 91 and velocidade <= 99:
    print("levou multa leve")
else:
    print("levou multa gravissima")
