import flet as ft
import subprocess

def main(page: ft.Page):
    t = ft.Text(value="Hello, world!")
    page.add(t)
    subprocess.run("python3 /discord_connection.py")

ft.app(target=main)
