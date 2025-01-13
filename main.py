from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer 
from tkinter import *

# Function for clearing the contents of all entry boxes and text area.
def clearAll() : 

	# deleting the content from the entry box 
	negativeField.delete(0, END) 
	neutralField.delete(0, END) 
	positiveField.delete(0, END) 
	overallField.delete(0, END) 

	# whole content of text area is deleted 
	textArea.delete(1.0, END)
	
# function to print sentiments of the sentence. 
def detect_sentiment():

	# get input
	sentence = textArea.get("1.0", "end")

	# SentimentIntensityAnalyzer object 
	sid_obj = SentimentIntensityAnalyzer() 

	# polarity_scores method of SentimentIntensityAnalyzer object gives a sentiment dictionary. Which contains pos, neg, neu, and compound scores. 
	sentiment_dict = sid_obj.polarity_scores(sentence) 

	string = str(sentiment_dict['neg']*100) + "% Negative"
	negativeField.insert(10, string)
	

	string = str(sentiment_dict['neu']*100) + "% Neutral"
	neutralField.insert(10, string)

	string = str(sentiment_dict['pos']*100) +"% Positive"
	positiveField.insert(10, string)
	
	# decide sentiment as positive, negative and neutral 
	if sentiment_dict['compound'] >= 0.05 :
		string = "Positive"

	elif sentiment_dict['compound'] <= - 0.05 :
		string = "Negative"
	

	else :
		string = "Neutral"

	overallField.insert(10, string)
		


if __name__ == "__main__" :
	

	# GUI 
	gui = Tk() 
	
	# background colour of GUI 
	gui.config(background = "light green") 

	# name of GUI window 
	gui.title("Sentiment Detector") 

	# configuration of GUI window 
	gui.geometry("250x400") 

	# label
	enterText = Label(gui, text = "Enter Your Sentence",
									bg = "light green")

	# a text area for the root 
	textArea = Text(gui, height = 5, width = 25, font = "lucida 13")

	# create a Submit Button and place into the root window 
	check = Button(gui, text = "Check Sentiment", fg = "Black", 
						bg = "Red", command = detect_sentiment)

	negative = Label(gui, text = "sentence was rated as: ",
										bg = "light green") 

	neutral = Label(gui, text = "sentence was rated as: ", 
									bg = "light green") 

	positive = Label(gui, text = "sentence was rated as: ",
										bg = "light green")

	overall = Label(gui, text = "Sentence Overall Rated As: ",
										bg = "light green")
	# text entry box 
	negativeField = Entry(gui)

	neutralField = Entry(gui)

	positiveField = Entry(gui)

	overallField = Entry(gui) 

	clear = Button(gui, text = "Clear", fg = "Black", 
					bg = "Red", command = clearAll)
	 
	Exit = Button(gui, text = "Exit", fg = "Black", 
						bg = "Red", command = exit)

	# grid method for placing the widgets at respective positions in table like structure
	enterText.grid(row = 0, column = 2)
	
	textArea.grid(row = 1, column = 2, padx = 10, sticky = W)
	
	check.grid(row = 2, column = 2)
	
	negative.grid(row = 3, column = 2)
	
	neutral.grid(row = 5, column = 2)
	
	positive.grid(row = 7, column = 2)
	
	overall.grid(row = 9, column = 2)
	
	negativeField.grid(row = 4, column = 2)

	neutralField.grid(row = 6, column = 2)
					
	positiveField.grid(row = 8, column = 2)
	
	overallField.grid(row = 10, column = 2)
	
	clear.grid(row = 11, column = 2)
	
	Exit.grid(row = 12, column = 2)

	# start the GUI 
	gui.mainloop() 
	
