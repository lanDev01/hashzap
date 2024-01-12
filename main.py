import flet as ft

def main(page):
    text = ft.Text("HashZap")

    def startChat(event):
        print("Iniciar o chat")

    button = ft.ElevatedButton("Iniciar Chat", on_click=startChat)


    page.add(text)
    page.add(button)
    
ft.app(main)