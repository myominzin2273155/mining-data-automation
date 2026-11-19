import pandas as pd

# ၁။ သန့်စင်ပြီးသား Master ဖိုင်ကို ဖတ်ယူခြင်း
df_clean = pd.read_excel("Master_Clean_Report.xlsx")

# ၂။ Column ခေါင်းစဉ်များကို ကြည့်ရှုခြင်း
print("Master_Clean_Report ထဲရှိ Column များ:")
print(df_clean.columns.tolist())

# ၃။ Numeric (ဂဏန်း) Column များ၏ အကျဉ်းချုပ် ကိန်းဂဏန်းများကို ကြည့်ရှုခြင်း
print("\n=== ကိန်းဂဏန်း Column များ၏ Summary ===")
print(df_clean.describe())