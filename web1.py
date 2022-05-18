import os
import pandas as pd
from tkinter import *
from tkcalendar import Calendar

'''# creating an object of tkinter

tkobj = Tk()

# setting up the geomentry

tkobj.geometry("400x400")
tkobj.title("Calendar picker")
#creating a calender object

tkc = Calendar(tkobj,selectmode = "day",year=2022,month=1,date=1)

#display on main window
tkc.pack(pady=40)

# getting date from the calendar

def fetch_date():
    date.config(text = "Selected Date is: " + tkc.get_date())

#add button to load the date clicked on calendar

but = Button(tkobj,text="Select Date",command=fetch_date, bg="black", fg='white')
#displaying button on the main display
but.pack()
#Label for showing date on main display
date = Label(tkobj,text="",bg='black',fg='white')
date.pack(pady=20)
#starting the object
tkobj.mainloop()'''

#main code (trying to rework this into this)

tweet_count = input("How many tweets do you want? ")
text_query = input("Enter the keyword of which tweets you want: ")
since_date = input("Enter the date from which you want the tweets (YY-MM-DD): ")
until_date = input("Enter the date to until you want the tweets (YY-MM-DD): ")

os.system('snscrape --jsonl --max-results {} --since {} twitter-search "{} until:{}"> text-query-tweets.json'.format(tweet_count, since_date, text_query, until_date))

tweets_df2 = pd.read_json('text-query-tweets.json', lines=True)
tweets_df2.head()

tweets_df2.to_csv('text-query-tweets.csv', sep=',', index=True)