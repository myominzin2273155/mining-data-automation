import pandas as pd

# ၁။ မူလ Excel ဖိုင်ကို ဖတ်ယူခြင်း (header=1 ဖြင့်)
df = pd.read_excel("Daily Mining.xlsx", header=1)
df.columns = df.columns.str.strip()

# ၂။ Total တန်းများကဲ့သို့သော NaN row များကို ဖယ်ရှားခြင်း
df = df.dropna(subset=['Site_Location'])

# ၃။ Output_Tons စုစုပေါင်း (Total) ကို တွက်ချက်ခြင်း
total_output = df['Output_Tons'].sum()
print(f"=== Total Output Tons: {total_output} ===")

# ၄။ Total တန်းကို Dataframe ရဲ့ အောက်ဆုံးသို့ အသစ်ထည့်သွင်းခြင်း
total_row = pd.DataFrame({
    'Date': ['Total'],
    'Site_Location': ['-'],
    'Mineral_Type': ['-'],
    'Output_Tons': [total_output],
    'Status': ['-']
})

df_final = pd.concat([df, total_row], ignore_index=True)

# ၅။ စုစုပေါင်းပါဝင်သော Report အသစ်ကို Excel ဖိုင်အဖြစ် သိမ်းဆည်းခြင်း
df_final.to_excel("Final_Mining_Summary.xlsx", index=False)
print("\n'Final_Mining_Summary.xlsx' ဖိုင်အဖြစ် အောင်မြင်စွာ သိမ်းဆည်းပြီးပါပြီ။")