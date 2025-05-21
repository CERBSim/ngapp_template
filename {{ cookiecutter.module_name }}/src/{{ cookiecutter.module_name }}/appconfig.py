from webapp_client import AppAccessConfig, AppConfig
from . import __version__, {{ cookiecutter.app_class }}

_DESCRIPTION = "App descrition shown in preview"

config = AppConfig(
    name="{{ cookiecutter.app_title }}",
    version = __version__,
    python_class={{ cookiecutter.app_class }},
    frontend_pip_dependencies=[],
    frontend_dependencies=[],
    description=_DESCRIPTION,
    compute_environments=[],
    access=AppAccessConfig()
)
    
