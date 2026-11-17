import pandas as pd

# ၁။ မူလ Excel ဖိုင်ကို ဖတ်ယူခြင်း (header=1 ဖြင့်)
df = pd.read_excel("Daily Mining.xlsx", header=1)
df.columns = df.columns.str.strip()

# ၂။ Total တန်းများကဲ့သို့သော NaN row များကို ဖယ်ရှားခြင်း
df = df.dropna(subset=['Site_Location'])

# ၃။ Output_Tons ပေါ်မူတည်၍ Performance အခြေအနေ သတ်မှတ်မည့် စည်းမျဉ်းလုပ်ဆောင်ချက် (Function)
def check_performance(tons):
    if tons >= 300:
        return "High Output"
    else:
        return "Normal"

# ၄။ Function ကို အသုံးပြု၍ Column အသစ် ('Performance') ကို အလိုအလျောက် ဖန်တီးခြင်း
df['Performance'] = df['Output_Tons'].apply(check_performance)

print("=== Data with New Performance Column ===")
print(df[['Date', 'Site_Location', 'Output_Tons', 'Performance']])

# ၅။ အချက်အလက်အသစ်ပါသော Report ကို Excel ဖိုင်အဖြစ် သိမ်းဆည်းခြင်း
df.to_excel("Performance_Mining_Report.xlsx", index=False)
print("\n'Performance_Mining_Report.xlsx' ဖိုင်အဖြစ် အောင်မြင်စွာ သိမ်းဆည်းပြီးပါပြီ။")