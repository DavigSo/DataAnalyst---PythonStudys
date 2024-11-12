# Eu cheguei atrasado na aula, ainda posso entrar? Se essa não for sua terceira vez chegando atrasado, então pode sim, caso contrário irá tomar uma suspensão


atrasos_do_aluno = 0
if atrasos_do_aluno >= 3:
    print("Você está suspenso")
elif atrasos_do_aluno == 1:
    print("Pode entrar, porém caso tome mais 2 faltas, irá ser suspenso")
elif atrasos_do_aluno == 2:
    print("Pode entrar, pórem caso tome mais 1 falta, irá ser suspenso")
else:
    print("Pode entrar")
