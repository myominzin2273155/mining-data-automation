import pandas as pd

# ၁။ မူလ Excel ဖိုင်ကို ဖတ်ယူခြင်း (header=1 ဖြင့်)
df = pd.read_excel("Daily Mining.xlsx", header=1)
df.columns = df.columns.str.strip()

# ၂။ Total တန်းများကဲ့သို့သော NaN row များကို ဖယ်ရှားခြင်း
df = df.dropna(subset=['Site_Location'])

# ၃။ ExcelWriter ကို အသုံးပြု၍ Sheet များစွာပါသော Excel ဖိုင်တစ်ခု ဖန်တီးခြင်း
with pd.ExcelWriter("Complete_Mining_Report.xlsx", engine='openpyxl') as writer:
    # ဃ၁။ ဒေတာအားလုံးကို 'All_Data' Sheet ထဲသို့ ထည့်ရန်
    df.to_excel(writer, sheet_name='All_Data', index=False)
    
    # ဃ၂။ Kachin-Site-A သီးသန့် ဒေတာကို 'Site_A' Sheet ထဲသို့ ထည့်ရန်
    site_a = df[df['Site_Location'] == 'Kachin-Site-A']
    site_a.to_excel(writer, sheet_name='Site_A', index=False)
    
    # ဃ၃။ Kachin-Site-B သီးသန့် ဒေတာကို 'Site_B' Sheet ထဲသို့ ထည့်ရန်
    site_b = df[df['Site_Location'] == 'Kachin-Site-B']
    site_b.to_excel(writer, sheet_name='Site_B', index=False)

print("=== 'Complete_Mining_Report.xlsx' (Multi-sheet) အောင်မြင်စွာ ဖန်တီးပြီးပါပြီ။ ===")