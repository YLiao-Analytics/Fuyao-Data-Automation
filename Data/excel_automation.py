import pandas as pd
import glob
import os

# 1. 自动获取当前脚本所在的目录
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = current_dir

print(f"正在搜索文件夹: {file_path}")

# 2. 获取所有 CSV 文件
all_files = glob.glob(os.path.join(file_path, "*.csv"))
print(f"找到的文件列表: {all_files}")

if not all_files:
    print("❌ 错误：没找到任何 CSV 文件！请检查 Data 文件夹里是否有 .csv 文件。")
else:
    li = []
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0)
        df['Workshop'] = os.path.basename(filename).split('.')[0]
        li.append(df)

    # 3. 合并数据
    frame = pd.concat(li, axis=0, ignore_index=True)
    
    # 后续处理...
    frame['Output'] = frame['Output'].fillna(0)
    summary = frame.groupby('Workshop').agg({
        'Output': 'sum',
        'Waste_Rate': 'mean'
    }).reset_index()

    summary.to_excel('Final_Monthly_Report.xlsx', index=False)
    print("✅ 成功生成 Excel！")