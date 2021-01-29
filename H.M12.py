prompt = """
(L)ogin
(N)ew user
(Q)uit
"""

user_data ={}
fhand = open("users.txt")
for line in fhand:
    data = line.strip().split(",")
    user_data[data[0]] = data[1]

def create_user(name,password):
    if name not in user_data:
        user_data[name] = password
        fhand = open("users.txt",'a')
        fhand.write("{0},{1}\n".format(name,password))
        fhand.close()
        print("-------User Created for:",name)
    else:
        print("User already exist,try other names!")

def login(name,password):
    if name in user_data and password == user_data[name]:
        print("Login  Successful!")
        print("Welcome to the game")
        return True
    else:
        print("Incorrect Username or Password")
        return False
    
while True:
    print("-"*29,"Welcome to my system","-"*29)
    print(prompt)
    a = input("Please input your choice:")
    a = a.lower()
    if a == "n":
        n = input("User Name:")
        while True:
            p = input("Password:")
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            numbers = "0123456789"
            have_a = False
            have_n = True
            if len(p) < 6:
                print("The length of the password should be greater than 6!")
                continue
            for c in p:
                if c in alphabet:
                    have_a = True
                if c in numbers:
                    have_n = True
            if have_a and have_n:
                break
            else:
                print("The password must have characters and numbers!")
        create_user(n,p)
    elif a == "l":
        n = input("User Name:")
        p = input("Password:")
        login(n,p)
        if login(n,p) == True:
            class Hero():
                def __init__(self,n,hp,atk,skills,dfs):
                    self.name = n
                    self.health = hp
                    self.attack = atk
                    self.skills = skills
                    self.defense = dfs
                def show_me(self):
                    print("Name:",self.name)
                    print("HP:",self.health)
                    print("Attack:",self.attack)
                    print("Defense:",self.defense)
                    for i in self.skills:
                        print("Skill:",i["name"],"---Damage:",i["damage"])
                def get_name(self):
                    return self.name
                def normal_attack(self,target):
                    if self.is_dead() or target.is_dead():
                        print("Stupid")
                        print("Someone_is_dead_error")
                    else:
                        dmg = self.attack
                        print(self.name," attacks ",target.get_name())
                        target.hurt(dmg,target)
                        target.show_me()
                        print("")
                def skill_attack(self,n,target):
                    if self.is_dead() or target.is_dead():
                        print("Stupid")
                        print("Someone_is_dead_error")
                    else:
                        skill = self.skills[n]
                        print(self.name," uses ",skill["name"]," on ",target.get_name())
                        target.hurt(skill["damage"],target)
                        print("")
                        target.show_me()
                        print("")
                def hurt(self,damage,target):
                    self.health -= damage - target.defense
                    print(self.name," suffers ",damage - target.defense," damage")
                    if self.health <= 0:
                        self.health = 0
                    if self.is_dead():
                        print(self.name," is killed!")
                def is_dead(self):
                    if self.health > 0:
                        return False
                    else:
                        return True

            iron_skills = [{"name":"Iron Punch","damage":150},{"name":"Laser Beam","damage":490}]
            a = Hero("Ironman",900,120,iron_skills,50)

            hulk_skills = [{"name":"Hulk Smash","damage":200},{"name":"Anger","damage":450}]
            b = Hero("Hulk",1000,110,hulk_skills,5)

            thor_skill = [{"name":"thunder","damage":300},{"name":"Thor's Hammer","damage":500}]
            c = Hero("Thor",1050,130,thor_skill,40)

            
            a.show_me()
            b.show_me()
            c.show_me()
            print("---------Battle Begins---------")
            import random
            import time
            while True:
                time.sleep(1)
                turn = random.randrange(1,19)
                if turn == 1:
                    a.normal_attack(b)
                elif turn == 2:
                    a.normal_attack(c)
                elif turn == 3:
                    b.normal_attack(a)        
                elif turn == 4:
                    b.normal_attack(c)
                elif turn == 5:
                    c.normal_attack(a)
                elif turn == 6:
                    c.normal_attack(b)
                elif turn == 7:
                    a.skill_attack(0,b)
                elif turn == 8:
                    a.skill_attack(0,c)        
                elif turn == 9:
                    a.skill_attack(1,b)
                elif turn == 10:
                    a.skill_attack(1,c)
                elif turn == 11:
                    b.skill_attack(0,a)
                elif turn == 12:
                    b.skill_attack(0,c)        
                elif turn == 13:
                    b.skill_attack(1,a)
                elif turn == 14:
                    b.skill_attack(1,c)
                elif turn == 15:
                    c.skill_attack(0,b)
                elif turn == 16:
                    c.skill_attack(0,a)        
                elif turn == 17:
                    c.skill_attack(1,b)
                elif turn == 18:
                    c.skill_attack(1,a)
                if (a.is_dead() and b.is_dead()) or (a.is_dead() and c.is_dead()) or (b.is_dead() and c.is_dead()):
                    a.show_me()
                    print("")
                    b.show_me()
                    print("")
                    c.show_me()
                    print("Game over")
                    break
    elif a == "q":
        print("Bye...")
        break
    else:
        print("Wrong choice, try again")




            




            
