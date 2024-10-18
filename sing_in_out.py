import flet as ft
import sqlite3


def main(page: ft.Page):
    page.title = 'Регистрация'
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 350
    page.window_height = 400
    page.window_resizable = False

    def reg(event):
        data_base = sqlite3.connect('Base')

        cursor = data_base.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            login TEXT,
            password TEXT
        )""")
        cursor.execute(f'INSERT INTO users VALUES(NULL, "{user_login.value}", "{user_password.value}")')

        data_base.close()

        user_login.value = ''
        user_password.value = ''
        button_reg.text = 'Добавлено'
        page.update()

    def validate(event):
        if all([user_login.value, user_password.value]):
            button_reg.disabled = False
        else:
            button_reg.disabled = True
        page.update()

    user_login = ft.TextField(label='Логин', width=200, on_change=validate)
    user_password = ft.TextField(label='Пароль', password=True, width=200, on_change=validate)

    button_reg = ft.OutlinedButton(text='Добавить', width=200, disabled=True, on_click=reg)

    page.add(
        ft.Row(
            [
                ft.Column(
                    [
                        ft.Text('Регистрация'),
                        user_login,
                        user_password,
                        button_reg
                    ]
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )



ft.app(target=main)