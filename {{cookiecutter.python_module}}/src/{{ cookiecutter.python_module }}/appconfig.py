from ngapp import AccessLevel, AppAccessConfig, AppConfig, ComputeEnvironment
from ngapp.utils import __DEFAULT_DOCKERFILE__

from . import __version__, {{ cookiecutter.python_class }}

_DESCRIPTION = "App descrition shown in preview"
_DOCKERFILE = __DEFAULT_DOCKERFILE__ + """
# Add any additional dependencies or configurations here
# RUN python3 -m pip install scipy
"""

config = AppConfig(
    name="{{ cookiecutter.app_title }}",
    version = __version__,
    python_class={{ cookiecutter.python_class }},
    frontend_pip_dependencies=[],
    description=_DESCRIPTION,
    compute_environments=[
        ComputeEnvironment(env_type="docker", dockerfile=_DOCKERFILE, cpus=1)
    ],
    access=AppAccessConfig(
        default_level=AccessLevel.STANDARD,
        enable_trial=True,
        auto_grant_trial=True,
        trial_days=21,
    ),
)
    
