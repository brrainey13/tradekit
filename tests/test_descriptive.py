import pandas as pd
import pytest

import quantkit as qk  # editable-installed package


def test_describe_mean_only():
    """
    Minimal sanity check:

    * Make a tiny DataFrame
    * Call YOUR describe()
    * Compare just the mean to pandas'
    """
    df = pd.DataFrame({"x": [1, 2, 3, 4, 5]})
    got = qk.describe(df)  # will fail until you implement it
    expect = df.describe()  # pandas ground truth

    assert pytest.approx(expect.loc["mean", "x"]) == got.loc["mean", "x"]
