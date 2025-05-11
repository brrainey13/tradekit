from importlib.metadata import version

__all__ = ["describe"]  # top-level convenience
__version__ = version("tradekit")

# re-export handy funcs
from .stats.descriptive import describe
