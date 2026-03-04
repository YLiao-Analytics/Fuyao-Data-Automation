import streamlit as st
import pandas as pd
import glob
import os

# 1. 网页标题和设置
st.set_page_config(page_title="福耀生产数据看板", layout="wide")
st.title("📊 Fuyao Glass 生产自动看板")
st.markdown("---")

# 2. 侧边栏：上传文件
st.sidebar.header("数据上传区")
uploaded_files = st.sidebar.file_uploader("上传各车间 CSV 文件", type="csv", accept_multiple_files=True)

if uploaded_files:
    li = []
    for file in uploaded_files:
        df = pd.read_csv(file)
        # 获取文件名作为车间名
        df['Workshop'] = file.name.split('.')[0]
        li.append(df)
    
    # 合并数据
    full_data = pd.concat(li, axis=0, ignore_index=True)
    full_data['Output'] = full_data['Output'].fillna(0)

    # 3. 页面布局：上方显示核心指标 (KPI)
    col1, col2, col3 = st.columns(3)
    total_output = full_data['Output'].sum()
    avg_waste = full_data['Waste_Rate'].mean()
    
    col1.metric("总产量 (Total Output)", f"{total_output:,.0f} units")
    col2.metric("平均废品率 (Avg Waste)", f"{avg_waste:.2%}")
    col3.metric("处理文件数", len(uploaded_files))

    # 4. 页面布局：下方显示图表
    st.subheader("📈 各车间产量对比")
    summary = full_data.groupby('Workshop')['Output'].sum()
    st.bar_chart(summary)

    # 5. 显示原始数据
    with st.expander("查看合并后的原始数据"):
        st.write(full_data)

    # 6. 下载按钮
    csv = full_data.to_csv(index=False).encode('utf-8')
    st.download_button("📥 下载汇总报表", data=csv, file_name="consolidated_report.csv")

else:
    st.info("请在左侧上传 CSV 文件开始分析。")