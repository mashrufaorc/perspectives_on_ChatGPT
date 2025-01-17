# -*- coding: utf-8 -*-
"""412 asg.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LPOFyt-HvaIr8yZd4m-Al0vTldy4vfwi
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from google.colab import files

#reading and opening file
uploaded = files.upload()
data= pd.read_csv("chatgpt.csv", delimiter=",")
# Note: Need to upload the chatgpt.csv file and run this block first!

# question 1 = Have you had any experience with ChatGPT?
# question 1 code processing
# comparing academic status with experience with chatgpt

# all lists needed
options= ["High", "Medium", "Low"]
undergrad = [0, 0, 0] #in the format yes, maybe, no
college = [0, 0, 0]
prof= [0, 0, 0]
phd = [0, 0, 0]

diff_statuses = ["Undergraduate (Bachelor's)", "College Student", "Professor", "PhD"]
status_list= [undergrad, college, prof, phd]

# traversing through the data 4 times bc thats how long our status_list is
for j in range(4):
  # iterating for the amount of responses we have
  for i in range(106):
    if data.at[i, "ACADEMIC STATUS"] == diff_statuses[j]:
      if data.at[i, "Have you had any experience with ChatGPT?"]=="Yes":
        status_list[j][0] +=1
      elif data.at[i, "Have you had any experience with ChatGPT?"] =="Some":
        status_list[j][1] +=1
      elif data.at[i, "Have you had any experience with ChatGPT?"]=="No":
        status_list[j][2] +=1


# graphing
fig = plt.figure()
myaxes= fig.add_axes([0.1, 0.1, 1.6, 1.6])
myaxes.plot(options, undergrad, '#DA9E6C', lw=2.5, label= "Undergraduate")
myaxes.plot(options, college, '#6CDA7F', lw=2.5, label= "College Student")
myaxes.plot(options, phd, '#DF6FA6', lw=2.5, label= "PhD")
myaxes.plot(options, prof, "#916FDF", lw=2.5, label= "Professor")
myaxes.legend(title= "Academic Status")
myaxes.set_xlabel("Level of Experience")
myaxes.set_ylabel("Number Of Responses")
myaxes.set_title("Experience of ChatGPT Amongst Varying Academic Statuses")
plt.show()

# question 2 = Does ChatGPT Limit Creativity?
# question 2 code processing
# comparing ChatGPTS impact on creativity with various fields of studies

# all lists needed
options= ["Yes", "A Little", "No"]
compsci = [0, 0, 0] #in the format yes, a little, no
sci = [0, 0, 0]
eng= [0, 0, 0]
law = [0, 0, 0]
business = [0, 0, 0]
humanities = [0, 0, 0]
arts = [0, 0, 0]
other = [0, 0, 0]


diff_statuses = ["Computer Science", "Sciences", "Engineering", "Law", "Business", "Humanities", "Arts", "Other"]
status_list= [compsci, sci, eng, law, business, humanities, arts, other]

# traversing through the data 7 times bc thats how long our status_list is
for j in range(7):
  for i in range(106):
    if data.at[i, "FIELD OF STUDY"] == diff_statuses[j]:
      if data.at[i, "Have you had any experience with ChatGPT?"]=="Yes":
        status_list[j][0] +=1
      elif data.at[i, "Have you had any experience with ChatGPT?"] =="A little ":
        status_list[j][1] +=1
      elif data.at[i, "Have you had any experience with ChatGPT?"]=="No":
        status_list[j][2] +=1


# graphing
fig = plt.figure()
myaxes= fig.add_axes([0.1, 0.1, 1.6, 1.6])
myaxes.plot(options, compsci, "#F69F06", lw=2.5, label= "Computer Science")
myaxes.plot(options, sci, "#45ACB4", lw=2.5, label= "Sciences")
myaxes.plot(options, eng, "#4579B4", lw=2.5, label= "Engineering")
myaxes.plot(options, law, "#9051A5", lw=2.5, label= "Law")
myaxes.plot(options, business, "#A55156", lw=2.5, label= "Business")
myaxes.plot(options, humanities, "#9B6A6D", lw=2.5, label= "Humanities")
myaxes.plot(options, arts, "#E198DC", lw=2.5, label= "Arts")
myaxes.plot(options, other, "#98A2E1", lw=2.5, label= "Other")

myaxes.legend(title = "Fields of Study")
myaxes.set_xlabel("Level of Experience")
myaxes.set_ylabel("Number Of Responses")
myaxes.set_title("Experience with AI tools According to Various Fields of Study")
plt.show()

# question 3 = Do You Think ChatGPT is Considered Plagiarism?
# question 3 code processing
# evaluating whether chagpt is seen as plagiarism across different age groups
# all lists needed
options= ["Yes", "A Little", "No"]
age18_21 = [0, 0, 0] #in the format yes, maybe, no
age21_24 = [0, 0, 0]
age24_29 = [0, 0, 0]
age30 = [0, 0, 0]

diff_statuses = ["18-21", "21-24", "24-29", "30"]
status_list= [age18_21, age21_24, age24_29, age30]

# traversing through the data 4 times bc thats how long our status_list is
for j in range(4):
  for i in range(106):
    if data.at[i, "AGE"] == diff_statuses[j]:
      if data.at[i, "Do You Think ChatGPT is Considered Plagiarism?"]=="Yes":
        status_list[j][0] +=1
      elif data.at[i, "Do You Think ChatGPT is Considered Plagiarism?"] =="Maybe":
        status_list[j][1] +=1
      elif data.at[i, "Do You Think ChatGPT is Considered Plagiarism?"]=="No":
        status_list[j][2] +=1


# graphing
fig = plt.figure()
myaxes= fig.add_axes([0.1, 0.1, 1.6, 1.6])
myaxes.plot(options, age18_21, "#BAB96F", lw=2.5, label= "18-21")
myaxes.plot(options, age21_24, "#305781", lw=2.5, label= "21-24")
myaxes.plot(options, age24_29, "#BD506D", lw=2.5, label= "24-29")
myaxes.plot(options, age30, "#629865", lw=2.5, label= "30+")

myaxes.legend(title= "Age Groups")
myaxes.set_xlabel("Degree to how much ChatGPT Should be Considered Plagiarism")
myaxes.set_ylabel("Number Of Responses")
myaxes.set_title("Whether ChatGPT Should be Considered Plagiarism According to Various Age Groups")
plt.show()

# question 2 = Do You Think ChatGPT limits creativity
# question 2 code processing
# evaluating whether chagpt limits creativity according to various age groups
# all lists needed
options= ["Yes", "A Little", "No"]
age18_21 = [0, 0, 0] #in the format yes, maybe, no
age21_24 = [0, 0, 0]
age24_29 = [0, 0, 0]
age30 = [0, 0, 0]

diff_statuses = ["18-21", "21-24", "24-29", "30"]
status_list= [age18_21, age21_24, age24_29, age30]

# traversing through the data 4 times bc thats how long our status_list is
for j in range(4):
  for i in range(106):
    if data.at[i, "AGE"] == diff_statuses[j]:
      if data.at[i, "Does ChatGPT Limit Creativity?"]=="Yes":
        status_list[j][0] +=1
      elif data.at[i, "Does ChatGPT Limit Creativity?"] =="A little":
        status_list[j][1] +=1
      elif data.at[i, "Does ChatGPT Limit Creativity?"]=="No":
        status_list[j][2] +=1


# graphing
fig = plt.figure()
myaxes= fig.add_axes([0.1, 0.1, 1.6, 1.6])
myaxes.plot(options, age18_21, "#BAB96F", lw=2.5, label= "18-21")
myaxes.plot(options, age21_24, "#305781", lw=2.5, label= "21-24")
myaxes.plot(options, age24_29, "#BD506D", lw=2.5, label= "24-29")
myaxes.plot(options, age30, "#629865", lw=2.5, label= "30+")

myaxes.legend(title= "Age Groups")
myaxes.set_xlabel("Degree to how much ChatGPT limits creativity")
myaxes.set_ylabel("Number Of Responses")
myaxes.set_title("Whether ChatGPT Limits Creativity According to Various Age Groups")
plt.show()

# question 4 = Should The Information You Get From ChatGPT Be Considered Reliable/Unbiased?
# question 4 code processing
# evaluating the degree to which information from chagpt should be considered reliable according to various fields of studies

# all lists needed
options= ["Very Reliable", "Somewhat Reliable", "Not Reliable"]
compsci = [0, 0, 0] #in the format yes, a little, no
sci = [0, 0, 0]
eng= [0, 0, 0]
law = [0, 0, 0]
business = [0, 0, 0]
humanities = [0, 0, 0]
arts = [0, 0, 0]
other = [0, 0, 0]


diff_statuses = ["Computer Science", "Sciences", "Engineering", "Law", "Business", "Humanities", "Arts", "Other"]
status_list= [compsci, sci, eng, law, business, humanities, arts, other]

# traversing through the data 7 times bc thats how long our status_list is
for j in range(7):
  for i in range(106):
    if data.at[i, "FIELD OF STUDY"] == diff_statuses[j]:
      if data.at[i, "Should The Information You Get From ChatGPT Be Considered Reliable/Unbiased?"]=="Yes":
        status_list[j][0] +=1
      elif data.at[i, "Should The Information You Get From ChatGPT Be Considered Reliable/Unbiased?"] =="Sometimes":
        status_list[j][1] +=1
      elif data.at[i, "Should The Information You Get From ChatGPT Be Considered Reliable/Unbiased?"]=="No":
        status_list[j][2] +=1



# graphing
fig = plt.figure()
myaxes= fig.add_axes([0.1, 0.1, 1.6, 1.6])
myaxes.plot(options, compsci, "#45B47D", lw=2.5, label= "Computer Science")
myaxes.plot(options, sci, "#EA6161", lw=2.5, label= "Sciences")
myaxes.plot(options, eng, "#EA9961", lw=2.5, label= "Engineering")
myaxes.plot(options, law, "#EADB61", lw=2.5, label= "Law")
myaxes.plot(options, business, "#61D9EA", lw=2.5, label= "Business")
myaxes.plot(options, humanities, "#618BEA", lw=2.5, label= "Humanities")
myaxes.plot(options, arts, "#4E0E46", lw=2.5, label= "Arts")
myaxes.plot(options, other, "#EA61D5", lw=2.5, label= "Other")

myaxes.legend(title= "Fields of Study")
myaxes.set_xlabel("Degree to how much ChatGPT Should be Considered Reliable")
myaxes.set_ylabel("Number Of Responses")
myaxes.set_title("Whether Information from ChaGPT should be Considered Reliable According to Various Fields of Study")
plt.show()

# question 5 = How Comfortable Do You Feel with the Widespread use of ChatGPT and Other AI Tools in Society?
# question 5 code processing
# evaluating the degree of Comfortability towards ChatGPT and Other AI Tools in Society According to various fields of Study

# all lists needed
options= ["Very comfortable", "Uncomfortable", "Not sure"]
compsci = [0, 0, 0] #in the format very comfortable, uncofortable, not sure
sci = [0, 0, 0]
eng= [0, 0, 0]
law = [0, 0, 0]
business = [0, 0, 0]
humanities = [0, 0, 0]
arts = [0, 0, 0]
other = [0, 0, 0]


diff_statuses = ["Computer Science", "Sciences", "Engineering", "Law", "Business", "Humanities", "Arts", "Other"]
status_list= [compsci, sci, eng, law, business, humanities, arts, other]

# traversing through the data 7 times bc thats how long our status_list is
for j in range(7):
  for i in range(106):
    if data.at[i, "FIELD OF STUDY"] == diff_statuses[j]:
      if data.at[i, "How Comfortable Do You Feel with the Widespread use of ChatGPT and Other AI Tools in Society? "]=="Very comfortable":
        status_list[j][0] +=1
      elif data.at[i, "How Comfortable Do You Feel with the Widespread use of ChatGPT and Other AI Tools in Society? "] =="Uncomfortable":
        status_list[j][1] +=1
      elif data.at[i, "How Comfortable Do You Feel with the Widespread use of ChatGPT and Other AI Tools in Society? "]=="Not sure":
        status_list[j][2] +=1



# graphing
fig = plt.figure()
myaxes= fig.add_axes([0.1, 0.1, 1.6, 1.6])
myaxes.plot(options, compsci, "#9C0085", lw=2.5, label= "Computer Science")
myaxes.plot(options, sci, "#D58C9D", lw=2.5, label= "Sciences")
myaxes.plot(options, eng, "#00349C", lw=2.5, label= "Engineering")
myaxes.plot(options, law, "#670A85", lw=2.5, label= "Law")
myaxes.plot(options, business, "#009C50", lw=2.5, label= "Business")
myaxes.plot(options, humanities, "#E3335B", lw=2.5, label= "Humanities")
myaxes.plot(options, arts, "#5C55B4", lw=2.5, label= "Arts")
myaxes.plot(options, other, "#EA61D5", lw=2.5, label= "Other")

myaxes.legend(title= "Field of Study")
myaxes.set_xlabel("Degree of Comfortability towards ChatGPT and Other AI Tools in Society")
myaxes.set_ylabel("Number Of Responses")
myaxes.set_title("Degree of Comfort Towards AI Tools in Society According to Various Fields of Study")
plt.show()

# question 5 = How Comfortable Do You Feel with the Widespread use of ChatGPT and Other AI Tools in Society?
# question 5 code processing
# evaluating the degree of Comfortability towards ChatGPT and Other AI Tools in Society According to age

# all lists needed
options= ["Very comfortable", "Uncomfortable", "Not sure"]
age18_21 = [0, 0, 0] #in the Very comfortabl, uncomfortable, not sure
age21_24 = [0, 0, 0]
age24_29 = [0, 0, 0]
age30 = [0, 0, 0]

diff_statuses = ["18-21", "21-24", "24-29", "30"]
status_list= [age18_21, age21_24, age24_29, age30]

# traversing through the data 4 times bc thats how long our status_list is
for j in range(4):
  for i in range(106):
    if data.at[i, "AGE"] == diff_statuses[j]:
      if data.at[i, "How Comfortable Do You Feel with the Widespread use of ChatGPT and Other AI Tools in Society? "]=="Very comfortable":
        status_list[j][0] +=1
      elif data.at[i, "How Comfortable Do You Feel with the Widespread use of ChatGPT and Other AI Tools in Society? "] =="Uncomfortable":
        status_list[j][1] +=1
      elif data.at[i, "How Comfortable Do You Feel with the Widespread use of ChatGPT and Other AI Tools in Society? "]=="Not sure":
        status_list[j][2] +=1


# graphing
fig = plt.figure()
myaxes= fig.add_axes([0.1, 0.1, 1.6, 1.6])
myaxes.plot(options, age18_21, "#8D1212", lw=2.5, label= "18-21")
myaxes.plot(options, age21_24, "#546B0A", lw=2.5, label= "21-24")
myaxes.plot(options, age24_29, "#0A6B48", lw=2.5, label= "24-29")
myaxes.plot(options, age30, "#0A146B", lw=2.5, label= "30+")

myaxes.legend(title= "Age Groups")
myaxes.set_xlabel("Degree of Comfortability towards ChatGPT and Other AI Tools in Society")
myaxes.set_ylabel("Number Of Responses")
myaxes.set_title("Degree of Comfort Towards AI Tools in Society According to Various Age Groups")
plt.show()

# question 6 = Do You Think ChatGPT Will Benefit Academics in The Future?
# question 6 code processing
# evaluating how beneficial chatGPT would be to academia in the future according to Undergrad Students in different Years of Study

# all lists needed
options= ["Very Beneficial", "Somewhat Beneficial", "Not Beneficial"]
yr1 = [0, 0, 0] #in the Very comfortable, uncomfortable, not sure
yr2 = [0, 0, 0]
yr3 = [0, 0, 0]
yr4 = [0, 0, 0]
yr5 = [0, 0, 0]

diff_statuses = ["First Year", "Second Year", "Third Year", "Fourth Year","Fifth Year+"]
status_list= [yr1, yr2, yr3, yr4, yr5]

# traversing through the data 5 times bc thats how long our status_list is
for j in range(5):
  for i in range(106):
    if data.at[i, "ACADEMIC STATUS"] == "Undergraduate (Bachelor's)" and data.at[i, "YEAR OF STUDY"] == diff_statuses[j]:
      if data.at[i, "Do You Think ChatGPT Will Benefit Academics in The Future?"]=="Yes":
        status_list[j][0] +=1
      elif data.at[i, "Do You Think ChatGPT Will Benefit Academics in The Future?"] =="Maybe":
        status_list[j][1] +=1
      elif data.at[i, "Do You Think ChatGPT Will Benefit Academics in The Future?"]=="No":
        status_list[j][2] +=1


# graphing
fig = plt.figure()
myaxes= fig.add_axes([0.1, 0.1, 1.6, 1.6])
myaxes.plot(options, yr1, "#8D1212", lw=2.5, label= "1st Year")
myaxes.plot(options, yr2, "#48920E", lw=2.5, label= "2nd Year")
myaxes.plot(options, yr3, "#9C6360", lw=2.5, label= "3rd Year")
myaxes.plot(options, yr4, "#0A146B", lw=2.5, label= "4th Year")
myaxes.plot(options, yr5, "#6F72A0", lw=2.5, label= "5th Year+")


myaxes.legend(title= "Year of Undergrad Study")
myaxes.set_xlabel("Degree of how Much ChatGPT will be Beneficial to Academia In the Future")
myaxes.set_ylabel("Number Of Responses")
myaxes.set_title("Benefit of ChatGPT to Academia in the Future According to Undergraduate Students in Different Years of Study")
plt.show()

# question 7 = Would You Recommend ChatGPT to Other Students?
# question 7 code processing
# evaluating whether Undergrad students in different years would recommend chatgpt to other students

# all lists needed
options= ["Would Recommend", "Would Maybe Recommend", "Would Not Recommend"]
yr1 = [0, 0, 0] #in the format would recommend, maybe recommend, and would not recommend
yr2 = [0, 0, 0]
yr3 = [0, 0, 0]
yr4 = [0, 0, 0]
yr5 = [0, 0, 0]

diff_statuses = ["First Year", "Second Year", "Third Year", "Fourth Year","Fifth Year+"]
status_list= [yr1, yr2, yr3, yr4, yr5]

# traversing through the data 5 times bc thats how long our status_list is
for j in range(5):
  for i in range(106):
    if data.at[i, "ACADEMIC STATUS"] == "Undergraduate (Bachelor's)" and data.at[i, "YEAR OF STUDY"] == diff_statuses[j]:
      if data.at[i, "Would You Recommend ChatGPT to Other Students?"]=="Yes":
        status_list[j][0] +=1
      elif data.at[i, "Would You Recommend ChatGPT to Other Students?"] =="Maybe":
        status_list[j][1] +=1
      elif data.at[i, "Would You Recommend ChatGPT to Other Students?"]=="No":
        status_list[j][2] +=1


# graphing
fig = plt.figure()
myaxes= fig.add_axes([0.1, 0.1, 1.6, 1.6])
myaxes.plot(options, yr1, "#8D1212", lw=2.5, label= "1st Year")
myaxes.plot(options, yr2, "#7FCDC6", lw=2.5, label= "2nd Year")
myaxes.plot(options, yr3, "#9C6360", lw=2.5, label= "3rd Year")
myaxes.plot(options, yr4, "#0A146B", lw=2.5, label= "4th Year")
myaxes.plot(options, yr5, "#9294AD", lw=2.5, label= "5th Year+")


myaxes.legend(title= "Year of Undergrad Study")
myaxes.set_xlabel("Degree to How Much Undergrad Students Would Recommend ChatGPT")
myaxes.set_ylabel("Number Of Responses")
myaxes.set_title("Whether Undergraduate Students in Various Years would Recommend ChatGPT to Others")
plt.show()

# question 7 = Would You Recommend ChatGPT to Other Students?
# question 7 code processing
# evaluating whether different academic statuses would recommend chatgpt to other students

# all lists needed
options= ["Would Recommend", "Would Maybe Recommend", "Would Not Recommend"]
undergrad = [0, 0, 0] #in the format would recommend, would maybe recommend and would not recommend
college = [0, 0, 0]
prof= [0, 0, 0]
phd = [0, 0, 0]

diff_statuses = ["Undergraduate (Bachelor's)", "College Student", "Professor", "PhD"]
status_list= [undergrad, college, prof, phd]

# traversing through the data 4 times bc thats how long our status_list is
for j in range(4):
  # iterating for the amount of responses we have
  for i in range(106):
    if data.at[i, "ACADEMIC STATUS"] == diff_statuses[j]:
      if data.at[i, "Would You Recommend ChatGPT to Other Students?"]=="Yes":
        status_list[j][0] +=1
      elif data.at[i, "Would You Recommend ChatGPT to Other Students?"] =="Maybe":
        status_list[j][1] +=1
      elif data.at[i, "Would You Recommend ChatGPT to Other Students?"]=="No":
        status_list[j][2] +=1


# graphing
fig = plt.figure()
myaxes= fig.add_axes([0.1, 0.1, 1.6, 1.6])
myaxes.plot(options, undergrad, '#DA9E6C', lw=2.5, label= "Undergraduate")
myaxes.plot(options, college, '#6CDA7F', lw=2.5, label= "College Student")
myaxes.plot(options, phd, '#DF6FA6', lw=2.5, label= "PhD")
myaxes.plot(options, prof, "#916FDF", lw=2.5, label= "Professor")
myaxes.legend(title= "Academic Status")
myaxes.set_xlabel("Degree to How Much Various Academic Statuses Would Recommend ChatGPT")
myaxes.set_ylabel("Number Of Responses")
myaxes.set_title("Degree of Recommendation of ChatGPT According to Various Academic Statuses")
plt.show()