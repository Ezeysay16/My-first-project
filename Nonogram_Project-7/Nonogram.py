from calendar import c
from graphics import Canvas
import time
import random

canvas = Canvas()

CANVAS_SİZE_X=600
CANVAS_SİZE_Y=600
"""
EEE 103 Project

The students who prepared the Nonogram project:

    Name & Surname: Ata GÜNEŞ
    StudentID: 2106102007

    Name & Surname: Esma Zeynep SAYILI
    StudentID: 2006102005

"""


#Playable boxes settings: 
# NUMBER_OF_SET_BOXES=5
NUMBER_OF_BOX_SETES=1
BOX_START_X= CANVAS_SİZE_X/6
BOX_START_Y= CANVAS_SİZE_Y/6
BOX_END_X= 11*CANVAS_SİZE_X/12
BOX_END_Y= 11*CANVAS_SİZE_Y/12

def front_page():
    kapak = canvas.create_image_with_size(0, 0, CANVAS_SİZE_X, CANVAS_SİZE_Y, 'cover.png')
    

 

    beslik = canvas.create_rectangle(95,360,245,470)
    onluk = canvas.create_rectangle(355,360,505,470)
    total_object = int(canvas.find_all()[-1])
    return total_object



def choosing_the_game_option(BOX_SIZE, NUMBER_OF_SET_BOXES, WIN_OR_LOST):
    canvas.set_canvas_size(CANVAS_SİZE_X,CANVAS_SİZE_Y)
    total_object = front_page()
 
    b = 0
    
    while b >= 0:
        
        clicks = canvas.get_new_mouse_clicks()

        for click in clicks:
    
            # a = canvas.find_element_at(click.x,click.y)
            # print(a)
            
            if click.x  > 100 and click.x < 360 and click.y > 250 and click.y < 470:
                
                

                canvas.delete_all()
                NUMBER_OF_SET_BOXES = NUMBER_OF_SET_BOXES
                BOX_SIZE = (BOX_END_X - BOX_START_X) / (NUMBER_OF_BOX_SETES * NUMBER_OF_SET_BOXES)
                i = 0
                i, playable_boxes=player_screen(i,BOX_SIZE, NUMBER_OF_SET_BOXES, total_object)
                
                
                
                WIN_OR_LOST = playing(i, playable_boxes,NUMBER_OF_SET_BOXES,BOX_SIZE, total_object, WIN_OR_LOST )
                b -= 1
                
                
                
            elif click.x  > 310 and click.x < 500 and click.y > 260 and click.y < 350:
                

                
                canvas.delete_all()
                NUMBER_OF_SET_BOXES =  NUMBER_OF_SET_BOXES + 5
                BOX_SIZE= (BOX_END_X - BOX_START_X) / (NUMBER_OF_BOX_SETES * NUMBER_OF_SET_BOXES)
                i = 0
                i, playable_boxes=player_screen(i,BOX_SIZE, NUMBER_OF_SET_BOXES, total_object)
                WIN_OR_LOST = playing(i, playable_boxes,NUMBER_OF_SET_BOXES,BOX_SIZE, total_object, WIN_OR_LOST )
                b -= 1
                
                
        canvas.update()    
    return WIN_OR_LOST
     
def player_screen(i, BOX_SIZE, NUMBER_OF_SET_BOXES, total_object):
    canvas.set_canvas_size(CANVAS_SİZE_X,CANVAS_SİZE_Y)
    playable_boxes = {}
    list_of_boxes = []
    i, playable_boxes = set_of_boxes(playable_boxes, list_of_boxes, i,BOX_SIZE, NUMBER_OF_SET_BOXES,total_object)
    info_box = info_boxes(playable_boxes, BOX_SIZE, NUMBER_OF_SET_BOXES, total_object)
    final_info_y = info_numbers_y(playable_boxes, NUMBER_OF_SET_BOXES, total_object)
    final_info_x = info_numbers_x(playable_boxes, NUMBER_OF_SET_BOXES, total_object)
    add_numbersy(canvas,BOX_SIZE, info_box,final_info_x,NUMBER_OF_SET_BOXES)
    add_numbers_x(canvas,info_box, BOX_SIZE, final_info_y,NUMBER_OF_SET_BOXES)
    return i, playable_boxes

def set_of_boxes(playable_boxes, list_of_boxes, i , BOX_SIZE, NUMBER_OF_SET_BOXES, total_object):
    for a in range(NUMBER_OF_SET_BOXES):
        for b in range(NUMBER_OF_SET_BOXES):
            list_of_boxes.append(canvas.create_rectangle((BOX_START_X+(BOX_SIZE *b)), (BOX_START_Y+(BOX_SIZE *a)), (BOX_START_X+(BOX_SIZE *b)) + BOX_SIZE, (BOX_START_Y+(BOX_SIZE *a)) + BOX_SIZE  ))
            print(list_of_boxes)
            playable_boxes[(a*NUMBER_OF_SET_BOXES)+b+1+total_object] = random.choice(["X", "O"])
            canvas.set_fill_color((a*NUMBER_OF_SET_BOXES)+b+1+total_object, 'ghost white')
            if playable_boxes[(a*NUMBER_OF_SET_BOXES)+b+1+total_object] == "O" :
                i += 1
            #if a == 2: #kod doğru çalışıyor mu diye denediğim kısım. 
            #    print(list_of_boxes[(a*5)+b])
            #    canvas.set_fill_color(list_of_boxes[(a*5)+b], 'black')
            #print(playable_boxes)
    return i, playable_boxes


