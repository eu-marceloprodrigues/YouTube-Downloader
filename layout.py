import flet as ft
from flet import Colors
from functions.method import dowload_video

def main(page: ft.Page):
    page.title = 'Baixar vídeos'
    page.window.resizable = False
    page.window.always_on_top = True
    page.window.height = 185
    page.window.width = 350
    page.window.center()

    # Função chamada quando o botão é clicado
    def on_click(e):
        url = tb.value  # <-- pega o valor digitado        
        tb.value = " "
        page.snack_bar = ft.SnackBar(ft.Text(f"URL recebida: {url}"))
        page.snack_bar.open = True
        page.update()
        dowload_video(url)


# Imagem que vai dentro do botão (use caminho local ou URL)
    imagem = ft.Image(
        src="https://cdn-icons-png.flaticon.com/512/25/25284.png",  # exemplo: ícone de download
        width=24,
        height=24,
    )
    # Campo de texto
    tb = ft.TextField(label="Insira a URL")

    # Botão
     # Botão com imagem + texto
    botao = ft.Container(
        content=ft.Row(
            controls=[
                imagem,
                ft.Text("Baixar", color=Colors.WHITE, weight=ft.FontWeight.BOLD),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=8,
        ),
        width=120,
        height=50,
        border_radius=40,
        bgcolor="#02ee51",
        alignment=ft.alignment.center,
        ink=True,  # permite clique visual
        on_click= on_click
    )

    # Alinhar o botão à direita
    linha_botao = ft.Row(
        controls=[botao],
        alignment=ft.MainAxisAlignment.END  # <-- alinha à direita
    )

    # Adicionar os elementos na página
    page.add(tb, linha_botao)

ft.app(main)
