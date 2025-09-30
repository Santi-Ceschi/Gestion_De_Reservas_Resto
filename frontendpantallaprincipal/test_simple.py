import flet as ft

def main(page: ft.Page):
    page.title = "Test Simple"
    page.add(ft.Text("Hola mundo"))

if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER, port=8084)