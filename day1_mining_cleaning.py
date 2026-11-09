import pandas as pd

# 1. တူးဖော်မှု အချက်အလက် ဒေတာများ ဖန်တီးခြင်း
data = {
    'Date': ['2026-11-01', '2026-11-02', '2026-11-03', '2026-11-04'],
    'Site_Location': ['Kachin-Site-A', 'Kachin-Site-A', 'Kachin-Site-B', 'Kachin-Site-B'],
    'Mineral_Type': ['Rare Earth', 'Rare Earth', 'Copper', 'Copper'],
    'Output_Tons': [120, None, 350, 400],  # None ဆိုသည်မှာ Data ကွက်လပ် ဖြစ်နေခြင်း
    'Status': ['Approved', 'Pending', 'Approved', 'Approved']
}

# 2. DataFrame အဖြစ် ပြောင်းလဲခြင်း
df = pd.DataFrame(data)

# 3. Data Cleaning: ကွက်လပ်ဖြစ်နေသော Output_Tons ကို ပျှမ်းမျှတန်ဖိုး (Mean) ဖြင့် ဖြည့်ဆည်းခြင်း
mean_tons = df['Output_Tons'].mean()
df['Output_Tons'] = df['Output_Tons'].fillna(mean_tons)

# 4. Total Output နှင့် Daily Average တွက်ချက်ခြင်း
total_output = df['Output_Tons'].sum()
avg_output = df['Output_Tons'].mean()

print("--- Cleaned Mining Dataset ---")
print(df)
print(f"\nTotal Output: {total_output:.2f} Tons")
print(f"Daily Average: {avg_output:.2f} Tons")