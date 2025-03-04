#%%
import pandas as pd
from datetime import datetime, timedelta
import os
from pathlib import Path
# %%
parent_dir = Path(__file__).parent.parent
file_path_24 = parent_dir / "processed_dispatcher_data_2024.csv"
df_24 = pd.read_csv(file_path_24)
file_path_25 = parent_dir / "processed_dispatcher_data_2025.csv"
df_25 = pd.read_csv(file_path_25)

columns_dict = {
    "date": "Дата",
    "shift": "Смяна",
    "dispatcher": "Диспечер",
    "daily_ore_fed": "Подадена руда от МГТЛ за денонощието",
    "warehouse_2_status": "Състояние на склад №2",
    "crushed_ore_sst": "Натрошена руда от Цех ССТ",
    "ore_class_15mm": "Класа +   15,0мм.",
    "ore_class_12_5mm": "Класа +   12,5мм.",
    "ore_to_int_bunkers": "Превозена руда до междинни бункери",
    "int_bunkers_status": "Състояние на междинни бункери",
    "processed_ore_mfc": "Преработена руда в цех МФЦ",
    "processed_ore_moisture": "Влага на преработената руда",
    "dry_processed_ore": "Суха преработена руда",
    "granodiorites": "Гранодиорити",
    "dikes": "Дайки",
    "schists": "Шисти",
    "grinding_class_plus_0_2mm": "Смилане класа + 0,20мм",
    "grinding_class_minus_0_08mm": "Смилане класа -0,08мм",
    "pulp_density": "Плътност на пулпа",
    "cu_content_in_ores": "Съдържание на мед в рудите по Куриер",
    "cu_metal_in_ores": "Метал мед в рудите по Куриер",
    "adjusted_cu_content_in_ores": "Коригирана съдържание на мед в рудите",
    "cu_content_in_waste": "Съдържание на мед в отпадъка по Куриер",
    "cu_metal_in_waste": "Метал мед в отпадъка по Куриер",
    "cu_content_in_concentrate": "Съдържание на мед в медния к-т Куриер",
    "cu_metal_in_concentrate": "Метал мед в концентрата по Куриер",
    "tech_extraction": "Технологично извличане по Куриер",
    "load_extraction": "Товарно извличане",
    "extracted_cu_concentrate": "Добит меден концентрат",
    "cu_concentrate_moisture": "Влага на медния концентрат",
    "cu_content_in_concentrate_basic": "Съдържание на мед в медния к-т",
    "cu_content_in_concentrate_chem": "Съдържание на мед в медния к-т  /химия-товарен/",
    "cu_metal_in_concentrate_basic": "Метал мед в медния концентрат",
    "cu_metal_in_concentrate_chem": "Метал мед в медния концентрат /химия/",
    "liter_weight_in_thickener": "Литрово тегло в сгъстителя",
    "cu_concentrate_auto_scale": "Меден концентра, автомобилна везна",
    "cu_concentrate_in_warehouse": "Меден концентрат в склад",
    "timestamp": "TimeStamp"
}
# %%
df_all = pd.concat([df_24, df_25], ignore_index=True)
colummns_bg = columns_dict.values()
# df_all = df_all[colummns_bg]
# print(df_all[colummns_bg])
# df_all = df_all.dropna()
# df_all
# %%
