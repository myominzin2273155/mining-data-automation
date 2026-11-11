import pandas as pd

# Excel ဖိုင်ကို ဖတ်သည့်အခါ ပထမတန်းကို ကျော်ပြီး ဒုတိယတန်းကို Column ခေါင်းစဉ် (Header) အဖြစ် သတ်မှတ်ရန် header=1 ကို သုံးပါ
df = pd.read_excel("Daily Mining.xlsx", header=1)

# Column နာမည်များတွင် ပါလာနိုင်သော နေရာလွတ် (Spaces) များကို ဖယ်ရှားပေးခြင်း
df.columns = df.columns.str.strip()

# Filtering: Kachin-Site-A ၏ ဒေတာကို သီးသန့် ခွဲထုတ်ခြင်း
site_a_df = df[df["Site_Location"] == "Kachin-Site-A"]

print("=== Kachin-Site-A Data Only ===")
print(site_a_df)

# Grouping: Site တစ်ခုချင်းစီအလိုက် စုစုပေါင်း Output Tons တွက်ချက်ခြင်း
site_summary = df.groupby("Site_Location")["Output_Tons"].sum().reset_index()

print("\n=== Total Output by Site Location ===")
print(site_summary)

# Excel ဖိုင်အသစ်အဖြစ် သိမ်းဆည်းခြင်း
site_summary.to_excel("Site_Summary_Report.xlsx", index=False)
print("\n'Site_Summary_Report.xlsx' ဖိုင်အဖြစ် အောင်မြင်စွာ သိမ်းဆည်းပြီးပါပြီ။")