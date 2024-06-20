import pandas as pd
import re
import streamlit as st


# エクセルファイルの読み込み
def load_excel(file):
    return pd.read_excel(file, sheet_name='Sheet1')

def make_patterns(clean_dict):
    return {key: re.compile(value) for key, value in clean_dict.items()}

def make_key_list(clean_dict):
    return list(clean_dict.keys())

def move_values_to_correct_columns(df, patterns, key_list):
    # 各行を確認し、適切なカラムに値を割り当てる
    for index, row in df.iterrows():
        values = row[key_list].dropna().values
        for value in values:
            for key, pattern in patterns.items():
                if pattern.search(value):
                    df.at[index, key] = value
    return df


def clean_content(df, column_name, pattern):
    # 列の値がpatternsで始まらない場合、その値を空白にする
    for index, row in df.iterrows():
        if pd.notna(row[column_name]) and not row[column_name].startswith(pattern):
            df.at[index, column_name] = ''
    
    return df


st.title("Excel Data Cleaner")
uploaded_file = st.file_uploader("Choose an Excel file", type="xlsx")


if uploaded_file is not None:
    df = load_excel(uploaded_file)

    st.write("Please provide the cleaning patterns for each column:")
    
    clean_dict = {}
    
    num_pairs = st.number_input('Number of key-value pairs', min_value=1, max_value=20, value=7)

    for i in range(num_pairs):
        key = st.text_input(f"Key {i+1}", "")
        value = st.text_input(f"Value {i+1}", "")
        if key and value:
            clean_dict[key] = value

    if st.button("Clean Data"):
        if clean_dict:
            key_list = make_key_list(clean_dict)
            patterns = make_patterns(clean_dict)

            # 値を適切な位置に移動
            df = move_values_to_correct_columns(df, patterns, key_list)

            for key, value in clean_dict.items():
                df = clean_content(df, key, value)


            st.write("Cleaned Data:")
            st.dataframe(df)

            # Cleaned file download
            output_file_path = 'cleaned_data.xlsx'
            df.to_excel(output_file_path, index=False)

            with open(output_file_path, "rb") as file:
                st.download_button(
                    label="Download cleaned Excel file",
                    data=file,
                    file_name="cleaned_data.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
        else:
            st.error("Please provide valid key-value pairs.")