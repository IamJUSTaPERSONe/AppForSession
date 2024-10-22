import flet as ft
import sqlite3


def main(page: ft.Page):
    page.title = 'It_app'
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

        data_base.commit()
        data_base.close()

        user_login.value = ''
        user_password.value = ''
        button_reg.text = 'Добавлено'
        page.update()

    def validate(event):
        if all([user_login.value, user_password.value]):
            button_reg.disabled = False
            button_auth.disabled = False
        else:
            button_reg.disabled = True
            button_auth.disabled = True
        page.update()

    def user_auth(event):
        data_base = sqlite3.connect('Base')

        cursor = data_base.cursor()
        cursor.execute(f'SELECT * FROM users WHERE login = "{user_login.value}" AND password = "{user_password.value}"')
        if cursor.fetchone() != None:
            user_login.value = ''
            user_password.value = ''
            button_auth.text = 'Авторизовано'
            page.update()
        else:
            page.snack_bar = ft.SnackBar(ft.Text('Неверно введены данные'))
            page.snack_bar.open = True
            page.update()

        data_base.commit()
        data_base.close()



    user_login = ft.TextField(label='Логин', width=200, on_change=validate)
    user_password = ft.TextField(label='Пароль', password=True, width=200, on_change=validate)

    button_reg = ft.OutlinedButton(text='Добавить', width=200, disabled=True, on_click=reg)
    button_auth = ft.OutlinedButton(text='Авторизоваться', width=200, disabled=True, on_click=user_auth)

    panel_registration = ft.Row(
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

    panel_auth = ft.Row(
            [
                        ft.Column(
                            [
                                ft.Text('Авторизация'),
                                user_login,
                                user_password,
                                button_auth
                            ]
                        )
                    ],
            alignment=ft.MainAxisAlignment.CENTER
    )

    def navigation(event):
        index = page.navigation_bar.selected_index
        page.clean()

        if index == 0: page.add(panel_registration)
        elif index == 1: page.add(panel_auth)

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.VERIFIED_USER, label='Регистрация'),
            ft.NavigationDestination(icon=ft.icons.VERIFIED_USER_OUTLINED, label='Авторизация')
        ], on_change=navigation
    )

    page.add(panel_registration)



ft.app(target=main)