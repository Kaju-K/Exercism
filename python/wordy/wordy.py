import operator
import re

def answer(question):
    if bool(re.search(r"^[Ww]hat is", question)):   #first we need to check if the question starts with the "What is"
                                                    #here i put the option for the question to start with "w" in lowercase (just in case)
        question = question.strip("?")              #don't need the question mark, this would only make the checking harder after
        question = question.split()                 #break into a list so i can check every element separetly
        question = question[2:]                     #again, don't need the "What is"
        operations = {"plus": operator.add, "minus": operator.sub, "multiplied": operator.mul, "divided": operator.truediv}
                                                    #creating a dictionary so later i can transform the words into the respective operations
        for by in range(question.count("by")):      #same for "by" - we don't need it
            question.remove("by")
        if len(question) == 0:                      #for the "What is?" case
            raise ValueError("syntax error")
        if bool(re.search(r"[a-zA-Z!@#$%&*~^]", question[0])) == False:     #here I'm making sure that the "what is ..." is for a number specifically
                                                            #although there is no test for this, in case it's not a number, just raise an exception below
            calculation = int(question[0])                  #store this for later and since it's a number, use "int()"
            if len(question) == 1:                          #for the specific case of just asking for one number
                return calculation
            for index, element in enumerate(question[1:]):  #now we can check the elements one by one
                                                            #we want it to be: operation -> number -> operation -> number...
                                                            #necessarly ending with a number and starting with "operation" because i'm taking b[1:]
                                                            #cause we know that question[0] is number from the "if"
                if index % 2 == 0:                          #the even indexes should give us the operations while the odd should give us the numbers
                    if bool(re.search(r"[0-9]", element)):  #in case the operation is in fact a number
                        raise ValueError("syntax error")
                    if element not in operations:           #in case the name of the operation is not listed in our dictionary or it's a random word
                        raise ValueError("unknown operation")
                    if element == question[-1]:             #in case the question finishes with the operation
                        raise ValueError("syntax error")
                    if element in operations:               #Phew! We survived the exceptions (so far...)
                        continue
                if index % 2 == 1:                          #don't know if it's necessary since we have the previous "if"
                                                            #but it helps me understand that this part is for the odd indexes
                    if bool(re.search(r"[a-zA-Z!@#$%&^~]", element)):                           #in case it's not a number
                        raise ValueError("syntax error")
                    calculation = operations.get(question[index])(calculation, int(element))    #making the so desired operation using "int()"
                                                            #because we know that element is a number from the previous if and remember
                                                            #that index in question show the previous element since we used question[1:] in the for
            return calculation              #WE MADE IT!!
        raise ValueError("syntax error")    #in case the first number it's not a number :P
    raise ValueError("unknown operation")   #in case the question does not start with "What is..."

