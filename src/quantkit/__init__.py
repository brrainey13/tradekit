from importlib.metadata import version

__all__ = ["describe"]  # top-level convenience
__version__ = version("quantkit")

# re-export handy funcs
from .stats.descriptive import describe

