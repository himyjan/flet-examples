import math

import flet as ft


def main(page: ft.Page):
    page.title = "Containers with gradient"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.add(
        ft.Row(
            [
                ft.Container(
                    content=ft.Text("Linear gradient"),
                    padding=10,
                    alignment=ft.alignment.center,
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.top_left,
                        end=ft.Alignment(0.8, 1),
                        colors=[
                            "0xff1f005c",
                            "0xff5b0060",
                            "0xff870160",
                            "0xffac255e",
                            "0xffca485c",
                            "0xffe16b5c",
                            "0xfff39060",
                            "0xffffb56b",
                        ],
                        tile_mode=ft.GradientTileMode.MIRROR,
                        rotation=math.pi / 3,
                    ),
                    width=200,
                    height=200,
                    border_radius=10,
                ),
                ft.Container(
                    content=ft.Text("Linear gradient with stops"),
                    padding=10,
                    alignment=ft.alignment.center,
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.center_left,
                        end=ft.alignment.center_right,
                        colors=[ft.colors.RED, ft.colors.GREEN, ft.colors.BLUE],
                        stops=[0.1, 0.2, 1.0],
                        tile_mode=ft.GradientTileMode.MIRROR,
                    ),
                    width=200,
                    height=200,
                    border_radius=10,
                ),
                ft.Container(
                    content=ft.Text("Radial gradient"),
                    padding=10,
                    alignment=ft.alignment.center,
                    gradient=ft.RadialGradient(
                        center=ft.Alignment(0.7, -0.6),
                        radius=0.2,
                        colors=[
                            "0xFFFFFF00",  # yellow sun
                            "0xFF0099FF",  # blue sky
                        ],
                        stops=[0.4, 1.0],
                    ),
                    width=200,
                    height=200,
                    border_radius=10,
                ),
                ft.Container(
                    content=ft.Text("Sweep gradient"),
                    padding=10,
                    alignment=ft.alignment.center,
                    gradient=ft.SweepGradient(
                        center=ft.alignment.center,
                        start_angle=0.0,
                        end_angle=math.pi * 2,
                        colors=[
                            "0xFF4285F4",
                            "0xFF34A853",
                            "0xFFFBBC05",
                            "0xFFEA4335",
                            "0xFF4285F4",
                        ],
                        stops=[0.0, 0.25, 0.5, 0.75, 1.0],
                        rotation=math.pi / 4,
                    ),
                    width=200,
                    height=200,
                    border_radius=10,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            scroll=ft.ScrollMode.AUTO,
        ),
    )


ft.app(main)
