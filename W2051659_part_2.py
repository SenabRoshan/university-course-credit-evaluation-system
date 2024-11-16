#I declare that my contains no examples of misconducts ,such as plagiarism, or collusion
#Any code taken from other sources is referrenced within my code solution

#Student ID = W2051659 / 20230406
#Date : 11/12/2023

from W2051659_part_1 import *            # importing the whole part 1  inorder to use on part 2
path = "Course Work.txt"
file = open(path,"a")        
progression_data.sort(reverse = True)     # got idea  for this part from https://www.w3schools.com/python/ref_list_sort.asp
if user_type == "STAFF":
      for nested_credits in progression_data:
                if nested_credits[0] == 120:
                     progress_text = f"Progess: {str(nested_credits)[1:-1]}" # got idea for this part from https://www.decalage.info/en/python/print_list   #converting the content of nested_credits into string before including it to the formatted string.
                     file.write(progress_text + '\n')
                     print(progress_text)
                elif nested_credits[0] == 100:
                     module_trailer_text = f"Progess (module trailer): {str(nested_credits)[1:-1]}"
                     file.write(module_trailer_text + '\n')
                     print(module_trailer_text)
                elif nested_credits[2] >= 80:
                     exclude_text = f"Exclude: {str(nested_credits)[1:-1]}"
                     file.write(exclude_text + '\n')
                     print(exclude_text) 
                else:
                     module_retreiver_text = f"Module retreiver: {str(nested_credits)[1:-1]}"
                     file.write(module_retreiver_text + '\n')
                     print(module_retreiver_text)
file.close
