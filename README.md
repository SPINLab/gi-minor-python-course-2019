# GI Minor Python course

Dear GI Minor student, 

welcome to the Vrije Universiteit Python course. In this course we'll take a small dive into the Python programming language. **We'll cover some basics programming concepts and briefly delve into spatial analysis and data mining by way of scraping web pages.**

From previous iterations we've distilled that learning the basics isn't the a challenge (anymore) due to the abundance of MOOCs and interactive online tutorials. **Rather, the question is: how do I craft useful scripts that solve real-world problems?** 

Hence, we'll show you how to apply your knowledge to solve problems you run into in your studies, and give you tips-and-tricks on how to find help and expand Python's capabilities with external modules.
   
This course is extremely hands-on: we don't have slides or lecture notes; we'll only show and execute Python code. We think we can get away with this approach only because you'll have done the bulk of the learning by the time you join us on Monday morning. 

Curious? Read on!

## course overview

- introduction to Python
- introduction to debugging
- getting help: introduction to StackOverflow and online documentation 
- introduction to geospatial analysis with Shapely
- introduction to scraping with BeautifulSoup

## methodology and programme

This course consists of a self-learning part and two hands-on workshops. Each workshop lasts a full day. Interactive lectures are planned for the morning while the afternoons are filled with supervised practical assignments.

The program is as follows: 

 - self-study: [Python course on Codeacademy](https://www.codecademy.com/learn/python)
 - workshop I:
   - morning: interactive recap of Codeacademy material, introduction to spatial analysis
   - afternoon: practical assignment - reading, analysing and writing spatial datasets 
 - workshop II: 
   - morning: recap of workshop I, introduction to scraping
   - afternoon: practical assignment - scraping data from the web



## self-study: codeacademy.com

To maximize the time available for hands-on lectures and exercises we kindly ask you to complete a number of Codeacademy Python lessons in advance.
 
 [codeacademy.com](codeacademy.com) is an online learning platform that offers programming courses in a wide range of languages. You learn to program by typing and executing Python commands directly in your browser.
 
 Registering for Codeacademy is easy:

1. go to [https://www.codecademy.com/](https://www.codeacademy.com) and register
2. log in and navigate to the [Python course](https://www.codecademy.com/learn/python)
3. click `Start`

Please complete the following exercises before coming to class on the 19th of September. 

- Unit 1 - [Lesson: Python Syntax](https://www.codecademy.com/courses/introduction-to-python-6WeG3/0/1)
- Unit 2 - Lesson: Strings & Console Output
- Unit 3 - Lesson: Conditionals & Control Flow
- Unit 4 - Lesson: Functions
- Unit 5 - Lesson: Python Lists and Dictionaries
- Unit 7 - Lesson: List and functions
- Unit 8 - Lesson: Loops
- (optional) Unit 10 - Lesson: Advanced Topics in Python
- Unit 12 - Lesson: File Input and Output

Practice makes perfect: feel free to complete any of the other lessons and or exercises after you've gone through thist list.

## obtaining the lecture materials
The folders in this repository contain the lecture materials, code examples and exercises for the practical sessions. Download them as follows:

1. scroll to the top of this page
2. click on the green button labelled `Clone or download`
3. click on `Download ZIP`
4. Unzip the file you downloaded and load the `.py` scripts in your favourite editor.

## installing Python 

You'll need to install Python and a number of external modules on your machine to run the example scripts and perform. You can do so as follows: 

- download and install `Python 2.7` -> [Download Python 2.7](https://www.python.org/downloads/).

- install the `BeautifulSoup` module: open a command prompt  (Start Menu -> Run cmd...) and execute: `pip install --user BeautifulSoup4`

- install the `pyshp` module: execute `pip install --user pyshp` in the command prompt

- install the `Shapely` module: download ... to ... and execute `pip install --user C:\Users\<username>\Downloads\<downloaded_file>.whl`

- (only in case of trouble) install `pip` -> download and execute [ez_setup.py](https://bootstrap.pypa.io/ez_setup.py ) (execute by double-clicking it) and execute the above steps

## getting help

Pleae use the [issue tracker](https://github.com/ndkv/gi-minor-python-course/issues) to post questions about the lecture notes, examples, exercises and Python in general or in case you're having difficulties installing Python. 

1. scroll to the top of this page and click on `Issues`
2. click on the green button labelled `New issue`
3. enter a descriptive `Title` and a describe your issue/question in the `Comment` textbox.
 
 *Note*: you need a GitHub account to post an issue.
 
 We encourage you to use the issue tracker as it 
 - saves us a lot of time since we don't have to answer each question separately (through mail)
 - saves you a lot of time in case someone else posted your question
 - is a nice collaborative learning mechanism: seeing other people's questions is a sure way to learn something new and unexpected
 
 Not conviced? Feel free to send us an email. 

## the team

- Eduardo Dias
- Simeon Nedkov
- Brian de Vogel
- Mark Opmeer
- Chris Lucas