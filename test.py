from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode
import streamlit as st
import pandas as pd

# Dummy DataFrame (replace with your BigQuery DataFrame)
df = pd.DataFrame({
    'id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie'],
    'score': [85, 90, 95]
})

# Streamlit write to help debug
st.write("Data in table:")
st.dataframe(df)

# AgGrid Config
gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_selection(selection_mode='multiple', use_checkbox=True)
grid_options = gb.build()

# AgGrid Display
grid_response = AgGrid(
    df,
    gridOptions=grid_options,
    update_mode=GridUpdateMode.SELECTION_CHANGED,
    enable_enterprise_modules=False,
    height=300,
    theme='streamlit',
    fit_columns_on_grid_load=True
)

# Debug log
st.write("Raw Grid Response:", grid_response)

# Get selected rows
selected_rows = grid_response['selected_rows']

if selected_rows:
    st.success("You selected these rows:")
    st.write(selected_rows)
else:
    st.warning("No rows selected yet.")