def info_boxes(playable_boxes, BOX_SIZE, NUMBER_OF_SET_BOXES, total_object):
    info_box = []
    info = []
    for i in range(2):
        if i==0:
            for b in range(NUMBER_OF_SET_BOXES): #Üsttekiler 
                info_box.append(canvas.create_rectangle((BOX_START_X+(BOX_SIZE *b)), (BOX_START_Y - BOX_SIZE ), (BOX_START_X+(BOX_SIZE *b)) + BOX_SIZE, (BOX_START_Y - BOX_SIZE) + BOX_SIZE  ))
                # canvas.set_outline_color(info_box[b], 'red')
                canvas.set_fill_color(info_box[b], 'light steel blue')
                info = info_numbers_y(playable_boxes,NUMBER_OF_SET_BOXES,total_object)
                print(info)
        else:
            for a in range(NUMBER_OF_SET_BOXES): #Alttakiler 
                info_box.append(canvas.create_rectangle((BOX_START_X - BOX_SIZE), (BOX_START_Y+(BOX_SIZE *a)), BOX_START_X, (BOX_START_Y+(BOX_SIZE *a)) + BOX_SIZE  ))
                # canvas.set_outline_color(info_box[b+a+1], 'red')
                canvas.set_fill_color(info_box[b+a+1], 'light steel blue')
                # info = info_numbers_x(playable_boxes)
                # print(info)

    print(playable_boxes, NUMBER_OF_SET_BOXES)
    return info_box

def info_numbers_y(playable_boxes, NUMBER_OF_SET_BOXES, total_object):
    series_info = 0
    prepare_info = []
    final_info_y = []
    y = 0
    for y in range(NUMBER_OF_SET_BOXES):
        if series_info >0:
            prepare_info.append(str(series_info))
            series_info = 0
        if y !=0 :
            final_info_y.append(prepare_info)
            prepare_info = []
        for x in range(NUMBER_OF_SET_BOXES):
            if playable_boxes[(x*NUMBER_OF_SET_BOXES)+y+1+total_object] == "X":
                if series_info > 0:
                    prepare_info.append(str(series_info))
                    series_info = 0
            elif playable_boxes[(x*NUMBER_OF_SET_BOXES)+y+1+total_object] == "O":
                series_info +=1
    if series_info > 0:
        prepare_info.append(str(series_info))
        series_info = 0
    final_info_y.append(prepare_info)
    prepare_info = []


    return final_info_y



def add_numbersy(canvas,BOX_SIZE, info_box,final_info_y,NUMBER_OF_SET_BOXES):
    a = 0
    num = NUMBER_OF_SET_BOXES
    print(info_box)
    # y = (BOX_START_Y / 2) + BOX_SIZE
    for i in range(1,num + 1 ):
        y = canvas.get_top_y(info_box[NUMBER_OF_SET_BOXES -1+ i])  +  (BOX_SIZE / 2) 
        x = canvas.get_left_x(info_box[NUMBER_OF_SET_BOXES ]) +(BOX_SIZE/2)
        
        numbers_in_one_square = canvas.create_text(x,y,final_info_y[i -1])
        canvas.set_font(numbers_in_one_square, 'courier', int(15*(5/NUMBER_OF_SET_BOXES)))
        
        a += 1
    return numbers_in_one_square

def add_numbers_x(canvas,info_box, BOX_SIZE, final_info_x, NUMBER_OF_SET_BOXES):
    for i in range(1,NUMBER_OF_SET_BOXES+1):
        
        x = canvas.get_left_x(info_box[-1 + i]) + (BOX_SIZE / 2) 
        y = canvas.get_top_y(info_box[0]) + (BOX_SIZE/2)
        numbers_in_one_square = canvas.create_text(x,y,final_info_x[i -1])
        canvas.set_font(numbers_in_one_square, 'courier', int(15*(5/NUMBER_OF_SET_BOXES)))
    return numbers_in_one_square   
        
        
        

def info_numbers_x(playable_boxes, NUMBER_OF_SET_BOXES, total_object):
    series_info = 0
    prepare_info = []
    final_info_x = []
    y = 0
    for x in range(NUMBER_OF_SET_BOXES):
        if series_info >0:
            prepare_info.append(str(series_info))
            series_info = 0
        if x !=0 :
            final_info_x.append(prepare_info)
            prepare_info = []
        for y in range(NUMBER_OF_SET_BOXES):
            if playable_boxes[(x*NUMBER_OF_SET_BOXES)+y+1+ total_object] == "X":
                if series_info > 0:
                    prepare_info.append(str(series_info))
                    series_info = 0
            elif playable_boxes[(x*NUMBER_OF_SET_BOXES)+y+1+total_object] == "O":
                series_info +=1
    if series_info > 0:
        prepare_info.append(str(series_info))
        series_info = 0
    final_info_x.append(prepare_info)
    prepare_info = []


    return final_info_x


