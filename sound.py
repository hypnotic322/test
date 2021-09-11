import pygame
import play
import time



play.set_backdrop('white')

#pic_chidori = play.new_image(image='Chidori.jpg',size=100,x = 0)
#pic_chidori.hide()

pic_jutsu= play.new_image(image='jutsu.jpg',size=100,y=30)
pic_jutsu.hide()

key_jutsu= []

x=-250
a = 0.3
score = False 

chek = False 
check2 = False 

fireball_jutsu = [] 
#def blocks():
for i in range(4):
    key_x = x + i * 165
    key_ju=play.new_box(color= "white",x=key_x,y= 150,width= 100,height= 40, border_color = "black", border_width = 3)
    key_jutsu.append(key_ju)
for i in range(4):
    key_x = x + i * 165
    key_ju=play.new_box(color= "white",x=key_x,y= -20,width= 100,height= 40, border_color = "black", border_width = 3)
    key_jutsu.append(key_ju)
for i in range(4):
    key_x = x + i * 165
    key_ju=play.new_box(color= "white",x=key_x,y= -170,width= 100,height= 40, border_color = "black", border_width = 3)
    key_jutsu.append(key_ju) 

for i in range(4):
    for i in key_jutsu:
        i.hide()




 
gogo3 = [11,10,3,6,7]
gogo2 = [9,7,6,11,1,4]  
gogo1 = [6,5,8,3,0,9,10,4,6]  



            #key_jutsu.remove(i)
     
#fireball = [key_jutsu[9], key_jutsu[7], key_jutsu[6], key_jutsu[11], key_jutsu[1], key_jutsu[4]]









       #Черновик стен
#wall10=play.new_box(color= "green",x= -150,y= -150,width= 110,height= 60, border_color = "black", border_width = 2)
#wall11=play.new_box(color= "blue",x= 150,y= -150,width= 110,height= 60, border_color = "black", border_width = 2)
    #Картинки при нажатии клавиши
pic_Jojo = play.new_image(image='Jojo.pic.png',size=120,x = 10)
pic_Jojo.hide()
pic_Naruto = play.new_image(image='Naruto.pic1.jpg',size=120,x = 0)
pic_Naruto.hide()

jutsu_sound = pygame.mixer.Sound("jutsu_sound.ogg")
start_theme = pygame.mixer.Sound("start.ogg")
end_jutsu = pygame.mixer.Sound("end_jutsu.ogg")
start_jutsu = pygame.mixer.Sound("start_jutsu.ogg")

pic_start = play.new_image(image='pic3.jpg',size=60)

box1 =play.new_box(color= "red",x= -150,y= 0,width= 180,height= 220)
box2 =play.new_box(color= "red",x= 150,y= 0,width= 160,height= 220)

key_Jojo = play.new_image(image='pic1.jpg',size=75, x = -150, y = 0)
key_Naruto  = play.new_image(image='pic2.jpg', x = 150, y = 0, size =50)
key_back = play.new_box(color= "white",x= -310,y= -250,width= 120,height= 60, border_color = "black", border_width = 2)
key_back.hide()
text12 = play.new_text(words = "back to menu", x = -310, y = -250, font= None, font_size =25)
text12.hide()
sounds_naruto = []
sounds_Jojo = []
keys_Jojo = []
keys_Naruto = [] 

melody = []
key_mini_game=play.new_box(color= "white", y = -150, width= 100,height= 40, border_color = "black", border_width = 3)
key_mini_game.hide()
text_mini_game = play.new_text(words = "Мини игра", y = -150, font= None, font_size =25)
text_mini_game.hide()

text0 = play.new_text(words = "Бык", x = -250, y = 150, font= None, font_size =25)
text1 = play.new_text(words = "Лошадь", x = -85, y = 150, font= None, font_size =25)
text2 = play.new_text(words = "Кролик", x = 80, y = 150, font= None, font_size =25)
text3 = play.new_text(words = "Птица", x = 245, y = 150, font= None, font_size =25)

text4 = play.new_text(words = "Тигр", x = -250, y = -20, font= None, font_size =25)
text5 = play.new_text(words = "Дракон", x = -85, y = -20, font= None, font_size =25)
text6 = play.new_text(words = "Обезьяна", x = 80, y = -20, font= None, font_size =25)
text7 = play.new_text(words = "Овца", x = 245, y = -20, font= None, font_size =25)

