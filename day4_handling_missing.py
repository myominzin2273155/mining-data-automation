import pandas as pd

# ၁။ Excel ဖိုင်ကို ဖတ်ယူခြင်း (header=1 ဖြင့်)
df = pd.read_excel("Daily Mining.xlsx", header=1)
df.columns = df.columns.str.strip()

print("=== Raw Data (With Potential Missing Values) ===")
print(df[['Date', 'Site_Location', 'Mineral_Type', 'Output_Tons', 'Status']])

# ၂။ Status ကဲ့သို့သော နေရာလွတ်များတွင် 'Unassigned' ဟု အစားထိုးဖြည့်ဆည်းခြင်း
df['Status'] = df['Status'].fillna('Unassigned')

print("\n=== Data After Filling Missing Values ===")
print(df[['Date', 'Site_Location', 'Mineral_Type', 'Output_Tons', 'Status']])

# ၃။ သန့်စင်ပြီးသား ဒေတာကို Excel ဖိုင်အသစ်အဖြစ် သိမ်းဆည်းခြင်း
df.to_excel("Cleaned_Mining_Report.xlsx", index=False)
print("\n'Cleaned_Mining_Report.xlsx' ဖိုင်အဖြစ် အောင်မြင်စွာ သိမ်းဆည်းပြီးပါပြီ။")