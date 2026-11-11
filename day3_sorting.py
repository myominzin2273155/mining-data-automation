import pandas as pd

# ၁။ Excel ဖိုင်ကို ဖတ်ယူခြင်း (header=1 ဖြင့်)
df = pd.read_excel("Daily Mining.xlsx", header=1)
df.columns = df.columns.str.strip()

# ၂။ Site_Location မပါရှိသော Excel အောက်ခြေက Total တန်းများကို ဖယ်ရှားခြင်း
df = df.dropna(subset=['Site_Location'])

# ၃။ Output_Tons များအလိုက် အများဆုံးမှ အနည်းဆုံးသို့ အစဉ်လိုက် စီခြင်း (Descending Order)
sorted_df = df.sort_values(by="Output_Tons", ascending=False)

print("=== Mining Data Sorted by Highest Output Tons ===")
print(sorted_df[['Date', 'Site_Location', 'Mineral_Type', 'Output_Tons', 'Status']])

# ၄။ Sorting လုပ်ပြီးသား ဒေတာများကို Excel ဖိုင်အသစ်အဖြစ် ထုတ်ယူ သိမ်းဆည်းခြင်း
sorted_df.to_excel("Sorted_Mining_Report.xlsx", index=False)
print("\n'Sorted_Mining_Report.xlsx' ဖိုင်အဖြစ် အောင်မြင်စွာ သိမ်းဆည်းပြီးပါပြီ။")