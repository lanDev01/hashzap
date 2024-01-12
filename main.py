import flet as ft

def main(page):
    text = ft.Text("HashZap") # Titulo da pagina

    nameUser = ft.TextField(label="Escreva seu nome")

    popUp = ft.AlertDialog(
        open=False,
        modal=True, 
        title=ft.Text("Bem vindo ao HashZap"), 
        content=nameUser,
        actions=[ft.ElevatedButton("Entrar")]
    ) # criando PopUp

    def startChat(event): # Função que faz o pop aparecer
        page.dialog = popUp
        popUp.open = True
        page.update()
    button = ft.ElevatedButton("Iniciar Chat", on_click=startChat)


    page.add(text)
    page.add(button)
    
ft.app(main)