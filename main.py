import flet as ft

def main(page):
    text = ft.Text("HashZap") # Titulo da pagina
    nameUser = ft.TextField(label="Escreva seu nome") # Input que recebe o nome do usuario

    # Criando conexão com outros usuarios | paginas
    def sendMessage(informations):
        chat.controls.append(ft.Text(informations))
        page.update() # Atualizando a pagina

    page.pubsub.subscribe(sendMessage)

    def submitMessage(event):
        # Colocando o nome do usuario na mensagem
        value = f"{nameUser.value}: {inputMenssage.value}"
        page.pubsub.send_all(value) # Enviando mensagem
        # Limpando o input quando enviar a mensagem
        inputMenssage.value = ""

        page.update()

    chat = ft.Column() # Criando chat com estilização em coluna
    inputMenssage = ft.TextField(label="Escreva sua mensagem...", on_submit=submitMessage) # Input de receber as mensagens
    buttonSubmit = ft.ElevatedButton("Enviar", on_click=submitMessage) # Botão de enviar

    def loginChat(event):
        popUp.open = False # Removendo PopUp
        page.remove(button) # Removendo o Botão 
        page.add(chat) # Adicionando Chat
        lineMessage = ft.Row(
            [inputMenssage, buttonSubmit]
        ) # Campo de escrever mensagem
        page.add(lineMessage) # Adicionando na pagina

        # Criando de texto que informa quando e qual usuario entro no chat
        textName = f"{nameUser.value} Entrou no Chat!"
        page.pubsub.send_all(textName)
        page.update() # Atualizando a pagina

    popUp = ft.AlertDialog(
        open=False, # Inicializando modal -> false
        modal=True, # Definindo PopUp como Modal
        title=ft.Text("Bem vindo ao HashZap"), # Titulo no Modal
        content=nameUser, # Campo onde o usuario escreve o nome dele
        actions=[ft.ElevatedButton("Entrar", on_click=loginChat)] # Ações do modal
    ) # criando PopUp

    def startChat(event): # Função que faz o pop aparecer
        page.dialog = popUp 
        popUp.open = True # Fazendo o PopUp aparecer
        page.update() # Atualizando a ágina
    button = ft.ElevatedButton("Iniciar Chat", on_click=startChat)


    page.add(text) # Adicionando titulo na pagina
    page.add(button) # Adicionando botão na pagina
    
# Rodando em formato de aplicativo
# ft.app(main) 
# Rodando no navegador
ft.app(main, view=ft.WEB_BROWSER) # Chamando função main para rodar a aplicação