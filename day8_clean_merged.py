import pandas as pd

# ၁။ ပေါင်းစည်းထားသော Master ဖိုင်ကို ပြန်ဖတ်ယူခြင်း
df = pd.read_excel("Master_Combined_Report.xlsx")
print("မူလ ဒေတာအတန်း အရေအတွက်:", len(df))

# ၂။ တူညီနေသော Row များကို ဖယ်ရှားခြင်း (Source_File column ကို မထည့်ဘဲ အဓိက column များကို နှိုင်းယှဉ်လိုလျှင် subset သတ်မှတ်နိုင်သည်)
df_clean = df.drop_duplicates()
print("ထပ်နေသော Row များ ဖယ်ရှားပြီးနောက် အတန်းအရေအတွက်:", len(df_clean))

# ၃။ သန့်စင်ပြီးသား ဖိုင်ကို သိမ်းဆည်းခြင်း
df_clean.to_excel("Master_Clean_Report.xlsx", index=False)
print("\n'Master_Clean_Report.xlsx' အဖြစ် သန့်စင် သိမ်းဆည်းပြီးပါပြီ။")