from ngapp import AppConfig
from . import __version__, {{ cookiecutter.python_class }}

_DESCRIPTION = "App descrition shown in preview"

config = AppConfig(
    name="{{ cookiecutter.app_title }}",
    version = __version__,
    python_class={{ cookiecutter.python_class }},
    frontend_pip_dependencies=[],
    description=_DESCRIPTION,
)
    
