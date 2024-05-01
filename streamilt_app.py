# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col
import pandas as pd

# Write directly to the app
st.title("Zena's Amazing Athleisure Catalog")
st.write(
    """Pick a sweatsuit color or style:
    """
)

# Get the current credentials
session = get_active_session()
my_catlog=session.table('catalog_for_website').select(col('COLOR_OR_STYLE'))

option=st.selectbox('enter',my_catlog)

# We'll build the image caption now, since we can
product_caption = 'Our warm, comfortable, ' + option + ' sweatsuit!'

ans=session.table('catalog_for_website').filter(col('COLOR_OR_STYLE')==option)
#st.write(ans)
p_df=ans.to_pandas()
#st.write(p_df)
#df2 = session.fetchone()


#st.write(p_df['DIRECT_URL'].iloc[0])
st.image(p_df['DIRECT_URL'].iloc[0],width=400,caption=product_caption)

st.write('Price:',p_df['PRICE'].iloc[0])
st.write('Sizes Available::',p_df['SIZE_LIST'].iloc[0])
st.write(p_df['UPSELL_PRODUCT_DESC'].iloc[0])
