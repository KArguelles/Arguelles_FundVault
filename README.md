FundVault System
Project Overview
The FundVault System was created to address common challenges individuals face in managing personal finances effectively. It offers a structured platform to help users organize savings, track expenses, and achieve financial goals. By tackling issues such as the lack of goal-oriented savings, limited financial transparency, and inadequate emergency preparedness, FundVault empowers users with tools to foster financial discipline and independence.

Key Features:
Goal-Based Saving: Create and manage specific financial goals.
Emergency Fund Management: Allocate funds for unforeseen expenses.
Transaction Tracking: Ensure transparency with real-time history.
User Authentication: Secure access to user accounts.
Target Audience:
Students, employees, and freelancers seeking improved financial literacy and effective savings management.

Measurable Goals:
30% user growth in goal-setting within six months of launch.
10% monthly income savings for emergencies by year-end.
40% reduction in time spent managing savings after three months.
95% user satisfaction regarding security and functionality within the first year.
By fostering disciplined saving habits, FundVault aligns with Sustainable Development Goals (SDGs), specifically:

SDG 1: No Poverty
SDG 8: Decent Work and Economic Growth.
Python Concepts and Libraries
The FundVault System leverages various Python concepts and libraries to deliver an interactive, efficient, and user-friendly application.

Tkinter: Builds the graphical user interface (GUI), including buttons, labels, and windows.
Messagebox (Tkinter): Provides pop-up notifications for user interaction.
Pillow (PIL): Handles image processing tasks such as resizing images.
Tkcalendar: Adds a calendar widget for date selection.
Datetime & Timedelta: Tracks and manipulates date and time data.
Random: Generates random values for testing or event simulation.
MySQL: Manages data storage and retrieval for user accounts, transactions, and goals.
These libraries enhance functionality, ensuring a seamless and secure user experience.

Sustainable Development Goals (SDGs)
SDG 1: No Poverty
By encouraging goal-based saving and emergency preparedness, FundVault reduces the financial strain caused by unexpected expenses, supporting users in achieving financial independence and stability.

SDG 8: Decent Work and Economic Growth
FundVault promotes sound financial management practices, enabling users to plan for education, entrepreneurship, and career growth. This fosters sustainable economic progress and broader development.

Instructions for Running the Program
Prerequisites:
Python (version 3.8 or higher)

Required Python libraries:

tkinter
pillow
tkcalendar
mysql-connector-python
Install them using pip:

pip install pillow tkcalendar mysql-connector-python

Database Setup:

Locate the SQL File
The fvault_db.sql file is included in the repository. This file contains the database structure and initial data.

Import the Database

Open phpMyAdmin (usually at http://localhost/phpmyadmin).
Create a new database with the name fvault_db.
Import the fvault_db.sql file into the newly created fvault_db database via the Import tab.
Configure the Database Connection
Ensure the database connection details in the program's configuration file match your MySQL server:

Database name: fvault_db
Username: root (or your MySQL username)
Password: Your MySQL password
Run the Program

Start the program by executing:

python app.py

Usage:
Launch the application to create saving goals and track progress.
Manage transactions and allocate emergency funds.
Review transaction history and goal progress in real time.
