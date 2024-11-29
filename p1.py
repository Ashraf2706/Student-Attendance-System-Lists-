"""
File: p1.py
Author: Ashraf Kawooya
Date: 11/3/2022
Lab Section: 11
Email:  ashrafk1@umbc.edu
Description:  This program shows the layout of code in a Python file, and greets
the user with the name of the programmer
"""

''' ***** LEAVE THE LINES BELOW ALONE ***************
********* LEAVE THE LINES BELOW ALONE ***************
********* LEAVE THE LINES BELOW ALONE *************** '''
debug = False

from dataEntry import fill_roster
from dataEntry import fill_attendance_data

''' ***** LEAVE THE LINES ABOVE ALONE ***************
********* LEAVE THE LINES ABOVE ALONE ***************
********* LEAVE THE LINES ABOVE ALONE *************** '''

def list_students_not_in_class(classRoster, attendData):
    """
    Compare the swipe log with the given course roster. Place those students that
    did not show up for class into a list.
    :param classRoster: the list of all students that go to the school
    :param attendData: the list of all students that showed up to school that day
    :return: names of students that did not attend
    """
    not_in_class = []
    name_list = []
    for i in range(len(attendData)):
        name = attendData[i].split(",")[0] + "," + attendData[i].split(",")[1]
        name_list.append(name)
        
    for word in classRoster:
        if word not in name_list:
            not_in_class.append(word)
        
    return not_in_class

        
def list_all_times_checking_in_and_out(string, attendData):
    """
    Looking at the swiping log, this function will list all in and outs for a
    particular Student. Please note, as coded in the p1.py file given, this
    function was called three times with different student values.
    :param string: the name string in the attendance that has the names of the students
    :param attendData: contains the information of the students that attended that day
    :return: times in and out for particular students
    """
    in_and_out = []
    for name in attendData:
        if string in name:
            in_and_out.append(name)
    return in_and_out
            
            
def list_all_times_checked_in(attendData):
    """
    This function returns a list of when all student(s) FIRST swipe in.
    :param attendData: contains that the name and timestamp of the students
    :param :
    :return: the names and times of the students when they first swiped in regardless of being late.
    """
    name_list = []
    time_list = []
    date_list = []
    final_names = []
    first_check_in = []
    first_swipe = []
    
    for i in range(len(attendData)):
        name = attendData[i].split(",")[0] + "," + attendData[i].split(",")[1]
        name_list.append(name)
        
    for i in range(len(attendData)):
        time = attendData[i].split(",")[2]
        time_list.append(time)
        
    for i in range(len(attendData)):
        date = attendData[i].split(",")[3]
        date_list.append(date)

    for name in name_list:
        if name not in final_names:
            final_names.append(name)
    
    for item in final_names:
        for value in attendData:
            if item in value:
                if item not in first_swipe:
                    first_swipe.append(item)
                    first_check_in.append(value)
    return first_check_in


def list_students_late_to_class(attendData):
    """
    When given a timestamp string and the swipe log, a list of those records
    of students who swiped in late into the class is produced. This function
    returns a list of when all student(s) FIRST swipe in.
    :param attendData: contains the timestamp string
    :param time_list: contatins the times of the students that is split to find the late and early attendees
    :return: names of students that attended late to class
    """

    name_list = []
    time_list = []
    date_list = []
    before_9 = []
    after_9 = []
    early_list = []
    late_list = []
    final_late_names = []
    this_final_names = []
    this_final_value = []
    
    for i in range(len(attendData)):
        name = attendData[i].split(",")[0] + "," + attendData[i].split(",")[1]
        name_list.append(name)
    
    for i in range(len(attendData)):
        time = attendData[i].split(",")[2]
        time_list.append(time)

    for i in range(len(attendData)):
        date = attendData[i].split(",")[3]
        date_list.append(date)
    
    for i in range(len(time_list)):
        split_time = time_list[i].split(":")
        if int(split_time[0]) >= 9:
            after_9.append(name_list[i])
        else:
            before_9.append(name_list[i])

    for name in after_9:
        if name in before_9:
            early_list.append(name)
        else:
            late_list.append(name)

    for name in late_list:
        if name not in final_late_names:
            final_late_names.append(name)

    for item in final_late_names:
        for value in attendData:
            if item in value:
                if item not in this_final_names:
                    this_final_names.append(item)
                    this_final_value.append(value)
    return this_final_value
                    
            
        
def get_first_student_to_enter(attendData):
    """
    Simply, this function returns the student that swiped in first. Note,
    the order of the data entered into the swipe log as not the earliest
    student to enter.
    :param attendData: contains the names and timestamps of the students in the attendance
    :param time_list: contains the times that is later broken down to find the earliest timestamp
    :return: the student that attended earliest to school
    """
    name_list = []
    time_list = []
    date_list = []
    early_list = []
    late_list = []
    first_to_enter = []
    
    for i in range(len(attendData)):
        name = attendData[i].split(",")[0] + "," + attendData[i].split(",")[1]
        name_list.append(name)

    for i in range(len(attendData)):
        time = attendData[i].split(",")[2]
        time_list.append(time)
        
    for i in range(len(attendData)):
        date = attendData[i].split(",")[3]
        date_list.append(date)
        
    for i in range(len(time_list)):
        split_time = time_list[i].split(":")
        if int(split_time[0]) >= 9:
            late_list.append(time_list[i])
        else:
            early_list.append(time_list[i])

    min_early_time = '08:59:59'
    for time in early_list:
        if int(time.split(':')[1]) < int(min_early_time.split(':')[1]):
            min_early_time = time
            
    for time in attendData:
        if min_early_time in time:
            first_to_enter.append(time)

    return first_to_enter

            
def printList(list):
    
    """
    Simply prints the list. The function should not be able to change any
    values of that list passed in.
    :param ????:
    :param ????:
    :return: ????
    """
    for value in list:
        print(value)

    
    ''' ***** LEAVE THE LINES BELOW ALONE ***************
    ********* LEAVE THE LINES BELOW ALONE ***************
    ********* LEAVE THE LINES BELOW ALONE *************** '''
if __name__ == '__main__':
    # Example, Dr. Nicholas, 9am class
    
    # load class roster here into a list
    classRoster = fill_roster()

    # figure out which attendance data file to load here
    
    # load data
    attendData = fill_attendance_data()

    # use different tests
    # make sure roster was filled
    # printList(classRoster)
    # make sure attendance data was loaded
    # printList(attendData)
        
    # list all those missing
    print("****** Students missing in class *************")
    printList(list_students_not_in_class(classRoster, attendData))
    # list signin/out times for a student
    print("****** List all swipe in and out for a student *******")
    printList(list_all_times_checking_in_and_out("Lupoli, Shawn", attendData))
    print("****** List all swipe in and out for a student *******")
    printList(list_all_times_checking_in_and_out("Allgood, Nick", attendData))
    print("****** List all swipe in and out for a student *******")
    printList(list_all_times_checking_in_and_out("Arsenault, Al", attendData))
    # display when students first signed in (and in attendance)
    print("****** Check in times for all students who attended***")
    printList(list_all_times_checked_in(attendData))
    # display all of those students late to class
    print("****** Students that arrived late ********************")
    printList(list_students_late_to_class(attendData))
    # display first student to enter class
    print("******* Get 1st student to enter class ****************")
    print(get_first_student_to_enter(attendData))
    
    ''' ***** LEAVE THE LINES ABOVE ALONE ***************
    ********* LEAVE THE LINES ABOVE ALONE ***************
    ********* LEAVE THE LINES ABOVE ALONE *************** '''
    
    
