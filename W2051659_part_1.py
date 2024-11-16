#I declare that my contains no examples of misconducts ,such as plagiarism, or collusion
#Any code taken from other sources is referrenced within my code solution

#Student ID = W2051659 / 20230406
#Date : 11/12/2023

total_progress_count = 0      # global variables to keep count each outcome 
total_module_trailer_count = 0
total_module_retriever_count = 0
total_exclude_count = 0
def validate_credit(value):      # checking credit values using seperate function
    credit_value = list(range(0,121,20))
    if value not in credit_value:
        print("Out of range") 
        return True
    else:
       return False       
          
progression_data = []          # empty list to append outcomes
   
def progress_outcome_of_students():
    global total_progress_count            # got this idea from https://realpython.com/python-scope-legb-rule/#the-global-statement    
    global total_module_trailer_count
    global total_module_retriever_count
    global total_exclude_count

    expected_credits = 120
    while True:
      try:   
        # Get input for each category and checks it's validity
          pass_credits = int(input("Please enter your credits at pass: "))
          if validate_credit(pass_credits):
           pass_credits = int(input("Please enter your credits at pass: "))
            
          defer_credits = int(input("Please enter your credits at defer : "))
          if validate_credit(defer_credits):
            defer_credits = int(input("Please enter your credits at defer : "))
            
          fail_credits = int(input("Please enter your credits at fail: "))
          if validate_credit(fail_credits):
             fail_credits = int(input("Please enter yout credits at fail: "))
          
          #check whether the total is correct
          total_credits = pass_credits + defer_credits + fail_credits
          if total_credits != expected_credits:
             print("Total incorrect")
             print("Please Enter from the Beginning......\n")
             continue
               
          #appending the input datas to a nested list
          progression_data.append([pass_credits, defer_credits, fail_credits])

          # Store all students' results
          if pass_credits == expected_credits:
            print("Progress")
            total_progress_count += 1
          elif pass_credits == 100:
            print("Progress(module trailer)")
            total_module_trailer_count += 1
          elif pass_credits <= 80 and fail_credits<=60:
            print("Do not progress - module retriever")
            total_module_retriever_count += 1
          elif fail_credits >= 80:
            print("Exclude")
            total_exclude_count += 1
          break

      except ValueError:
        print("Integer required.")
       
# Program starts to run from here....
while True:
   user_type = input("Please Enter Staff/Student:").upper()

   if user_type == "STUDENT":
    progress_outcome_of_students()
    break
   elif user_type == "STAFF":
    option = ''
    while option != 'q':
        progress_outcome_of_students()
        option = input("Please enter 'q' to QUIT or 'y / any other characters' to CONTINUE: ").lower()

    #getting the total to use on histogram
    total = total_exclude_count + total_module_retriever_count + total_module_trailer_count + total_progress_count
   
    # call the graphics.py
    from graphics import *
    def main():
     
     win = GraphWin("My Rectangle", 1000, 800)
     win.setBackground("light pink")
     y_axis = Line(Point(100,100), Point(100,700))  
     x_axis = Line(Point(100,700), Point(900,700))   
     y_axis.draw(win)
     x_axis.draw(win)
     
     #draw rectange for each progression outcome.
     progress_bar = Rectangle(Point(300,(700-50* total_progress_count)) , Point(200,700))  #rectangles from up second corner to down 1 st corner
     module_trailer_bar =  Rectangle(Point(450,(700-50* total_module_trailer_count)) , Point(350,700))  # 700 is constant as y axis starts from 0 means 700 (point 700 is on bottom)
     module_retriever_bar = Rectangle(Point(600,(700-50* total_module_retriever_count)) , Point(500,700)) 
     exclude_bar = Rectangle(Point(750,(700-50* total_exclude_count)) , Point(650,700))
     
     progress_bar.setFill("grey")
     module_trailer_bar.setFill("purple")
     module_retriever_bar.setFill("yellow")
     exclude_bar.setFill("brown")
  
     progress_bar.draw(win)
     module_trailer_bar.draw(win)
     module_retriever_bar.draw(win)
     exclude_bar.draw(win)

    # defining relevent names for each areas.
     title = Text(Point(200,70), "Histogram Results.")
     title.setSize(18)
     title.setStyle("bold")
     title.draw(win)

     progress_bar_messege = Text(Point(240,720), "Progress")
     progress_bar_messege.setStyle("bold")
     progress_bar_messege.draw(win)

     trailer_bar_messege = Text(Point(390,720), "Trailer")
     trailer_bar_messege.setStyle("bold")
     trailer_bar_messege.draw(win)

     retriever_bar_messege = Text(Point(540,720), "Retriever")
     retriever_bar_messege.setStyle("bold")
     retriever_bar_messege.draw(win)

     exclude_bar_messege = Text(Point(690,720), "Excluded")
     exclude_bar_messege.setStyle("bold")
     exclude_bar_messege.draw(win)

     show_outcome = Text(Point(240,750), f'{total} outcomes in total')
     show_outcome.setStyle("bold")
     show_outcome.draw(win)

     win.getMouse() # pause for click in window
     win.close()

    main()
    break

   else:
      print("Invalid input.")
   
   

