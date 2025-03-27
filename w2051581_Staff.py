# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code soluƟon.
# Student ID: w2051581 / 20230196
# Date: 2023/12/13

from graphics import GraphWin, Point, Rectangle, Text, Line, GraphicsError

List1 = []
def Progression_Outcomes():
    Progress = 0
    Trailer = 0
    Retriever = 0
    Exclude = 0
    List2 = []

    while True:
        try:
            Pass_Credits = int(input("Enter your pass credits :"))
            Defer_Credits = int(input("Enter your defer credits :"))
            Fail_Credits = int(input("Enter your fail credits :"))

            if Pass_Credits not in [0, 20, 40, 60, 80, 100, 120] or \
               Defer_Credits not in [0, 20, 40, 60, 80, 100, 120] or \
               Fail_Credits not in [0, 20, 40, 60, 80, 100, 120] :
                print( " out of range " )
                continue

        except ValueError:
            print(" Integer required ")
            continue

        total_credits = Pass_Credits + Defer_Credits + Fail_Credits
        if total_credits != 120:
            print("Total incorrect")
        else:
            if Pass_Credits == 120 and Defer_Credits == 0 and Fail_Credits == 0:
                print("Progress")
                List2 = [" Progress " ,Pass_Credits, Defer_Credits,  Fail_Credits]
                Progress += 1
            elif Pass_Credits == 100 and 20 in [ Defer_Credits, Fail_Credits ]:
                print("Progress (module trailer)")
                List2 = [" Progress (module trailer)" ,Pass_Credits, Defer_Credits,  Fail_Credits]
                Trailer += 1
            elif 0 <= Pass_Credits <= 80 and 0 <= Defer_Credits <= 120 and 0 <= Fail_Credits <= 60 :
                print("Do not Progress - module retriever")
                List2 = ["Do not Progress - module retriever " ,Pass_Credits, Defer_Credits,  Fail_Credits]
                Retriever += 1
            elif 0 <= Pass_Credits <= 40 and 0 <= Defer_Credits <= 40 and 80 <= Fail_Credits <= 120:
                print("Exclude")
                List2 = ["Exclude" ,Pass_Credits, Defer_Credits,  Fail_Credits]
                Exclude += 1

        List1.append(List2)
        
        print("Would you like to enter another set of data ?")
        cont = input('Enter "y" to continue or "q" to quit and view result :')
        print()
        if cont == "y":
            continue
        elif cont == "q" :
            #call the main function with counts
            main(Retriever, Exclude, Trailer, Progress)
            break
        else:
            print("Integer required")

    print(" Part 2 ")
    for i in List1:
        print(i[0],"-", end =' ')
        print(i[1],",", end =' ')
        print(i[2],",", end =' ')
        print(i[3])

        # write the data to a text file
        with open ("Progression_Data (staff).txt", "w")as f:
            f.write("Part 3:\n")
            f.writelines([f" {data[0]} ={data[1]} , {data[2]} , {data[3]}\n "  for data in List1])


def create_rectangle(win, x, y, label, count, color = "maroon"):
    #Create the bottom text
    rec_down = Text (Point(x,520), f" {label} " )
    rec_down.setSize(15)
    rec_down.setFill(color)
    rec_down.setStyle("bold")
    rec_down.draw(win)

    #Create the upper text with count
    rec_up = Text(Point(x + 3, (490 - count *20)), str(count))
    rec_up.setSize(18)
    rec_up.setStyle("bold")
    rec_up.draw(win)

def main (retriever_count, exclude_count, trailer_count, progress_count):
    #calculate total using sum function
    total =  sum([retriever_count, exclude_count, trailer_count, progress_count])

    win = GraphWin("Histogram",700,700)
    win.setBackground("floralwhite")

    Topic_1 = Text(Point(230, 60), "Histogram Result")
    Topic_1.setTextColor("red4")
    Topic_1.setSize(25)
    Topic_1.setStyle("bold")
    Topic_1.draw(win)

    Topic_2 = Text(Point(240, 550),str (total) +  " Outcomes in total ")
    Topic_2.setTextColor("darkorchid4")
    Topic_2.setSize(18)
    Topic_2.setStyle("bold")
    Topic_2.draw(win)

    Rec_1 = Rectangle(Point(100 , 500), Point(210, (500 - progress_count *20)))
    Rec_1.setFill("darkseagreen4")
    Rec_1.draw(win)

    Rec_2 = Rectangle(Point(232 , 500), Point(342, (500 - trailer_count *20)))
    Rec_2.setFill("palevioletred")
    Rec_2.draw(win)

    Rec_3 = Rectangle(Point(364 , 500), Point(474, (500 - retriever_count *20)))
    Rec_3.setFill("orange")
    Rec_3.draw(win)

    Rec_4 = Rectangle(Point(496 , 500), Point(606, (500 - exclude_count *20)))
    Rec_4.setFill("steelblue4") 
    Rec_4.draw(win)

    create_rectangle(win, 155, 1, "Progress", progress_count)
    create_rectangle(win, 290, 2, "Trailer", trailer_count)
    create_rectangle(win, 420, 3, "Retriever", retriever_count)
    create_rectangle(win, 550, 4, "Excluded", exclude_count)

    Line_1 = Line(Point(60,500) , Point(646,500)).draw(win)
    Line_2 = Line(Point(95,72) , Point(370,72)).draw(win)

    
    try:
        win.getMouse()
        win.close()
    except GraphicsError:
        pass

#call the function
Progression_Outcomes()

