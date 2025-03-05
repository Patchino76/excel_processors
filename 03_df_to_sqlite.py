#%%
import pandas as pd
from datetime import datetime, timedelta
import os
from pathlib import Path
import sys

# Add parent directory to path so we can import the columns_dictionary module
parent_dir = Path(__file__).parent.parent
sys.path.append(str(parent_dir))

# %%
parent_dir = Path(__file__).parent.parent
file_path = "combined_dispatcher_data_en.csv"
df = pd.read_csv(file_path)
df.tail()
# %%
