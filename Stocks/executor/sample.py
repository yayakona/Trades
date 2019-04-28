
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..","..","..")))

from Stocks.Stocks.load.PandasDataAccessor import PandasDataAccessor
from Stocks.Stocks.show.DataFrameViewer import DataFrameViewer


df = PandasDataAccessor.load("4563", start="2019-01-01",end="2019-03-31")
DataFrameViewer.candlestick(df)
