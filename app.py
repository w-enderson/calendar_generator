from flask import Flask, render_template
import calendar

app = Flask(__name__)

def ajustar_calendario(ano, mes):
    cal = calendar.monthcalendar(ano, mes)

    diaSemana = ['D', 'S', 'T', 'Q', 'Q', 'S', 'S']

    ajustedCalendar = []

    diaAnterior = [0]
    for semana in cal:
        semanaAjustada = diaAnterior + semana[:-1]
        
        diaAnterior = semana[-1:]
        ajustedCalendar.append(semanaAjustada)
    
    # verifica se a linha 0 está zerada;
    isZero = True
    for dia in ajustedCalendar[0]:
        if dia!=0:
            isZero = False
    
    # se estiver zerada, removo-a
    if isZero:
        ajustedCalendar.pop(0)
    
    return ajustedCalendar, diaSemana


eventos = {}
def addEvent(nome, dias, mes):
    if mes not in eventos:
        eventos[mes] = {}
    for dia in dias:
        if dia not in eventos[mes]:
            eventos[mes][dia] = []
        eventos[mes][dia].append(nome)


addEvent("reunião", [7, 8, 12, 14, 15, 19, 21, 23,  26, 28, 30], 8)
addEvent("reunião", [2, 5, 9, 11, 13, 23, 25, 27, 30], 9)
addEvent("reunião", [2, 4, 7, 9, 11, 14, 25], 10)
addEvent("palestra", [23], 8)

@app.route('/')
def calendario():
    ano = 2024
    mes = 8

    cal, diaSemana = ajustar_calendario(ano, mes)

    return render_template('index.html', 
                           cal=cal, dias_da_semana=diaSemana, 
                           mes=mes, 
                           ano=ano,
                           eventos=eventos
                        )

if __name__ == '__main__':
    app.run(debug=True)
