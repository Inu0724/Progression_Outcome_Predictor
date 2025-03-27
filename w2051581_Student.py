# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code soluƟon.
# Student ID: w2051581 / 20230196
# Date: 2023/12/13

def Progression_Outcomes():
    try:
        Pass_Credits = int(input(" Enter your pass credits : "))
        Defer_Credits = int(input(" Enter your defer credits :" ))
        Fail_Credits = int(input(" Enter your fail credits :" ))

        if Pass_Credits not in [0,20,40,60,80,100,120] or \
        Defer_Credits not in [0,20,40,60,80,100,120] or \
        Fail_Credits not in [0,20,40,60,80,100,120]:
            print(" Out of range ")
                

    except ValueError:
        print(" Integer required ")
            

    total_credits = Pass_Credits + Defer_Credits + Fail_Credits
    if total_credits != 120:
        print(" Total incorrect ")
    else:
        if Pass_Credits == 120 and Defer_Credits == 0 and Fail_Credits == 0 :
            print(" Progress ")
        elif Pass_Credits == 100 and 20 in [Defer_Credits , Fail_Credits]:
            print(" Progress ( module trailer )")
        elif 0 <= Pass_Credits <= 80 and 0 <= Defer_Credits <=120 and 0 <= Fail_Credits <= 60:
            print(" Module retriever ")
        elif 0 <= Pass_Credits <= 40 and 0 <= Defer_Credits <= 40 and 80 <= Fail_Credits <= 120:
            print(" Exclude ")

#Call the function
Progression_Outcomes()

        



        
            
