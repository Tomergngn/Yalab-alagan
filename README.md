# Yalab-alagan
Yalab-alagan is a Python-based tool with a user-friendly interface that helps automate communication with students via WhatsApp and manage course enrollment data. It scrapes HTML content from a website to keep course and student records up-to-date and provides an intuitive interface to plan and initiate student outreach.

## Schedule WhatsApp Messages
1. Select a course.
2. Choose a time slot (e.g., 15:00).
3. Send.

The app will automatically send WhatsApp messages to students in the selected course, asking if they'll attend at the specified date and time.

## Update Courses and Student Information
Pulls real-time data from a website. Retrieves:
* Student names
* Gender
* Enrolled courses
* Phone numbers

Ensures your contact list is always current and accurate.

## How It Works
### Web Scraping:
The app fetches student and course data from an external HTML-based site.

### WhatsApp Messaging:
Uses the scraped phone numbers to contact students directly with a confirmation message.

## Technologies Used
* Python 3
* User manipulation - pyautogui, clipboard, pyperclip
* Screen reading - PIL
* GUI toolkit - customtkinter
* Data Management - os, pickle, ctypes
* Web Integration - webbrowser, urllib, pywhatkit

## Setup - NEED A LOGGED IN YALAB ACCOUNT IN ORDER TO UPDATE ACCOUNTS
1. Clone this repository:
```
git clone https://github.com/Tomergngn/Yalab-alagan.git
cd Yalab-alagan
```
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Run the program:
```
python main.py
```


This project respects privacy and is intended for internal organizational use.
