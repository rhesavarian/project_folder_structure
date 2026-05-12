import os
from dotenv import load_dotenv
from func.data_file_path import get_data_path
import pandas as pd

load_dotenv()
print(os.getenv("SAMPLE_KEY"))

file_path = get_data_path("00_sample_data.csv", data_type="raw")
df = pd.read_csv(file_path)
print(df)
