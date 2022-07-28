import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

# Create menu with title, headers and text
streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

#Create Special Menu
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#import fruit list from Amazon S3 Bucket
#import pandas
my_fruit_list = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')

#add fruit picklist for users to choose fruits
fruits_selected = streamlit.multiselect('Pick some fruits:', list(my_fruit_list.index),['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display fruit list
streamlit.dataframe(fruits_to_show)

#New section to display fruitvice api response
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    #import requests
    fruityvice_response = requests.get("https://www.fruityvice.com/api/fruit/" + fruit_choice)
    # normalize json response
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    # output response as table
    streamlit.dataframe(fruityvice_normalized)
except URLError as e:
  streamlit.error()



#STOP TO TROUBLESHOOT
streamlit.stop()

# snowflake connector
#import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * FROM fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

#Allow the end user to add a fruit to the list
add_my_fruit = streamlit.text_input('What fruit would you like to add?')
streamlit.write('Thanks for adding ' + add_my_fruit + '!')

my_cur.execute("insert into fruit_load_list values ('from streamlit')")




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

