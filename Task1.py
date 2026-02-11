#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1.user log in

# defining correct credentials
correct_username = "admin"
correct_password = "1234"

# Taking input from user
username = input("Enter username: ")
password = input("Enter password: ")

# Checking login credentials
if username == correct_username and password == correct_password:
    print("Login Successful")
else:
    print("Invalid Credentials")


# In[2]:


#2.Pass / Fail Analyzer

# marks list provided
marks = [45, 78, 90, 33, 60]

# Initializing counters
pass_students_count = 0
fail_students_count = 0

# comparing marks above 50
for mark in marks:
    if mark >= 50:
        pass_students_count += 1
    else:
       fail_students_count += 1

# Print final result
print("Total Students:", len(marks))
print("Passed Students:", pass_students_count)
print("Failed Students:", fail_students_count)


# In[3]:


#3.Simple Data Cleaner

# Given list of names
names = [" Alice ", "bob", " CHARLIE "]

# declaring an empty list
cleaned_names = []

for name in names:
    cleaned_name = name.strip().lower()  # Remove spaces and convert to lowercase
    cleaned_names.append(cleaned_name)   #adding cleaned name to cleaned_names list

# Print cleaned_nmes list
print("Original Names:", names)
print("Cleaned Names:", cleaned_names)


# In[9]:


#4.Message Length Analyzer

# Given list of messages
messages = ["Hi", "Welcome to the platform", "OK"]


for message in messages:
    length = len(message)
    print("Message:", message)  #printing message
    print("Length:", length)    #printing length of message
    
    if length > 10:
        print("Status: Message longer than 10 characters")
    else:
        print("Status: Message is within limit")
        
    print()  # For spacing
    
    


# In[7]:


#5.Error Message Detector

# Given system logs
logs = ["INFO", "ERROR", "WARNING", "ERROR"]

# Count ERROR entries in given system logs
error_count = 0

for log in logs:
    if log == "ERROR":
        error_count += 1   #if error present,increment in error_count

# Print result
print("Total Logs:", len(logs))
print("Total ERROR Entries:", error_count)


# In[ ]:




