import flet as ft


def main(page):
    page.add(
        ft.Stack(
            [
                ft.CircleAvatar(
                    foreground_image_src="https://avatars.githubusercontent.com/u/5041459?s=88&v=4"
                ),
                ft.Container(
                    content=ft.CircleAvatar(bgcolor=ft.Colors.GREEN, radius=5),
                    alignment=ft.alignment.bottom_left,
                ),
            ],
            width=40,
            height=40,
        )
    )


ft.app(main)
