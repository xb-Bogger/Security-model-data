import pandas as pd
import os

data_dir = 'data'
for filename in os.listdir(data_dir):
    if filename.endswith('.parquet'):
        parquet_path = os.path.join(data_dir, filename)
        csv_path = os.path.join(data_dir, filename.replace('.parquet', '.csv'))
        df = pd.read_parquet(parquet_path)
        df.to_csv(csv_path, index=False)
        print(f"{parquet_path} -> {csv_path}")