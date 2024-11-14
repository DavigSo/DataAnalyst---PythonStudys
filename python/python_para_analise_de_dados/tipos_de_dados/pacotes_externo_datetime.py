import datetime
Dia_Hoje = datetime.datetime.today()
print(Dia_Hoje)

print(type(Dia_Hoje))
print(datetime.datetime.today().date())
print(datetime.datetime.today().hour)
print(datetime.datetime.today().year)

Data = datetime.datetime.today().date()
Ano = Data.year
Mes = Data.month
Dia = Data.day
print(Ano, Mes, Ano)

Data_Antiga = datetime.date(2022, 1, 1)
print(Data_Antiga)

print(Data - Data_Antiga)

print()
Data.strftime("%d/%m/%y")
print(Data)
