# Simple Python To-Do list Application

### Paul Jaghab
### Coding Temple, January 2025 Cohort


## List Project 1 
================

The project, although fairly simple in concept, was completed within the first two weeks of the program. It's a simple program that challenged me quite a bit at the onset of the course. Even part I of the readme shows how inexperienced I was at the start, but list project 2 is a little more advanced, has more modularity and shows a better understanding of the foundations of Python.

### To Run The Program
Download the .py file from this GitHub repository to your local machine, and run in your existing Python terminal using VScode or a similar IDE. Once the program runs, it's pretty simple and intuitive. Just follow the prompts to build your list. You'll find more details below:

### Adding a Task
1. The program is designed to take a single input each time you select add a task.
2. You are able to add any combinations of letters and numbers that you wish as the task name. The input will return a string of the characters entered.
3. Once you add a task, you'll get a confirmation message, the new item will be added to the end of the list, and a traditional ordered list will display above the program menu. 

### Deleting a Task
The functionality to delete tasks was the most challenging part of the assignment to develop. The most challenging part was identifying the task that the user needs to delete and properly handling the deletion of the task. I used the pop function to delete the tasks rather than using remove or the del keyword. The choice was made so that the removed value was returned in the deleted_task variable. 

### Error Handling
The only error handling in the assignment that used try, except, else, and finally was in the delete selection in the program. The remaining attempts at error handling were through conditional statements that caught the possible exceptions under the else statement and print error statements. The while loop ensures the program keeps running until the user desires to quit. 

### Why My Project Stands Out
This project is extremely simple and intuitive. The menu is kept short, the user can exit at any time, and functionality is smooth, offering a clean terminal output. 



## List Project 2
================

A simple program for managing lists that has the added function of file handling, allowing for tasks to stay in memory between executions of the program

### Description
This program provides a basic framework for creating, editing, and deleting lists. Error handling has been improved and the file handling makes the program much more robust, functioning as a to-do list should. 

### Usage
To use the program, simply run the listproject2.py script and follow the prompts. In the program I've imported the time module to place some delays after the actions to provide for a better user experience. I think the times could be cut in half but you can change it to your liking. 

