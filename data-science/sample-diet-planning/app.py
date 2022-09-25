from dietkit import *
import streamlit as st
from PIL import Image
import plotly.graph_objects as go
import matplotlib
import seaborn
import pandas

st.title('AI Diet Creator')
st.write(''' This model is for all who have a problem with their eat and their meal and want to change their life,
             with our model you don't need to be an expert or go to doctors you just 'll input your data and let us \
            create your diet depending on your body type''')

image = Image.open('img.png')
st.image(image)
st.header('Create your own diet plan')
age = st.slider('Select age', 1, 100)
H = st.number_input('Height')
W = st.number_input('Weight')
days = st.slider('Select diet days', 1, 7, 4)
# Dietkitst
sample_ingredients = load_ingredient(sample_language='eng')
sample_menus = load_menu(ingredients=sample_ingredients, sample_language='eng')
sample_diets = load_diet(menus=sample_menus, num_loads=days, sample_language='eng', sample_name='ML')
# / DietKit

submit = st.button('Submit')
if submit:
    st.write("your meals for next ", days, 'days')
    st.success('Saved', icon="✅")


    def convert_df(df):
        data = pd.DataFrame(df)
        return data.to_csv().encode('utf-8')


    def convert_df_2(df):
        data = pd.DataFrame.from_dict(df, orient='index')
        return data.to_csv().encode('utf-8')


    meals_csv = convert_df(sample_diets.plan)
    ing_csv = convert_df_2(sample_diets.ingredient)
    nutrition_csv = convert_df_2(sample_diets.nutrition)

    st.download_button(
        label="Download your diet meals",
        data=meals_csv,
        file_name='meals_csv.csv',
    )
    st.download_button(
        label="Download your diet ingredients of the meals",
        data=ing_csv,
        file_name='ingredients_csv.csv',
    )
    st.download_button(
        label="Download nutrition of your diet meals",
        data=nutrition_csv,
        file_name='nutrition_csv.csv'
    )
    # st.balloons()
st.subheader('View your diet')
select_day = st.slider('Select the day', 1, days)

st.write(f'View Menu of day {select_day}')
Menu = st.button('Menu')
if Menu:
    data = sample_diets.plan[select_day - 1]
    st.write(data)

st.write(f'Ingredients of Menu of day {select_day}')
ing = st.button('Ingredients')
if ing:
    data_ing = sample_diets.ingredient[select_day - 1]
    st.write(data_ing)

st.write(f'Nutrition Values for Menu of day {select_day}')
nut = st.button('Nutrition Values')
if nut:
    data_nut = sample_diets.nutrition[select_day - 1]
    # The plot
    fig = go.Figure(
        go.Pie(
            labels=list(data_nut.keys()),
            values=list(data_nut.values()),
            hoverinfo="label+percent",
            textinfo="value"
        ))

    st.subheader("Pie chart")

    st.plotly_chart(fig)
    st.write(data_nut)

