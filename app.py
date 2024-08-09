import calendar
import imgkit

# Função para ajustar o calendário
def ajustar_calendario(ano, mes):
    cal = calendar.monthcalendar(ano, mes)
    diaSemana = ['D', 'S', 'T', 'Q', 'Q', 'S', 'S']
    ajustedCalendar = []
    diaAnterior = [0]
    for semana in cal:
        semanaAjustada = diaAnterior + semana[:-1]
        diaAnterior = semana[-1:]
        ajustedCalendar.append(semanaAjustada)

    # Verifica se a linha 0 está zerada; se estiver, removo-a
    if all(dia == 0 for dia in ajustedCalendar[0]):
        ajustedCalendar.pop(0)
    
    return ajustedCalendar, diaSemana

# Dicionário de eventos
eventos = {}

# Função para adicionar eventos
def addEvent(nome, dias, mes):
    if mes not in eventos:
        eventos[mes] = {}
    for dia in dias:
        if dia not in eventos[mes]:
            eventos[mes][dia] = []
        eventos[mes][dia].append(nome)

# Adiciona eventos
addEvent("academia", [7, 8, 12, 14, 15, 19, 21, 23, 26, 28, 30], 8)
addEvent("faculdade", [2, 5, 9, 11, 13, 23, 25, 27, 30], 9)
addEvent("palestra", [2, 4, 7, 9, 11, 14, 25], 10)
addEvent("correr", [23], 8)
addEvent("cinema", [14, 20], 8)


# Função para gerar o HTML estático
def gerar_html_static(cal, dias_da_semana, mes, ano, eventos):
    # Início do documento HTML
    html = f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Calendário - {mes} - {ano}</title>
        <style>
            * {{
                color: white;
                padding: 0;
                margin: 0;
                box-sizing: border-box;
            }}
            body {{
                background-color: #2e2e2e;
            }}
            table {{
                border-collapse: collapse;
            }}
            th, td {{
                border: 1px solid #070606;
                padding: 8px;
                text-align: center;
            }}
            td {{
                min-height: 100px;
                min-width: 50px;
                max-width: 150px;
                vertical-align: top;
                padding: 8px;
            }}
            th {{
                background-color: #181818;
            }}
            p {{
                background-color: rgb(120, 197, 197);
                padding: 2px;
                color: #070606;
                word-wrap: wrap;
            }}
            
        </style>
    </head>
    <body>
        <h1>Calendário de {mes} - {ano}</h1>
        <table>
            <thead>
                <tr>
                    {" ".join([f"<th>{dia}</th>" for dia in dias_da_semana])}
                </tr>
            </thead>
            <tbody>
    """

    # Adiciona cada semana ao corpo da tabela
    for semana in cal:
        html += "<tr>"
        for dia in semana:
            if dia == 0:
                html += "<td></td>"
            else:
                eventos_html = ""
                if mes in eventos and dia in eventos[mes]:
                    eventos_html = "<br>".join([f"<p>{evento}</p>" for evento in eventos[mes][dia]])
                html += f"<td><span>{dia}<span/>{eventos_html}</td>"
        html += "</tr>"

    # Finaliza o documento HTML
    html += """
            </tbody>
        </table>
    </body>
    </html>
    """

    # Escreve o HTML gerado em um arquivo
    with open("index.html", "w", encoding="utf-8") as file:
        file.write(html)

# Dados para gerar o HTML
ano = 2024
mes = 8
cal, diaSemana = ajustar_calendario(ano, mes)

# Gera o HTML e salva em 'index.html'
gerar_html_static(cal, diaSemana, mes, ano, eventos)

# Função para converter HTML em imagem
def html_to_image(html_file, output_image):
    # Opções para o wkhtmltoimage
    options = {
        'format': 'jpg',
        'quality': '100',
        # 'width': '750', 
    }
    
    # Converte o HTML para imagem JPG
    imgkit.from_file(html_file, output_image, options=options)

# Converte o arquivo HTML gerado para uma imagem JPG
html_file = "index.html"
output_image = "calendario.jpg"
html_to_image(html_file, output_image)

print(f"Imagem gerada: {output_image}")
