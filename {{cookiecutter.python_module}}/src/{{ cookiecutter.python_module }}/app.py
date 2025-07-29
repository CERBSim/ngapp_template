from ngapp.app import App
from ngapp.components import *
from ngapp.utils import compute_node

class {{ cookiecutter.python_class }}(App):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = Heading("{{ cookiecutter.app_title }}")
        self.button = QBtn("Click me", ui_color="primary")
        self.counter_view = QInput(id="counter", ui_model_value=0,
                                   ui_style="width: 200px;")
        self.button.on_click(self.increment_counter)
        self.button_compute = QBtn("Compute", ui_color="primary", ui_class="q-mt-md")
        self.button_compute.on_click(self.compute_function)
        self.component = Centered(
            self.title,
            self.button,
            self.button_compute,
            self.counter_view,
            ui_style="padding-top: 50px;"
        )

    def increment_counter(self):
        self.counter_view.ui_model_value = int(self.counter_view.ui_model_value) + 1


    @compute_node
    def compute_function(self):
        from .backend.run import run_on_backend
        return run_on_backend(self)
