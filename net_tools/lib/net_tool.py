import numpy as np
import pandas as pd


def check_pandas_version():
    return pd.__version__


def np_test():
    return np.arange(10)
