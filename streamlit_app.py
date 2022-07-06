import streamlit

# Create menu with title, headers and text
streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

#Create Special Menu
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#--------------- OLD VERSION ----------------
#import streamlit
#import pandas
#
## Create menu with title, headers and text
#streamlit.title('My Parents New Healthy Diner')
#
#streamlit.header('Breakfast Menu')
#streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
#streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
#streamlit.text('🐔 Hard-Boiled Free-Range Egg')
#streamlit.text('🥑🍞 Avocado Toast')
#
#streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
#
## import fruit data into a table from csv using pandas
#my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#my_fruit_list = my_fruit_list.set_index('Fruit')
#
## create picklist for users to select the fruits for the smoothie
#fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
#fruits_to_show = my_fruit_list.loc[fruits_selected]
#
#
## display table on the page
#streamlit.dataframe(fruits_to_show)