text8 = play.new_text(words = "Крыса", x = -250, y = -170, font= None, font_size =25)
text9 = play.new_text(words = "Змея", x = -85, y = -170, font= None, font_size =25)
text10 = play.new_text(words = "Собака", x = 80, y = -170, font= None, font_size =25)
text11 = play.new_text(words = "Свинья", x = 245, y = -170, font= None, font_size =25)

text0.hide()
text1.hide()
text2.hide()
text3.hide()
text4.hide()
text5.hide()
text6.hide()
text7.hide()
text9.hide()
text8.hide()
text10.hide()
text11.hide()

key_proceed = play.new_box(color= "white",x=300,y= -250,width= 110,height= 60, border_color = "black", border_width = 3)
key_proceed.hide()
text_op1 =  play.new_text(words = "Введи правельную последовательность печати, ", y = -230, font= None, font_size =25)
text_op2 =  play.new_text(words = "чтобы использовать технику: Чидори", y = -250, font= None, font_size =25)
text_op3 = play.new_text(words = "Провал", y = 280, font= None, font_size =45, color = "red")
text_op1.hide()
text_op2.hide()
text_op3.hide()
text_no = play.new_text(words = "Ты неправильно расставил печати! Какаши не одобряет.", y = -250, font= None, font_size =25)
text_no.hide()
text_yes1 = play.new_text(words = "Вы получили респект от Какаши", y = -250, font= None, font_size =25)

text_yes1.hide()


@key_Jojo.when_clicked
async def Jojo():
    if key_Jojo.is_clicked:
        key_mini_game.hide()
        text_mini_game.hide()
        box1.hide()
        box2.hide()
        key_back.show()
        text12.show()
        Jojo_theme = pygame.mixer.Sound("to be continued.ogg")
        Jojo_theme.play()
        pic_Naruto.hide()
        pic_start.hide()
        pic_Jojo.show()
        key_Jojo.hide()
        key_Naruto.hide()
        x = -180
        for i in range(7):
            key_x = x + i * 60
            key=play.new_box(color= "white",x= key_x,y= 60,width= 50,height= 100, border_color = "black", border_width = 3)
            sound_Jojo = pygame.mixer.Sound("Jojo"+str(i)+".ogg")
            keys_Jojo.append(key)
            sounds_Jojo.append(sound_Jojo)
        for i in range(7):
            key_x = x + i * 60
            key=play.new_box(color= "white",x= key_x,y= -60,width= 50,height= 100, border_color = "black", border_width = 3)
            sound_Jojo = pygame.mixer.Sound("Jojo"+str(i+7)+".ogg")
            keys_Jojo.append(key)
            sounds_Jojo.append(sound_Jojo)
        
         
@key_Naruto.when_clicked
async def Naruto():
    if key_Naruto.is_clicked:
        key_mini_game.show()
        text_mini_game.show()
        box1.hide()
        box2.hide()
        key_back.show()
        text12.show()
        Naruto_theme = pygame.mixer.Sound("Naruto_sound.ogg")
        Naruto_theme.play()
        pic_Jojo.hide()
        pic_start.hide()
        pic_Naruto.show()
        key_Jojo.hide()
        key_Naruto.hide()
        for i in range(11):
            key_x = -300 + i * 60
            key=play.new_box(color= "white",x=key_x,y= 0,width= 50,height= 100, border_color = "black", border_width = 3)
            sound_naruto = pygame.mixer.Sound("Naruto"+str(i)+".ogg")
            keys_Naruto.append(key)
            sounds_naruto.append(sound_naruto)
            

@key_mini_game.when_clicked   
async def mini_game():
    if key_mini_game.is_clicked:
        jutsu_sound.play()
        key_back.show()
        text12.show()
        text_op1.show()
        text_mini_game.hide()
        text_op2.show()
        text_op3.hide()
        pic_jutsu.show()
        pic_start.hide()
        key_mini_game.hide()
        pic_Jojo.hide()
        pic_Naruto.hide()
        key_Naruto.hide()
        key_Jojo.hide()
        box1.hide()
        box2.hide()
        for i in range(4):
            for i in key_jutsu:
                i.show()

        for i in range(4):
            for i in keys_Naruto:
                i.hide()
                keys_Naruto.remove(i)

        text0.show()
        text1.show()
        text2.show()
        text3.show()
        text4.show()
        text5.show()
        text6.show()
        text7.show()
        text8.show()
        text9.show()
        text10.show()
        text11.show()
        

