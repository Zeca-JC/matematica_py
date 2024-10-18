# Gráficos simples no Python com Matplotlib - Visualização de Dados

import matplotlib.pyplot as grafico

meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun']
temp = [27, 31, 32, 26, 22, 17]

grafico.ylabel('Temp / ºC')
grafico.xlabel('Mês', color='blue')
grafico.axis(ymin=0, ymax=40)
grafico.title('Temperaturas Médias Mensais')
# grafico.plot(meses, temp, label='Temperaturas', marker='o')
grafico.bar(meses, temp)
grafico.legend()
grafico.grid(True)

grafico.show()

