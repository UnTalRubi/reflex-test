import reflex as rx


def index() -> rx.Component:
    return rx.container(
        rx.box(
            "What is Reflex?",
            text_align="right",
        ),
        rx.box(
            "A way to build web apps in pure Python!",
            text_align="left",
        ),
    )


app = rx.App()
app.add_page(index)