@key_back.when_clicked  
def back():
    text_op1.hide()
    text_op2.hide()
    text_op3.hide()
    text_mini_game.hide()
    key_Jojo.show()
    key_Naruto.show()
    pic_start.show()
    box1.show()
    box2.show()
    text_yes1.hide()
    
    text_no.hide()
    key_back.hide()
    text12.hide()
    key_proceed.hide()
    
    key_mini_game.hide()

    text0.hide()
    text1.hide()
    text2.hide()
    text3.hide()
    text4.hide()
    text5.hide()
    text6.hide()
    text7.hide()
    text8.hide()
    text9.hide()
    text10.hide()
    text11.hide()

    fireball_jutsu.clear()
    for i in range(4):
        for i in keys_Naruto:
            i.hide()
            keys_Naruto.remove(i)

    for i in range(4):
        for i in keys_Jojo:
            i.hide()
            keys_Jojo.remove(i)

    for i in range(4):
        for i in key_jutsu:
            i.hide()

@play.when_program_starts
def start():   
    start_theme.play()
    
@play.repeat_forever
async def do():
    global chek, check2, score
    for i in range(len(keys_Naruto)):
        if keys_Naruto[i].is_clicked:
            keys_Naruto[i].color = "light grey"
            sounds_naruto[i].play()
            await play.timer(seconds=3)
            keys_Naruto[i].color = "white"
    for i in range(len(keys_Jojo)):
        if keys_Jojo[i].is_clicked:
            keys_Jojo[i].color = "light grey"
            sounds_Jojo[i].play()
            await play.timer(seconds=3)
            keys_Jojo[i].color = "white"
    
     
        #Проверка расстановки печатей
    for i in range(len(key_jutsu)):
        if key_jutsu[i].is_clicked:
            start_jutsu.play()
            key_jutsu[i].color = "light grey"
            await play.timer(seconds=a) 
            key_jutsu[i].color = "white"
            fireball_jutsu.append(i)
            #if len(fireball_jutsu) == 9:
            if fireball_jutsu == gogo1: 
                text2.show()
                text_op1.hide()
                text_op2.hide()
                text_yes1.words = "Вы получили респект от Какаши"
                text_yes1.show()
                
                await play.timer(seconds=0.5)
                end_jutsu.play()
                await play.timer(seconds=2)
                fireball_jutsu.clear()
                text_yes1.hide()
                text_op2.words = "чтобы использовать технику: Огненный шар"
                text_op1.show()
                text_op2.show()
                await play.timer(seconds=3)
                chek = True
            
            
            elif fireball_jutsu == gogo2 and chek == True:
                text2.show()
                text_op1.hide()
                text_yes1.words = "Неплохо. Последняя техника будет попроще."
                text_op2.hide()
                text_yes1.show()
                
                await play.timer(seconds=0.5)
                end_jutsu.play()
                await play.timer(seconds=2)
                fireball_jutsu.clear()
                text_yes1.hide()
                text_op2.words = "чтобы использовать технику: Призыв сюрикена"
                text_op1.show()
                text_op2.show()
                text_op3.hide()
                check2 = True
                


            elif fireball_jutsu == gogo3 and check2 == True:
                text2.show()
                text_op1.hide()
                text_op2.hide()
                text_yes1.hide()
                text_op1.words = "Молодец! Ты использовал три сложные техники."
                text_op2.words = "Это твой первый шаг на пути становления Хокаге!"
                text_op1.show()
                text_op2.show()
                await play.timer(seconds=0.5)
                end_jutsu.play()
                fireball_jutsu.clear() 
                score = True 
                
            elif len(fireball_jutsu) == 9 and fireball_jutsu != gogo1 or (len(fireball_jutsu) == 6 and fireball_jutsu != gogo2 and chek == True) or (len(fireball_jutsu) == 5 and fireball_jutsu != gogo3 and check2 == True): 
                if chek != True:
                    text_no.show()
                if chek == True:
                    text_no.words = "Попробуй еще раз! Это довольно сложная техника."

                if check2 == True and chek == True:
                    text_no.words = "Твоя чакра почти на нуле, не удивительно. Давай еще раз!"
                text_op3.color = "red"
                text_op3.words = "Провал!"

                text_op3.show()
                text_no.show()
                text_op1.hide()
                text_op2.hide()
                await play.timer(seconds=0.5)
                end_jutsu.play()
                await play.timer(seconds=3)
                fireball_jutsu.clear()
                text_no.hide()
                text_op1.show()
                text_op2.show()
                text_op3.hide()
        
        elif chek == True and check2 == True and score == True:
            await play.timer(seconds = 4)
            text_op1.words = "Ты уже использовал все три техники."
            text_op2.words = "На этом твоя миссия окончена."
            text_op1.show()
            text_op2.show()                 
play.start_program()
        