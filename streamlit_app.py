import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("📊 성적 데이터 시각화 앱")
st.write("CSV 파일을 업로드하고 다양한 그래프를 그릴 수 있습니다.")

# 1. CSV 파일 업로드
uploaded_file = st.file_uploader("성적 데이터 CSV 파일을 업로드하세요", type=["csv"])

df = None
if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("데이터 업로드 성공!")
        st.dataframe(df)
    except Exception as e:
        st.error(f"파일을 읽는 중 오류 발생: {e}")

if df is not None:
    st.markdown("---")
    st.header("그래프 옵션")
    graph_options = ["히스토그램", "막대그래프", "산점도", "상자그림"]
    selected_graph = st.radio("원하는 그래프를 선택하세요", graph_options)

    if selected_graph == "히스토그램":
        with st.expander("히스토그램 변수 선택"):
            num_cols = df.select_dtypes(include=np.number).columns.tolist()
            if not num_cols:
                st.warning("수치형 변수가 없습니다.")
            else:
                col = st.selectbox("히스토그램을 그릴 변수 선택", num_cols, key="hist")
                bins = st.slider("빈 개수(bins)", 5, 50, 10)
                fig, ax = plt.subplots()
                ax.hist(df[col].dropna(), bins=bins, color='skyblue', edgecolor='black')
                ax.set_title(f"{col} 히스토그램")
                ax.set_xlabel(col)
                ax.set_ylabel("빈도")
                st.pyplot(fig)

    elif selected_graph == "막대그래프":
        with st.expander("막대그래프 변수 선택"):
            cat_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()
            num_cols = df.select_dtypes(include=np.number).columns.tolist()
            if not cat_cols or not num_cols:
                st.warning("범주형/수치형 변수가 모두 필요합니다.")
            else:
                cat_col = st.selectbox("범주형 변수 선택 (x축)", cat_cols, key="bar_cat")
                num_col = st.selectbox("수치형 변수 선택 (y축)", num_cols, key="bar_num")
                agg = st.selectbox("집계 방식", ["평균", "합계", "최대", "최소"])
                if agg == "평균":
                    data = df.groupby(cat_col)[num_col].mean()
                elif agg == "합계":
                    data = df.groupby(cat_col)[num_col].sum()
                elif agg == "최대":
                    data = df.groupby(cat_col)[num_col].max()
                else:
                    data = df.groupby(cat_col)[num_col].min()
                fig, ax = plt.subplots()
                data.plot(kind="bar", ax=ax, color='orange', edgecolor='black')
                ax.set_title(f"{cat_col}별 {num_col} {agg}")
                ax.set_xlabel(cat_col)
                ax.set_ylabel(f"{num_col} ({agg})")
                st.pyplot(fig)

    elif selected_graph == "산점도":
        with st.expander("산점도 변수 선택"):
            num_cols = df.select_dtypes(include=np.number).columns.tolist()
            if len(num_cols) < 2:
                st.warning("수치형 변수가 2개 이상 필요합니다.")
            else:
                x_col = st.selectbox("x축 변수", num_cols, key="scatter_x")
                y_col = st.selectbox("y축 변수", [c for c in num_cols if c != x_col], key="scatter_y")
                fig, ax = plt.subplots()
                ax.scatter(df[x_col], df[y_col], alpha=0.7, color='green')
                ax.set_title(f"{x_col} vs {y_col} 산점도")
                ax.set_xlabel(x_col)
                ax.set_ylabel(y_col)
                st.pyplot(fig)

    elif selected_graph == "상자그림":
        with st.expander("상자그림 변수 선택"):
            num_cols = df.select_dtypes(include=np.number).columns.tolist()
            if not num_cols:
                st.warning("수치형 변수가 없습니다.")
            else:
                cols = st.multiselect("상자그림을 그릴 변수(복수 선택 가능)", num_cols, default=num_cols[:1], key="box")
                if cols:
                    fig, ax = plt.subplots()
                    ax.boxplot([df[c].dropna() for c in cols], labels=cols)
                    ax.set_title(f"상자그림: {', '.join(cols)}")
                    st.pyplot(fig)
                else:
                    st.info("변수를 1개 이상 선택하세요.")

else:
    st.info("먼저 성적 데이터 CSV 파일을 업로드하세요.")
