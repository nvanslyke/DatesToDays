from tkinter import *


root = Tk()
root.title("Dates to Days")
root.geometry("300x500")
#root.iconbitmap('Calendar.ico')

def dayOfWeek():
 
    yearCode = (((int(yearBox.get()) % 100) // 4)+ int(yearBox.get()) % 100) % 7 
    if monthBox.get(monthBox.curselection()) == "January":
        monthCode = 0
    elif monthBox.get(monthBox.curselection()) == "Febuary":
        monthCode = 3
    elif monthBox.get(monthBox.curselection()) == "March":
        monthCode = 3
    elif monthBox.get(monthBox.curselection()) == "April":
        monthCode = 6
    elif monthBox.get(monthBox.curselection()) == "May":
        monthCode = 1
    elif monthBox.get(monthBox.curselection()) == "June":
        monthCode = 4
    elif monthBox.get(monthBox.curselection()) == "July":
        monthCode = 6
    elif monthBox.get(monthBox.curselection()) == "August":
        monthCode = 2
    elif monthBox.get(monthBox.curselection()) == "September":
        monthCode = 5
    elif monthBox.get(monthBox.curselection()) == "October":
        monthCode = 0
    elif monthBox.get(monthBox.curselection()) == "November":
        monthCode = 3
    elif monthBox.get(monthBox.curselection()) == "December":
        monthCode = 5

    if int(yearBox.get()) // 100 == 17:
        centuryCode = 4
    elif int(yearBox.get()) // 100 == 18:
        centuryCode = 2
    elif int(yearBox.get()) // 100 == 19:
        centuryCode = 0
    elif int(yearBox.get()) // 100 == 20:
        centuryCode = 6
    elif int(yearBox.get()) // 100 == 21:
        centuryCode = 4
    elif int(yearBox.get()) // 100 == 22:
        centuryCode = 2
    elif int(yearBox.get()) // 100 == 23:
        centuryCode = 0
    

    if (monthBox.get(monthBox.curselection()) == "January" or monthBox.get(monthBox.curselection()) == "Febuary") and int(yearBox.get()) % 4 == 0: 
        leapYear = 1
    else:
        leapYear = 0

    answer = (yearCode + monthCode + centuryCode + int(dayBox.get()) - leapYear) % 7
    
    if answer == 0:
        day = "Sunday"
    elif answer == 1:
        day = "Monday"
    elif answer == 2:
        day = "Tuesday"    
    elif answer == 3:
        day = "Wednesday"
    elif answer == 4:
        day = "Thursday"
    elif answer == 5:
        day = "Friday"
    elif answer == 6:
        day = "Saturday"

    finalAnswer = str(monthBox.get(monthBox.curselection())) +" "+ str(dayBox.get()) + ", "+ str(yearBox.get()) + " is a "+ day

    answerLabel = Label(root, text=finalAnswer)
    answerLabel.pack()

yearLabel = Label(root, text="Enter a year (1700-2399)")
yearLabel.pack()

yearBox = Entry(root)
yearBox.pack()

monthLabel = Label(root, text="Select a month")
monthLabel.pack()

monthBox = Listbox(root)
monthBox.insert(0, "January")
monthBox.insert(1, "Febuary")
monthBox.insert(2, "March")
monthBox.insert(3, "April")
monthBox.insert(4, "May")
monthBox.insert(5, "June")
monthBox.insert(6, "July")
monthBox.insert(7, "August")
monthBox.insert(8, "September")
monthBox.insert(9, "October")
monthBox.insert(10, "November")
monthBox.insert(11, "December")

monthBox.pack()

dayLabel = Label(root, text="Enter a day")
dayLabel.pack()

dayBox = Entry(root)
dayBox.pack()

answerButton = Button(root, text="Calculate", command=dayOfWeek)
answerButton.pack()






root.mainloop()











