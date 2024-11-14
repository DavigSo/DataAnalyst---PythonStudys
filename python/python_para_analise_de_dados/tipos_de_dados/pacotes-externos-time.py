import time
print('Comecei agora ...')
time.sleep(3)
print('Terminei')

Agora = time.localtime(
)
print(Agora)
print(type(Agora))

data_formatada = time.strftime('%m/%d/%y, %H:%M:%S', Agora)

print(data_formatada)