def sing_create():
    sign_box = canvas.create_rectangle((CANVAS_SİZE_X/2), 560,(CANVAS_SİZE_X/2)+30, 590 )
    canvas.set_fill_color(sign_box, 'goldenrod1')
    sign_text = canvas.create_text((CANVAS_SİZE_X/2)+15, 575, "O" )
    sign = "O"

    return sign, sign_box, sign_text


def playing(i, playable_boxes,NUMBER_OF_SET_BOXES,BOX_SIZE, total_object, WIN_OR_LOST ):
    clicks = []
    sign, sign_box, sign_text = sing_create()
    chance = "3"
    heart = canvas.create_image_with_size(10,10,80,80,"heart.png" )
    heart_number = canvas.create_text(50,50, chance )
    canvas.set_font(heart_number, "courier", 30)
    while i >0:
        if int(chance) >0:
            clicks = canvas.get_new_mouse_clicks() 
            # if clicks!= []: 
            for click in clicks:
                # print(click.y)
                # print(click.x)
                box = canvas.find_element_at(click.x, click.y)
                # print(box)
                if box == (((NUMBER_OF_SET_BOXES**2) + NUMBER_OF_SET_BOXES*4) + 1+total_object  ) or box == (((NUMBER_OF_SET_BOXES**2) + NUMBER_OF_SET_BOXES*4) + 2+total_object  ) :
                    if sign == "X":
                        canvas.set_fill_color(sign_box, 'goldenrod1')
                        canvas.set_text(sign_text, "O" )
                        sign = "O"
                    elif sign == "O":
                        canvas.set_fill_color(sign_box, 'rosy brown')
                        canvas.set_text(sign_text, "X" )
                        sign = "X"
                    
                if box in range(1,(NUMBER_OF_SET_BOXES**2)+1+total_object ):
                    # print(playable_boxes[box])
                    if sign == "O":
                        if playable_boxes[box] == "O" and canvas.get_fill_color(box) != 'goldenrod1' :
                            canvas.set_fill_color(box, 'goldenrod1')
                            i -= 1
                        elif playable_boxes[box] == "X":
                            chance = str(int(chance) - 1)
                            canvas.set_text(heart_number, chance)
                    if sign == "X":
                        if playable_boxes[box] == "O" and canvas.get_fill_color(box) != 'goldenrod1' :
                            chance = str(int(chance) - 1)
                            canvas.set_text(heart_number, chance)
                        elif playable_boxes[box] == "X":
                            canvas.set_fill_color(box, 'rosy brown')
        else:
            break



        canvas.update()
        time.sleep(0.02)
    WIN_OR_LOST = int(chance)
    return WIN_OR_LOST
def finish_screen(WIN_OR_LOST):
    canvas.delete_all()
    if WIN_OR_LOST == 0:
        lost_text = canvas.create_text(300, 180, "You'r such a LOSER!!")
        canvas.set_font(lost_text, 'Times New Roman', 40)

    elif WIN_OR_LOST >= 0:
        win_text = canvas.create_text(300,180, "Congratulations, not a big deal huh...")
        canvas.set_font(win_text, 'Times New Roman', 30)
    
    ###
    finish_box = canvas.create_rectangle(355,360,505,470)
    canvas.set_fill_color(finish_box, 'steel blue')
    finish = canvas.create_text(430,415, "Finish The Game ") 
    keep_going_box = canvas.create_rectangle(95,360,245,470)
    canvas.set_fill_color(keep_going_box, 'steel blue')
    keep_going = canvas.create_text(170,415, "Try Again")
    all_elements = canvas.find_all()
    waiting_count = 0
    ###
    while waiting_count == 0:
        clicks = canvas.get_new_mouse_clicks()
        for click in clicks:
            choice = canvas.find_element_at(click.x, click.y)
            if choice == all_elements[-1] or choice == all_elements[-2]:
                main()
                waiting_count -= 1
            elif choice == all_elements[-3] or choice == all_elements[-4]:
                waiting_count -= 1

        canvas.update()
        time.sleep(0.02)

def main():
    WIN_OR_LOST = 3
    canvas.set_canvas_background_color('ghost white')
    NUMBER_OF_SET_BOXES = 5


    BOX_SIZE= (BOX_END_X - BOX_START_X) / (NUMBER_OF_BOX_SETES * NUMBER_OF_SET_BOXES)

    
    WIN_OR_LOST = choosing_the_game_option(BOX_SIZE, NUMBER_OF_SET_BOXES, WIN_OR_LOST)
    


    finish_screen(WIN_OR_LOST)
    
    
    canvas.update()
    
    
    time.sleep(0.02)
    canvas.update()
   

if __name__ == "__main__":
    main()
    print("Finish")


