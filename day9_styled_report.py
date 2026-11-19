import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Alignment

# ၁။ သန့်စင်ပြီးသား Master ဖိုင်ကို ဖတ်ယူခြင်း
df = pd.read_excel("Master_Clean_Report.xlsx")

output_file = "Styled_Mining_Report.xlsx"
df.to_excel(output_file, index=False)

# ၂။ openpyxl ဖြင့် Excel ဖိုင်ကို ပြန်ဖွင့်ပြီး ပုံဖော်ခြင်း
wb = load_workbook(output_file)
ws = wb.active
ws.title = "Mining Report"

# Header (ပထမတန်း) အတွက် အရောင်၊ စာလုံး နှင့် အလယ်ဗဟိုညှိခြင်း
header_fill = PatternFill(start_color="1F4E78", end_color="1F4E78", fill_type="solid")
header_font = Font(color="FFFFFF", bold=True, size=11)

for cell in ws[1]:
    cell.fill = header_fill
    cell.font = header_font
    cell.alignment = Alignment(horizontal="center", vertical="center")

# ၃။ Column တစ်ခုချင်းစီ၏ စာလုံးအရှည်အလိုက် အကျယ် (Width) ကို အလိုအလျောက် ညှိခြင်း
for col in ws.columns:
    max_length = 0
    col_letter = col[0].column_letter
    for cell in col:
        val_str = str(cell.value or "")
        if len(val_str) > max_length:
            max_length = len(val_str)
    ws.column_dimensions[col_letter].width = max_length + 4

wb.save(output_file)
print(f"ပုံဖော်ပြီးသား Excel ဖိုင် '{output_file}' ကို အောင်မြင်စွာ ထုတ်လုပ်ပြီးပါပြီ။")