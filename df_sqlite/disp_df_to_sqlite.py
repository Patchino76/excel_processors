#%%
import pandas as pd
from datetime import datetime, timedelta
import os
from pathlib import Path
import sys

# Add parent directory to path so we can import the columns_dictionary module
parent_dir = Path(__file__).parent.parent
sys.path.append(str(parent_dir))
from columns_dictionary import columns_dict
# %%
parent_dir = Path(__file__).parent.parent
file_path_24 = parent_dir / "processed_dispatcher_data_2024_en.csv"
df_24 = pd.read_csv(file_path_24)
file_path_25 = parent_dir / "processed_dispatcher_data_2025_en.csv"
df_25 = pd.read_csv(file_path_25)


# %%
df_all = pd.concat([df_24, df_25], ignore_index=True)
colummns_bg = columns_dict.values()
# df_all = df_all[colummns_bg]
# print(df_all[colummns_bg])
# df_all = df_all.dropna()
df_all
# %%
