import pandas as pd


def describe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Quick numeric summary (count, mean, std, min, max, etc.)
    Future-proof: replace with more nuanced stats later.
    """

    return df.describe()
