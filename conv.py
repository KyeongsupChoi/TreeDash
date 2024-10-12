import pandas as pd

# Read CSV file
df = pd.read_csv('tourism.csv', encoding='euc-kr')



# Write it back to CSV with UTF-8 encoding (or any other changes you want to make)
df.to_csv('tourist.csv', index=False, encoding='utf-8-sig')