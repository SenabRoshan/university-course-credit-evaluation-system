# university-course-credit-evaluation-system
University Course Credit Evaluation System - Console Based

Description: This Python program assists staff and students in assessing their progress and course credits. It gives staff the ability to monitor the credit information of several students and produce a report, and it gives students the ability to check their progress status based on credits. In addition to options for sorting and displaying data in various forms, the program incorporates validation tests.

Features: 
Student Functionality: Pass, defer, and refer credits are entered by the student. The student's progress, deferment, or exclusion is assessed by the system. Before it exits, it verifies the inputs and displays the progress status.

Staff Functionality: Multiple students' credits are entered by the staff and stored in an array. The program repeatedly prompts for input until the staff decides to quit.

A histogram is generated, displaying the number of students who: Progressed, module trailer, module retriever and excluded. The staff can choose how to display the data: either in the order of entry or sorted by progression status.

Data Output:
The data is saved to an array and/or a text file and can be displayed in the console in either sorted or unsorted format.

Example
Student Workflow: Input: Pass Credits: 120 Defer Credits: 20 Refer Credits: 0

Output: Progress

Staff Workflow: Input: Enter Credits (for multiple students) Quit to generate the histogram and view progression data.

Output: Histogram showing the number of students who progressed, had a module trailer, were module retrievers, or were excluded. Data displayed in the desired order: either sorted or in the original order
