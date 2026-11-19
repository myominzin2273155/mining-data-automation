import glob
import pandas as pd

# ၁။ လက်ရှိ Folder ထဲရှိ Report.xlsx နှင့် ဆုံးသော ဖိုင်အားလုံးကို ရှာဖွေခြင်း
file_list = glob.glob("*Report.xlsx")
print("တွေ့ရှိသော ဖိုင်များ:", file_list)

# ၂။ ဖိုင်တစ်ခုချင်းစီကို ဖတ်ယူပြီး စာရင်း (List) ထဲသို့ စုစည်းခြင်း
all_data = []

for file in file_list:
    df = pd.read_excel(file)
    # ဘယ်ဖိုင်က လာတဲ့ ဒေတာလဲဆိုတာ သိရအောင် Source_File column အသစ်ထည့်ခြင်း
    df['Source_File'] = file
    all_data.append(df)

# ၃။ ဖိုင်အားလုံးကို Master DataFrame တစ်ခုတည်းအဖြစ် ပေါင်းစည်းခြင်း
if all_data:
    merged_df = pd.concat(all_data, ignore_index=True)
    
    # ၄။ ပေါင်းစည်းပြီးသား Master Report ကို Excel အဖြစ် သိမ်းဆည်းခြင်း
    merged_df.to_excel("Master_Combined_Report.xlsx", index=False)
    print(f"\nဖိုင်ပေါင်း ({len(file_list)}) ဖိုင်ကို 'Master_Combined_Report.xlsx' အဖြစ် အောင်မြင်စွာ ပေါင်းစည်းပြီးပါပြီ။")
    print(f"စုစုပေါင်း ဒေတာအတန်းအရေအတွက်: {len(merged_df)} တန်း")
else:
    print("ပေါင်းစည်းရန် ဖိုင်မတွေ့ပါ။")