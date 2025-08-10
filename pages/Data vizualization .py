import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd

# إعداد الصفحة
st.set_page_config(
    page_title="Data Visualization App",
    page_icon="📊",
    layout="wide")

@st.cache_data
#@st.cache_resource--- for ML
# دالة لتحميل البيانات
def load_data(file):
    if file.name.endswith('.csv'):
        return pd.read_csv(file)
    elif file.name.endswith('.xlsx'):
        return pd.read_excel(file)

# رفع الملف
file = st.file_uploader("Upload a file", type=["csv", "xlsx"])

if file is not None:
    df = load_data(file)

    # اختيار عدد الصفوف
    n_rows = st.slider("Select number of rows to display", 1, len(df), 5)

    # اختيار الأعمدة
    columns_to_show = st.multiselect(
        "Select columns to display",
        options=df.columns.tolist(),
        default=df.columns.tolist()
    )

    # الأعمدة الرقمية فقط
    numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()

    # عرض الجدول
    st.write(df.head(n_rows)[columns_to_show])

    # إنشاء التبويبات
    tab1, tab2 = st.tabs(["Scatter Plot", "Histogram"])

    with tab1:
        st.subheader("Scatter Plot")

        col_1, col_2, col_3 = st.columns(3)

        with col_1:
            x_column = st.selectbox("Select X-axis column", options=numeric_columns, index=0)
        with col_2:
            y_column = st.selectbox("Select Y-axis column", options=numeric_columns, index=1)
        with col_3:
            color_column = st.selectbox("Select color column", options=df.columns.tolist(), index=0)

        # إنشاء رسم Scatter
        fig_scatter = px.scatter(
            data_frame=df,
            x=x_column,
            y=y_column,
            color=color_column
        )
        st.plotly_chart(fig_scatter)

    with tab2:
        st.subheader("Histogram")

        histogram_feature = st.selectbox(
            "Select feature for histogram",
            options=numeric_columns,
            index=0
        )

        fig_hist = px.histogram(
            data_frame=df,
            x=histogram_feature,
            color=color_column,
            marginal="box",
            nbins=30
        )
        st.plotly_chart(fig_hist)
