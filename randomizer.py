print("\nVälkommen till Star Wars Duel.\nDu ska slåss i en turnering.")

import random,time

force = random.randint(1,1)

time.sleep(2)
print("\n-\n")
time.sleep(0.3)
print("-\n")
time.sleep(0.3)
print("-\n")

if(force == 1): # force sensitive
    print("Du är force sensitive.")
    
    time.sleep(1)
    print("\n-\n")
    
    force_ability = random.randint(2000,20000)

    
    if(force_ability > 15000 and force_ability <= 20000): # hög midichlorian
        print("Du är väldigt force sensitive.")
        
        alliance = random.randint(1,3)
        
        time.sleep(1)
        print("\n-\n")
    
        if(alliance == 1): # jedi
            print("Du är en Jedi.")
        
            experience = random.randint(1,3)
    
            time.sleep(1)
            print("\n-\n")
    
            if(experience == 1): # mycket erfarenhet
                print("Du har mycket erfarenhet i strid.") 
        
                master = random.randint(1,2)
        
                time.sleep(1)
                print("\n-\n")
        
                if(master == 1): # jedi knight
                    print("Du är en Jedi Master.")
                    
                    weapon = random.randint(1,4)
    
                    time.sleep(1)
                    print("\n-\n")
    
                    if(weapon == 1):
                        print("Ditt vapen är en vanlig Lightsaber.")
    
                    elif(weapon == 2):
                        print("Du har en modifierad Lightsaber med inbyggd Blaster.")
    
                    elif(weapon == 3):
                        print("Du har två Lightsabers.")
    
                    else:
                        print("Du har en double-bladed Lightsaber.")
                        
                    print("\nI turneringen möter du:\nBattle droid - Vinner\nClone Trooper - Vinner\nBoba Fett - Vinner\nAssajj Ventress - Vinner\nObi-Wan Kenobi - Vinner\nCount Dooku - Vinner\nYoda - Vinner\n Sheev Palpatine - Vinner\nDarth Vader - Vinner\nLuke Skywalker - Förlorar")
                    
                else: # jedi knight
                    print("Du är en Jedi Knight.")
                    
                    weapon = random.randint(1,4)
    
                    time.sleep(1)
                    print("\n-\n")
    
                    if(weapon == 1):
                        print("Ditt vapen är en vanlig Lightsaber.")
    
                    elif(weapon == 2):
                        print("Du har en modifierad Lightsaber med inbyggd Blaster.")
    
                    elif(weapon == 3):
                        print("Du har två Lightsabers.")
    
                    else:
                        print("Du har en double-bladed Lightsaber.")
                    
                    print("\nI turneringen möter du:\nBattle droid - Vinner\nClone Trooper - Vinner\nBoba Fett - Vinner\nAssajj Ventress - Vinner\nObi-Wan Kenobi - Vinner\nCount Dooku - Vinner\nYoda - Förlorar")
              
        
            elif(experience == 2):
                print("Du har erfarenthet i strid, men gör fortfarande vissa fel.")
        
                master = random.randint(1,2)
        
                time.sleep(1)
                print("\n-\n")
        
                if(master == 1):
                    print("Du är en Jedi Knight")
                    
                    weapon = random.randint(1,4)
    
                    time.sleep(1)
                    print("\n-\n")
    
                    if(weapon == 1):
                        print("Ditt vapen är en vanlig Lightsaber.")
    
                    elif(weapon == 2):
                        print("Du har en modifierad Lightsaber med inbyggd Blaster.")
    
                    elif(weapon == 3):
                        print("Du har två Lightsabers.")
    
                    else:
                        print("Du har en double-bladed Lightsaber.")
                        
                    print("\nI turneringen möter du:\nBattle droid - Vinner\nClone Trooper - Vinner\nBoba Fett - Vinner\nAssajj Ventress - Vinner\nObi-Wan Kenobi - Förlorar")
                    
                    
                else:
                    print("Du är en Padawan.")
                    
                    weapon = random.randint(1,4)
    
                    time.sleep(1)
                    print("\n-\n")
    
                    if(weapon == 1):
                        print("Ditt vapen är en vanlig Lightsaber.")
    
                    elif(weapon == 2):
                        print("Du har en modifierad Lightsaber med inbyggd Blaster.")
    
                    elif(weapon == 3):
                        print("Du har två Lightsabers.")
    
                    else:
                        print("Du har en double-bladed Lightsaber.")
                        
                    print("\nI turneringen möter du:\nBattle droid - Vinner\nClone Trooper - Vinner\nBoba Fett - Vinner\nAssajj Ventress - Förlorar")
        
            else:
                print("Du har nästan ingen erfarenhet.")
        
                time.sleep(1)
                print("\n.\n")
        
                print("Du är en Padawan.")
                
                weapon = random.randint(1,4)
    
                time.sleep(1)
                print("\n-\n")
    
                if(weapon == 1):
                    print("Ditt vapen är en vanlig Lightsaber.")
    
                elif(weapon == 2):
                    print("Du har en modifierad Lightsaber med inbyggd Blaster.")
    
                elif(weapon == 3):
                    print("Du har två Lightsabers.")
    
                else:
                    print("Du har en double-bladed Lightsaber.")
                        
                print("\nI turneringen möter du:\nBattle droid - Vinner\nClone Trooper - Vinner\nBoba Fett - Förlorar")
    
        elif(alliance == 2): # grey jedi
            print("Du är en Grey Jedi.")
        
            experience = random.randint(1,3)
        
            time.sleep(1)
            print("\n-\n")
        
            if(experience == 1): # mycket erfarenhet
                print("Du har mycket erfarenhet i strid.")
                
                weapon = random.randint(1,4)
    
                time.sleep(1)
                print("\n-\n")
    
                if(weapon == 1):
                    print("Ditt vapen är en vanlig Lightsaber.")
    
                elif(weapon == 2):
                    print("Du har en modifierad Lightsaber med inbyggd Blaster.")
    
                elif(weapon == 3):
                    print("Du har två Lightsabers.")
    
                else:
                    print("Du har en double-bladed Lightsaber.")
                        
                print("\nI turneringen möter du:\nBattle droid - Vinner\nClone Trooper - Vinner\nBoba Fett - Vinner\nAssajj Ventress - Vinner\nObi-Wan Kenobi - Vinner\nCount Dooku - Vinner\nYoda - Vinner\n Sheev Palpatine - Vinner\nDarth Vader - Vinner\nLuke Skywalker - Förlorar")
                
            elif(experience == 2): # medel erfarenhet
                print("Du har erfarenhet i strid, men gör fortfarande vissa misstag.")
                
                weapon = random.randint(1,4)
    
                time.sleep(1)
                print("\n-\n")
    
                if(weapon == 1):
                    print("Ditt vapen är en vanlig Lightsaber.")
    
                elif(weapon == 2):
                    print("Du har en modifierad Lightsaber med inbyggd Blaster.")
    
                elif(weapon == 3):
                    print("Du har två Lightsabers.")
    
                else:
                    print("Du har en double-bladed Lightsaber.")
                        
                print("\nI turneringen möter du:\nBattle droid - Vinner\nClone Trooper - Vinner\nBoba Fett - Vinner\nAssajj Ventress - Vinner\nObi-Wan Kenobi - Vinner\nCount Dooku - Vinner\nYoda - Förlorar")
                
            else: # ingen erfarenhet
                print("Du har nästan ingen erfarenhet.")
                
                weapon = random.randint(1,4)
    
                time.sleep(1)
                print("\n-\n")
    
                if(weapon == 1):
                    print("Ditt vapen är en vanlig Lightsaber.")
    
                elif(weapon == 2):
                    print("Du har en modifierad Lightsaber med inbyggd Blaster.")
    
                elif(weapon == 3):
                    print("Du har två Lightsabers.")
    
                else:
                    print("Du har en double-bladed Lightsaber.")
                        
                print("\nI turneringen möter du:\nBattle droid - Vinner\nClone Trooper - Vinner\nBoba Fett - Förlorar")
    
        else: # sith
            print("Du är en Sith.")
        
            experience = random.randint(1,3)
        
            time.sleep(1)
            print("\n-\n")
        
            if(experience == 1): # mycket erfarenhet
                print("Du har mycket erfarenhet i strid.")
            
                master_or_apprentice = random.randint(1,2)
            
                time.sleep(1)
                print("\n-\n")
            
                if(master_or_apprentice == 1): # sith master
                    print("Du är en Sith Master.")
                    
                    weapon = random.randint(1,4)
    
                    time.sleep(1)
                    print("\n-\n")
    
                    if(weapon == 1):
                        print("Ditt vapen är en vanlig Lightsaber.")
    
                    elif(weapon == 2):
                        print("Du har en modifierad Lightsaber med inbyggd Blaster.")
    
                    elif(weapon == 3):
                        print("Du har två Lightsabers.")
    
                    else:
                        print("Du har en double-bladed Lightsaber.")
                        
                    print("\nI turneringen möter du:\nBattle droid - Vinner\nClone Trooper - Vinner\nBoba Fett - Vinner\nAssajj Ventress - Vinner\nObi-Wan Kenobi - Vinner\nCount Dooku - Vinner\nYoda - Vinner\n Sheev Palpatine - Vinner\nDarth Vader - Vinner\nLuke Skywalker - Förlorar")
                    
                else: # sith apprentice
                    print("Du är en Sith Apprentice.")
                    
                    weapon = random.randint(1,4)
    
                    time.sleep(1)
                    print("\n-\n")
    
                    if(weapon == 1):
                        print("Ditt vapen är en vanlig Lightsaber.")
    
                    elif(weapon == 2):
                        print("Du har en modifierad Lightsaber med inbyggd Blaster.")
    
                    elif(weapon == 3):
                        print("Du har två Lightsabers.")
    
                    else:
                        print("Du har en double-bladed Lightsaber.")
                        
                    print("\nI turneringen möter du:\nBattle droid - Vinner\nClone Trooper - Vinner\nBoba Fett - Vinner\nAssajj Ventress - Vinner\nObi-Wan Kenobi - Vinner\nCount Dooku - Vinner\nYoda - Förlorar")
                    
            elif(experience == 2): # medel erfarenhet
                print("Du har erfarenhet i strid, men gör fortfarande vissa misstag.")
            
                time.sleep(1)
                print("\n-\n")
            
                print("Du är en Sith Apprentice.")
                
                weapon = random.randint(1,4)
    
                time.sleep(1)
                print("\n-\n")
    
                if(weapon == 1):
                    print("Ditt vapen är en vanlig Lightsaber.")
    
                elif(weapon == 2):
                    print("Du har en modifierad Lightsaber med inbyggd Blaster.")
    
                elif(weapon == 3):
                    print("Du har två Lightsabers.")
    
                else:
                    print("Du har en double-bladed Lightsaber.")
                        
                print("\nI turneringen möter du:\nBattle droid - Vinner\nClone Trooper - Vinner\nBoba Fett - Vinner\nAssajj Ventress - Vinner\nObi-Wan Kenobi - Vinner\nCount Dooku - Förlorar")
            
            else: # ingen erfarenhet
                print("Du har nästan ingen erfarenhet.")
            
                master_or_apprentice = random.randint(1,3)
            
                time.sleep(1)
                print("\n-\n")
            
                if(master_or_apprentice == 1):
                    print("Du är en Sith Apprentice.")
                    
                    weapon = random.randint(1,4)
    
                    time.sleep(1)
                    print("\n-\n")
    
                    if(weapon == 1):
                        print("Ditt vapen är en vanlig Lightsaber.")
    
                    elif(weapon == 2):
                        print("Du har en modifierad Lightsaber med inbyggd Blaster.")
    
                    elif(weapon == 3):
                        print("Du har två Lightsabers.")
    
                    else:
                        print("Du har en double-bladed Lightsaber.")
                        
                    print("\nI turneringen möter du:\nBattle droid - Vinner\nClone Trooper - Vinner\nBoba Fett - Vinner\nAssajj Ventress - Vinner\nObi-Wan Kenobi - Förlorar")
            
                elif(master_or_apprentice == 2):
                    print("Du är en Sith Assassin.")
                    
                    weapon = random.randint(1,4)
    
                    time.sleep(1)
                    print("\n-\n")
    
                    if(weapon == 1):
                        print("Ditt vapen är en vanlig Lightsaber.")
    
                    elif(weapon == 2):
                        print("Du har en modifierad Lightsaber med inbyggd Blaster.")
    
                    elif(weapon == 3):
                        print("Du har två Lightsabers.")
    
                    else:
                        print("Du har en double-bladed Lightsaber.")
                        
                    print("\nI turneringen möter du:\nBattle droid - Vinner\nClone Trooper - Vinner\nBoba Fett - Vinner\nAssajj Ventress - Förlorar")
            
                else:
                    print("Du är knappt en Sith.")
                    
                    weapon = random.randint(1,4)
    
                    time.sleep(1)
                    print("\n-\n")
    
                    if(weapon == 1):
                        print("Ditt vapen är en vanlig Lightsaber.")
    
                    elif(weapon == 2):
                        print("Du har en modifierad Lightsaber med inbyggd Blaster.")
    
                    elif(weapon == 3):
                        print("Du har två Lightsabers.")
    
                    else:
                        print("Du har en double-bladed Lightsaber.")
                        
                    print("\nI turneringen möter du:\nBattle droid - Vinner\nClone Trooper - Vinner\nBoba Fett - Förlorar")



    elif(force_ability <= 15000 and force_ability >= 10000): # relativt hög midichlorian§                                                                                                                                                                                       §
        print("Du är relativt force sensitive.")
        
        alliance = random.randint(1,3)
        
        time.sleep(1)
        print("\n-\n")
    
        if(alliance == 1): # jedi
            print("Du är en Jedi.")
        
            experience = random.randint(1,3)
    
            time.sleep(1)
            print("\n-\n")
    
            if(experience == 1): # mycket erfarenhet
                print("Du har mycket erfarenhet i strid.")
        
                master = random.randint(1,2)
        
                time.sleep(1)
                print("\n-\n")
        
                if(master == 1): # jedi master
                    print("Du är en Jedi Master.")
                    
                    weapon = random.randint(1,4)
    
                    time.sleep(1)
                    print("\n-\n")
    
                    if(weapon == 1):
                        print("Ditt vapen är en vanlig Lightsaber.")
    
                    elif(weapon == 2):
                        print("Du har en modifierad Lightsaber med inbyggd Blaster.")
    
                    elif(weapon == 3):
                        print("Du har två Lightsabers.")
    
                    else:
                        print("Du har en double-bladed Lightsaber.")
                        
                    print("\nI en turnering möter du:\nBattle droid - Vinner\nClone Trooper - Vinner\nBoba Fett - Vinner\nAssajj Ventress - Vinner\nObi-Wan Kenobi - Vinner\nCount Dooku - Förlorar")
                    
                else: # jedi knight
                    print("Du är en Jedi Knight.")
                    
                    weapon = random.randint(1,4)
    
                    time.sleep(1)
                    print("\n-\n")
    
                    if(weapon == 1):
                        print("Ditt vapen är en vanlig Lightsaber.")
    
                    elif(weapon == 2):
                        print("Du har en modifierad Lightsaber med inbyggd Blaster.")
    
                    elif(weapon == 3):
                        print("Du har två Lightsabers.")
    
                    else:
                        print("Du har en double-bladed Lightsaber.")
                        
                    print("I en turnering möter du:\nBattle droid - Vinner\nClone Trooper - Vinner\nBoba Fett - Vinner\nAssajj Ventress - Vinner\nObi-Wan Kenobi - Förlorar")
              
            elif(experience == 2): # medel erfarenhet
                print("Du har erfarenthet i strid, men gör fortfarande vissa fel.")
        
                master = random.randint(1,2)
        
                time.sleep(1)
                print("\n-\n")
        
                if(master == 1): # jedi knight
                    print("Du är en Jedi Knight")
                    
                    weapon = random.randint(1,4)
    
                    time.sleep(1)
                    print("\n-\n")
    
                    if(weapon == 1):
                        print("Ditt vapen är en vanlig Lightsaber.")
    
                    elif(weapon == 2):
                        print("Du har en modifierad Lightsaber med inbyggd Blaster.")
    
                    elif(weapon == 3):
                        print("Du har två Lightsabers.")
    
                    else:
                        print("Du har en double-bladed Lightsaber.")
                        
                    print("I en turnering möter du:\nBattle droid - Vinner\nClone Trooper - Vinner\nBoba Fett - Vinner\nAssajj Ventress - Vinner\nObi-Wan Kenobi - Förlorar")
                    
                else: # padawan
                    print("Du är en Padawan.")
                    
                    weapon = random.randint(1,4)
    
                    time.sleep(1)
                    print("\n-\n")
    
                    if(weapon == 1):
                        print("Ditt vapen är en vanlig Lightsaber.")
    
                    elif(weapon == 2):
                        print("Du har en modifierad Lightsaber med inbyggd Blaster.")
    
                    elif(weapon == 3):
                        print("Du har två Lightsabers.")
    
                    else:
                        print("Du har en double-bladed Lightsaber.")
                        
                    print("I en turnering möter du:\nBattle droid - Vinner\nClone Trooper - Vinner\nBoba Fett - Vinner\nAssajj Ventress - Förlorar")
        
            else: # ingen erfarenhet
                print("Du har nästan ingen erfarenhet.")
        
                time.sleep(1)
                print("\n.\n")
        
                print("Du är en Padawan.")
                
                weapon = random.randint(1,4)
    
                time.sleep(1)
                print("\n-\n")
    
                if(weapon == 1):
                    print("Ditt vapen är en vanlig Lightsaber.")
    
                elif(weapon == 2):
                    print("Du har en modifierad Lightsaber med inbyggd Blaster.")
    
                elif(weapon == 3):
                    print("Du har två Lightsabers.")
    
                else:
                    print("Du har en double-bladed Lightsaber.")
                        
                print("I en turnering möter du:\nBattle droid - Vinner\nClone Trooper - Vinner\nBoba Fett - Förlorar")
    
        elif(alliance == 2): # grey jedi
            print("Du är en Grey Jedi.")
        
            experience = random.randint(1,3)
        
            time.sleep(1)
            print("\n-\n")
        
            if(experience == 1): # mycket erfarenhet
                print("Du har mycket erfarenhet i strid.")
                
                weapon = random.randint(1,4)
    
                time.sleep(1)
                print("\n-\n")
    
                if(weapon == 1):
                    print("Ditt vapen är en vanlig Lightsaber.")
    
                elif(weapon == 2):
                    print("Du har en modifierad Lightsaber med inbyggd Blaster.")
    
                elif(weapon == 3):
                    print("Du har två Lightsabers.")
    
                else:
                    print("Du har en double-bladed Lightsaber.")
                        
                print("I en turnering möter du:\nBattle droid - Vinner\nClone Trooper - Vinner\nBoba Fett - Vinner\nAssajj Ventress - Vinner\nObi-Wan Kenobi - Vinner\nCount Dooku - Förlorar")
                
            elif(experience == 2): # medel erfarenhet
                print("Du har erfarenhet i strid, men gör fortfarande vissa misstag.")
                
                weapon = random.randint(1,4)
    
                time.sleep(1)
                print("\n-\n")
    
                if(weapon == 1):
                    print("Ditt vapen är en vanlig Lightsaber.")
    
                elif(weapon == 2):
                    print("Du har en modifierad Lightsaber med inbyggd Blaster.")
    
                elif(weapon == 3):
                    print("Du har två Lightsabers.")
    
                else:
                    print("Du har en double-bladed Lightsaber.")
                        
                print("I en turnering möter du:\nBattle droid - Vinner\nClone Trooper - Vinner\nBoba Fett - Vinner\nAssajj Ventress - Vinner\nObi-Wan Kenobi - Förlorar")
                
            else: # ingen erfarenhet
                print("Du har nästan ingen erfarenhet.")
                
                weapon = random.randint(1,4)
    
                time.sleep(1)
                print("\n-\n")
    
                if(weapon == 1):
                    print("Ditt vapen är en vanlig Lightsaber.")
    
                elif(weapon == 2):
                    print("Du har en modifierad Lightsaber med inbyggd Blaster.")
    
                elif(weapon == 3):
                    print("Du har två Lightsabers.")
    
                else:
                    print("Du har en double-bladed Lightsaber.")
                        
                print("I en turnering möter du:\nBattle droid - Vinner\nClone Trooper - Vinner\nBoba Fett - Förlorar")
    
        else: # sith
            print("Du är en Sith.")
        
            experience = random.randint(1,3)
        
            time.sleep(1)
            print("\n-\n")
        
            if(experience == 1): # mycket erfarenhet
                print("Du har mycket erfarenhet i strid.")
            
                master_or_apprentice = random.randint(1,2)
            
                time.sleep(1)
                print("\n-\n")
            
                if(master_or_apprentice == 1): # sith master
                    print("Du är en Sith Master.")
                    
                    weapon = random.randint(1,4)
    
                    time.sleep(1)
                    print("\n-\n")
    
                    if(weapon == 1):
                        print("Ditt vapen är en vanlig Lightsaber.")
    
                    elif(weapon == 2):
                        print("Du har en modifierad Lightsaber med inbyggd Blaster.")
    
                    elif(weapon == 3):
                        print("Du har två Lightsabers.")
    
                    else:
                        print("Du har en double-bladed Lightsaber.")
                        
                    print("I en turnering möter du:\nBattle droid - Vinner\nClone Trooper - Vinner\nBoba Fett - Vinner\nAssajj Ventress - Vinner\nObi-Wan Kenobi - Vinner\nCount Dooku - Vinner\nYoda - Vinner\n Sheev Palpatine - Vinner\nDarth Vader - Vinner\nLuke Skywalker - Förlorar")
                    
                else: # sith apprentice
                    print("Du är en Sith Apprentice.")
                    
                    weapon = random.randint(1,4)
    
                    time.sleep(1)
                    print("\n-\n")
    
                    if(weapon == 1):
                        print("Ditt vapen är en vanlig Lightsaber.")
    
                    elif(weapon == 2):
                        print("Du har en modifierad Lightsaber med inbyggd Blaster.")
    
                    elif(weapon == 3):
                        print("Du har två Lightsabers.")
    
                    else:
                        print("Du har en double-bladed Lightsaber.")
                        
                    print("I en turnering möter du:\nBattle droid - Vinner\nClone Trooper - Vinner\nBoba Fett - Vinner\nAssajj Ventress - Vinner\nObi-Wan Kenobi - Vinner\nCount Dooku - Vinner\nYoda - Förlorar")
            
            elif(experience == 2): # medel erfarenhet
                print("Du har erfarenhet i strid, men gör fortfarande vissa misstag.")
            
                time.sleep(1)
                print("\n-\n")
            
                print("Du är en Sith Apprentice.")
                
                weapon = random.randint(1,4)
    
                time.sleep(1)
                print("\n-\n")
    
                if(weapon == 1):
                    print("Ditt vapen är en vanlig Lightsaber.")
    
                elif(weapon == 2):
                    print("Du har en modifierad Lightsaber med inbyggd Blaster.")
    
                elif(weapon == 3):
                    print("Du har två Lightsabers.")
    
                else:
                    print("Du har en double-bladed Lightsaber.")
                        
                print("I en turnering möter du:\nBattle droid - Vinner\nClone Trooper - Vinner\nBoba Fett - Vinner\nAssajj Ventress - Vinner\nObi-Wan Kenobi - Vinner\nCount Dooku - Förlorar")
            
            else: # ingen erfarenhet
                print("Du har nästan ingen erfarenhet.")
            
                master_or_apprentice = random.randint(1,3)
            
                time.sleep(1)
                print("\n-\n")
            
                if(master_or_apprentice == 1): # sith apprentice
                    print("Du är en Sith Apprentice.")
                    
                    weapon = random.randint(1,4)
    
                    time.sleep(1)
                    print("\n-\n")
    
                    if(weapon == 1):
                        print("Ditt vapen är en vanlig Lightsaber.")
    
                    elif(weapon == 2):
                        print("Du har en modifierad Lightsaber med inbyggd Blaster.")
    
                    elif(weapon == 3):
                        print("Du har två Lightsabers.")
    
                    else:
                        print("Du har en double-bladed Lightsaber.")
                        
                    print("I en turnering möter du:\nBattle droid - Vinner\nClone Trooper - Vinner\nBoba Fett - Vinner\nAssajj Ventress - Vinner\nObi-Wan Kenobi - Förlorar")
            
                elif(master_or_apprentice == 2): # sith assassin
                    print("Du är en Sith Assassin.")
                    
                    weapon = random.randint(1,4)
    
                    time.sleep(1)
                    print("\n-\n")
    
                    if(weapon == 1):
                        print("Ditt vapen är en vanlig Lightsaber.")
    
                    elif(weapon == 2):
                        print("Du har en modifierad Lightsaber med inbyggd Blaster.")
    
                    elif(weapon == 3):
                        print("Du har två Lightsabers.")
    
                    else:
                        print("Du har en double-bladed Lightsaber.")
                        
                    print("I en turnering möter du:\nBattle droid - Vinner\nClone Trooper - Vinner\nBoba Fett - Vinner\nAssajj Ventress - Förlorar")
            
                else: # dogshit sith
                    print("Du är knappt en Sith.")
                    
                    weapon = random.randint(1,4)
    
                    time.sleep(1)
                    print("\n-\n")
    
                    if(weapon == 1):
                        print("Ditt vapen är en vanlig Lightsaber.")
    
                    elif(weapon == 2):
                        print("Du har en modifierad Lightsaber med inbyggd Blaster.")
    
                    elif(weapon == 3):
                        print("Du har två Lightsabers.")
    
                    else:
                        print("Du har en double-bladed Lightsaber.")
                        
                    print("I en turnering möter du:\nBattle droid - Vinner\nClone Trooper - Vinner\nBoba Fett - Förlorar")

   
    
    elif(force_ability < 10000 and force_ability >= 5000): # medel midichlorian
        print("Du är medelstark med kraften.")
        
        alliance = random.randint(1,3)
        
        time.sleep(1)
        print("\n-\n")
    
        if(alliance == 1): # jedi
            print("Du är en Jedi.")
        
            experience = random.randint(1,3)
    
            time.sleep(1)
            print("\n-\n")
    
            if(experience == 1): # mycket erfarenhet
                print("Du har mycket erfarenhet i strid.")
        
                master = random.randint(1,2)
        
                time.sleep(1)
                print("\n-\n")
        
                if(master == 1): # jedi master
                    print("Du är en Jedi Master.")
                    
                    weapon = random.randint(1,4)
    
                    time.sleep(1)
                    print("\n-\n")
    
                    if(weapon == 1):
                        print("Ditt vapen är en vanlig Lightsaber.")
    
                    elif(weapon == 2):
                        print("Du har en modifierad Lightsaber med inbyggd Blaster.")
    
                    elif(weapon == 3):
                        print("Du har två Lightsabers.")
    
                    else:
                        print("Du har en double-bladed Lightsaber.")
                        
                    print("\nI turneringen möter du:\nBattle droid - Vinner\nClone Trooper - Vinner\nBoba Fett - Vinner\nAssajj Ventress - Vinner\nObi-Wan Kenobi - Vinner\nCount Dooku - Vinner\nYoda - Vinner\n Sheev Palpatine - Vinner\nDarth Vader - Vinner\nLuke Skywalker - Förlorar")
                    
                else: # jedi knight
                    print("Du är en Jedi Knight.")
                    
                    weapon = random.randint(1,4)
    
                    time.sleep(1)
                    print("\n-\n")
    
                    if(weapon == 1):
                        print("Ditt vapen är en vanlig Lightsaber.")
    
                    elif(weapon == 2):
                        print("Du har en modifierad Lightsaber med inbyggd Blaster.")
    
                    elif(weapon == 3):
                        print("Du har två Lightsabers.")
    
                    else:
                        print("Du har en double-bladed Lightsaber.")
                        
                    print("\nI turneringen möter du:\nBattle droid - Vinner\nClone Trooper - Vinner\nBoba Fett - Vinner\nAssajj Ventress - Vinner\nObi-Wan Kenobi - Vinner\nCount Dooku - Förlorar")
              
        
            elif(experience == 2):
                print("Du har erfarenthet i strid, men gör fortfarande vissa fel.")
        
                master = random.randint(1,2)
        
                time.sleep(1)
                print("\n-\n")
        
                if(master == 1):
                    print("Du är en Jedi Knight")
                else:
                    print("Du är en Padawan.")
        
            else:
                print("Du har nästan ingen erfarenhet.")
        
                time.sleep(1)
                print("\n.\n")
        
                print("Du är en Padawan.")
    
        elif(alliance == 2): # grey jedi
            print("Du är en Grey Jedi.")
        
            experience = random.randint(1,3)
        
            time.sleep(1)
            print("\n-\n")
        
            if(experience == 1): # mycket erfarenhet
                print("Du har mycket erfarenhet i strid.")
                
                weapon = random.randint(1,4)
    
                time.sleep(1)
                print("\n-\n")
    
                if(weapon == 1):
                    print("Ditt vapen är en vanlig Lightsaber.")
    
                elif(weapon == 2):
                    print("Du har en modifierad Lightsaber med inbyggd Blaster.")
    
                elif(weapon == 3):
                    print("Du har två Lightsabers.")
    
                else:
                    print("Du har en double-bladed Lightsaber.")
                        
                print("\nI turneringen möter du:\nBattle droid - Vinner\nClone Trooper - Vinner\nBoba Fett - Vinner\nAssajj Ventress - Vinner\nObi-Wan Kenobi - Vinner\nCount Dooku - Förlorar")
                
            elif(experience == 2): # medel erfarenhet
                print("Du har erfarenhet i strid, men gör fortfarande vissa misstag.")
                
                weapon = random.randint(1,4)
    
                time.sleep(1)
                print("\n-\n")
    
                if(weapon == 1):
                    print("Ditt vapen är en vanlig Lightsaber.")
    
                elif(weapon == 2):
                    print("Du har en modifierad Lightsaber med inbyggd Blaster.")
    
                elif(weapon == 3):
                    print("Du har två Lightsabers.")
    
                else:
                    print("Du har en double-bladed Lightsaber.")
                        
                print("\nI turneringen möter du:\nBattle droid - Vinner\nClone Trooper - Vinner\nBoba Fett - Vinner\nAssajj Ventress - Vinner\nObi-Wan Kenobi - Förlorar")
                
            else: # ingen erfarenhet
                print("Du har nästan ingen erfarenhet.")
                
                weapon = random.randint(1,4)
    
                time.sleep(1)
                print("\n-\n")
    
                if(weapon == 1):
                    print("Ditt vapen är en vanlig Lightsaber.")
    
                elif(weapon == 2):
                    print("Du har en modifierad Lightsaber med inbyggd Blaster.")
    
                elif(weapon == 3):
                    print("Du har två Lightsabers.")
    
                else:
                    print("Du har en double-bladed Lightsaber.")
                        
                print("\nI turneringen möter du:\nBattle droid - Vinner\nClone Trooper - Vinner\nBoba Fett - Förlorar")
    
        else: # sith
            print("Du är en Sith.")
        
            experience = random.randint(1,3)
        
            time.sleep(1)
            print("\n-\n")
        
            if(experience == 1): # mycket erfarenhet
                print("Du har mycket erfarenhet i strid.")
            
                master_or_apprentice = random.randint(1,2)
            
                time.sleep(1)
                print("\n-\n")
            
                if(master_or_apprentice == 1): # sith master
                    print("Du är en Sith Master.")
                    
                    weapon = random.randint(1,4)
    
                    time.sleep(1)
                    print("\n-\n")
    
                    if(weapon == 1):
                        print("Ditt vapen är en vanlig Lightsaber.")
    
                    elif(weapon == 2):
                        print("Du har en modifierad Lightsaber med inbyggd Blaster.")
    
                    elif(weapon == 3):
                        print("Du har två Lightsabers.")
    
                    else:
                        print("Du har en double-bladed Lightsaber.")
                        
                    print("\nI turneringen möter du:\nBattle droid - Vinner\nClone Trooper - Vinner\nBoba Fett - Vinner\nAssajj Ventress - Vinner\nObi-Wan Kenobi - Vinner\nCount Dooku - Förlorar")
                    
                else: # sith apprentice
                    print("Du är en Sith Apprentice.")
                    
                    weapon = random.randint(1,4)
    
                    time.sleep(1)
                    print("\n-\n")
    
                    if(weapon == 1):
                        print("Ditt vapen är en vanlig Lightsaber.")
    
                    elif(weapon == 2):
                        print("Du har en modifierad Lightsaber med inbyggd Blaster.")
    
                    elif(weapon == 3):
                        print("Du har två Lightsabers.")
    
                    else:
                        print("Du har en double-bladed Lightsaber.")
                        
                    print("\nI turneringen möter du:\nBattle droid - Vinner\nClone Trooper - Vinner\nBoba Fett - Vinner\nAssajj Ventress - Vinner\nObi-Wan Kenobi - Förlorar")
                
            elif(experience == 2): # medel erfarenhet
                print("Du har erfarenhet i strid, men gör fortfarande vissa misstag.")
            
                time.sleep(1)
                print("\n-\n")
            
                print("Du är en Sith Apprentice.")
                
                weapon = random.randint(1,4)
    
                time.sleep(1)
                print("\n-\n")
    
                if(weapon == 1):
                    print("Ditt vapen är en vanlig Lightsaber.")
    
                elif(weapon == 2):
                    print("Du har en modifierad Lightsaber med inbyggd Blaster.")
    
                elif(weapon == 3):
                    print("Du har två Lightsabers.")
    
                else:
                    print("Du har en double-bladed Lightsaber.")
                        
                print("\nI turneringen möter du:\nBattle droid - Vinner\nClone Trooper - Vinner\nBoba Fett - Vinner\nAssajj Ventress - Vinner\nObi-Wan Kenobi - Förlorar")
            
            else: # ingen erfarenhet
                print("Du har nästan ingen erfarenhet.")
            
                master_or_apprentice = random.randint(1,3)
            
                time.sleep(1)
                print("\n-\n")
            
                if(master_or_apprentice == 1): # sith apprentice
                    print("Du är en Sith Apprentice.")
                    
                    weapon = random.randint(1,4)
    
                    time.sleep(1)
                    print("\n-\n")
    
                    if(weapon == 1):
                        print("Ditt vapen är en vanlig Lightsaber.")
    
                    elif(weapon == 2):
                        print("Du har en modifierad Lightsaber med inbyggd Blaster.")
    
                    elif(weapon == 3):
                        print("Du har två Lightsabers.")
    
                    else:
                        print("Du har en double-bladed Lightsaber.")
                        
                    print("\nI turneringen möter du:\nBattle droid - Vinner\nClone Trooper - Vinner\nBoba Fett - Vinner\nAssajj Ventress - Vinner\nObi-Wan Kenobi - Förlorar")
            
                elif(master_or_apprentice == 2): # sith assassin
                    print("Du är en Sith Assassin.")
                    
                    weapon = random.randint(1,4)
    
                    time.sleep(1)
                    print("\n-\n")
    
                    if(weapon == 1):
                        print("Ditt vapen är en vanlig Lightsaber.")
    
                    elif(weapon == 2):
                        print("Du har en modifierad Lightsaber med inbyggd Blaster.")
    
                    elif(weapon == 3):
                        print("Du har två Lightsabers.")
    
                    else:
                        print("Du har en double-bladed Lightsaber.")
                        
                    print("\nI turneringen möter du:\nBattle droid - Vinner\nClone Trooper - Vinner\nBoba Fett - Vinner\nAssajj Ventress - Förlorar")
                    
                else: # dogshit sith
                    print("Du är knappt en Sith.")
                    
                    weapon = random.randint(1,4)
    
                    time.sleep(1)
                    print("\n-\n")
    
                    if(weapon == 1):
                        print("Ditt vapen är en vanlig Lightsaber.")
    
                    elif(weapon == 2):
                        print("Du har en modifierad Lightsaber med inbyggd Blaster.")
    
                    elif(weapon == 3):
                        print("Du har två Lightsabers.")
    
                    else:
                        print("Du har en double-bladed Lightsaber.")
                        
                    print("\nI turneringen möter du:\nBattle droid - Vinner\nClone Trooper - Vinner\nBoba Fett - Förlorar")

 
       
    else: # låg midichlorian
        print("Du är relativt svag med kraften.")
    
        alliance = random.randint(1,3)
        
        time.sleep(1)
        print("\n-\n")
    
        if(alliance == 1): # jedi
            print("Du är en Jedi.")
        
            experience = random.randint(1,3)
    
            time.sleep(1)
            print("\n-\n")
    
            if(experience == 1): # mycket erfarenhet
                print("Du har mycket erfarenhet i strid.")
        
                master = random.randint(1,2)
        
                time.sleep(1)
                print("\n-\n")
        
                if(master == 1): # jedi master
                    print("Du är en Jedi Master.")
                    
                    weapon = random.randint(1,4)
    
                    time.sleep(1)
                    print("\n-\n")
    
                    if(weapon == 1):
                        print("Ditt vapen är en vanlig Lightsaber.")
    
                    elif(weapon == 2):
                        print("Du har en modifierad Lightsaber med inbyggd Blaster.")
    
                    elif(weapon == 3):
                        print("Du har två Lightsabers.")
    
                    else:
                        print("Du har en double-bladed Lightsaber.")
                        
                    print("\nI turneringen möter du:\nBattle droid - Vinner\nClone Trooper - Vinner\nBoba Fett - Vinner\nAssajj Ventress - Vinner\nObi-Wan Kenobi - Förlorar")
                    
                else: # jedi knight
                    print("Du är en Jedi Knight.")
                    
                    weapon = random.randint(1,4)
    
                    time.sleep(1)
                    print("\n-\n")
    
                    if(weapon == 1):
                        print("Ditt vapen är en vanlig Lightsaber.")
    
                    elif(weapon == 2):
                        print("Du har en modifierad Lightsaber med inbyggd Blaster.")
    
                    elif(weapon == 3):
                        print("Du har två Lightsabers.")
    
                    else:
                        print("Du har en double-bladed Lightsaber.")
                        
                    print("\nI turneringen möter du:\nBattle droid - Vinner\nClone Trooper - Vinner\nBoba Fett - Vinner\nAssajj Ventress - Förlorar")
                    
            elif(experience == 2): # medel erfarenhet
                print("Du har erfarenthet i strid, men gör fortfarande vissa fel.")
        
                master = random.randint(1,2)
        
                time.sleep(1)
                print("\n-\n")
        
                if(master == 1): # jedi knight
                    print("Du är en Jedi Knight")
                    
                    weapon = random.randint(1,4)
    
                    time.sleep(1)
                    print("\n-\n")
    
                    if(weapon == 1):
                        print("Ditt vapen är en vanlig Lightsaber.")
    
                    elif(weapon == 2):
                        print("Du har en modifierad Lightsaber med inbyggd Blaster.")
    
                    elif(weapon == 3):
                        print("Du har två Lightsabers.")
    
                    else:
                        print("Du har en double-bladed Lightsaber.")
                        
                    print("\nI turneringen möter du:\nBattle droid - Vinner\nClone Trooper - Vinner\nBoba Fett - Vinner\nAssajj Ventress - Förlorar")
                    
                else: # padawan
                    print("Du är en Padawan.")
                    
                    weapon = random.randint(1,4)
    
                    time.sleep(1)
                    print("\n-\n")
    
                    if(weapon == 1):
                        print("Ditt vapen är en vanlig Lightsaber.")
    
                    elif(weapon == 2):
                        print("Du har en modifierad Lightsaber med inbyggd Blaster.")
    
                    elif(weapon == 3):
                        print("Du har två Lightsabers.")
    
                    else:
                        print("Du har en double-bladed Lightsaber.")
                        
                    print("\nI turneringen möter du:\nBattle droid - Vinner\nClone Trooper - Vinner\nBoba Fett - Förlorar")
        
            else: # ingen erfarenhet
                print("Du har nästan ingen erfarenhet.")
        
                time.sleep(1)
                print("\n.\n")
        
                print("Du är en Padawan.")
                
                weapon = random.randint(1,4)
    
                time.sleep(1)
                print("\n-\n")
    
                if(weapon == 1):
                    print("Ditt vapen är en vanlig Lightsaber.")
    
                elif(weapon == 2):
                    print("Du har en modifierad Lightsaber med inbyggd Blaster.")
    
                elif(weapon == 3):
                    print("Du har två Lightsabers.")
    
                else:
                    print("Du har en double-bladed Lightsaber.")
                        
                print("\nI turneringen möter du:\nBattle droid - Vinner\nClone Trooper - Förlorar")
    
        elif(alliance == 2): # grey jedi
            print("Du är en Grey Jedi.")
        
            experience = random.randint(1,3)
        
            time.sleep(1)
            print("\n-\n")
        
            if(experience == 1): # mycket erfarenhet
                print("Du har mycket erfarenhet i strid.")
                
                weapon = random.randint(1,4)
    
                time.sleep(1)
                print("\n-\n")
    
                if(weapon == 1):
                    print("Ditt vapen är en vanlig Lightsaber.")
    
                elif(weapon == 2):
                    print("Du har en modifierad Lightsaber med inbyggd Blaster.")
    
                elif(weapon == 3):
                    print("Du har två Lightsabers.")
    
                else:
                    print("Du har en double-bladed Lightsaber.")
                        
                print("\nI turneringen möter du:\nBattle droid - Vinner\nClone Trooper - Vinner\nBoba Fett - Vinner\nAssajj Ventress - Vinner\nObi-Wan Kenobi - Förlorar")
                
            elif(experience == 2): # medel erfarenhet
                print("Du har erfarenhet i strid, men gör fortfarande vissa misstag.")
                
                weapon = random.randint(1,4)
    
                time.sleep(1)
                print("\n-\n")
    
                if(weapon == 1):
                    print("Ditt vapen är en vanlig Lightsaber.")
    
                elif(weapon == 2):
                    print("Du har en modifierad Lightsaber med inbyggd Blaster.")
    
                elif(weapon == 3):
                    print("Du har två Lightsabers.")
    
                else:
                    print("Du har en double-bladed Lightsaber.")
                        
                print("\nI turneringen möter du:\nBattle droid - Vinner\nClone Trooper - Vinner\nBoba Fett - Vinner\nAssajj Ventress - Förlorar")
                
            else: # ingen erfarenhet
                print("Du har nästan ingen erfarenhet.")
                
                weapon = random.randint(1,4)
    
                time.sleep(1)
                print("\n-\n")
    
                if(weapon == 1):
                    print("Ditt vapen är en vanlig Lightsaber.")
    
                elif(weapon == 2):
                    print("Du har en modifierad Lightsaber med inbyggd Blaster.")
    
                elif(weapon == 3):
                    print("Du har två Lightsabers.")
    
                else:
                    print("Du har en double-bladed Lightsaber.")
                        
                print("\nI turneringen möter du:\nBattle droid - Vinner\nClone Trooper - Vinner\nBoba Fett - Förlorar")
    
        else: # sith
            print("Du är en Sith.")
        
            experience = random.randint(1,3)
        
            time.sleep(1)
            print("\n-\n")
        
            if(experience == 1): # mycket erfarenhet
                print("Du har mycket erfarenhet i strid.")
            
                master_or_apprentice = random.randint(1,2)
            
                time.sleep(1)
                print("\n-\n")
            
                if(master_or_apprentice == 1): # sith master
                    print("Du är en Sith Master.")
                    
                    weapon = random.randint(1,4)
    
                    time.sleep(1)
                    print("\n-\n")
    
                    if(weapon == 1):
                        print("Ditt vapen är en vanlig Lightsaber.")
    
                    elif(weapon == 2):
                        print("Du har en modifierad Lightsaber med inbyggd Blaster.")
    
                    elif(weapon == 3):
                        print("Du har två Lightsabers.")
    
                    else:
                        print("Du har en double-bladed Lightsaber.")
                        
                    print("\nI turneringen möter du:\nBattle droid - Vinner\nClone Trooper - Vinner\nBoba Fett - Vinner\nAssajj Ventress - Vinner\nObi-Wan Kenobi - Förlorar")
                    
                else: # sith apprentice
                    print("Du är en Sith Apprentice.")
                    
                    weapon = random.randint(1,4)
    
                    time.sleep(1)
                    print("\n-\n")
    
                    if(weapon == 1): 
                        print("Ditt vapen är en vanlig Lightsaber.")
    
                    elif(weapon == 2):
                        print("Du har en modifierad Lightsaber med inbyggd Blaster.")
    
                    elif(weapon == 3):
                        print("Du har två Lightsabers.")
    
                    else:
                        print("Du har en double-bladed Lightsaber.")
                        
                    print("\nI turneringen möter du:\nBattle droid - Vinner\nClone Trooper - Vinner\nBoba Fett - Vinner\nAssajj Ventress - Förlorar")
     
            elif(experience == 2):
                print("Du har erfarenhet i strid, men gör fortfarande vissa misstag.")
            
                time.sleep(1)
                print("\n-\n")
            
                print("Du är en Sith Apprentice.")
            
            else:
                print("Du har nästan ingen erfarenhet.")
            
                master_or_apprentice = random.randint(1,3)
            
                time.sleep(1)
                print("\n-\n")
            
                if(master_or_apprentice == 1):
                    print("Du är en Sith Apprentice.")
            
                elif(master_or_apprentice == 2):
                    print("Du är en Sith Assassin.")
            
                else:
                    print("Du är knappt en Sith.")


        weapon = random.randint(1,4)
    
        time.sleep(1)
        print("\n-\n")
    
        if(weapon == 1):
            print("Ditt vapen är en vanlig Lightsaber.")
    
        elif(weapon == 2):
            print("Du har en modifierad Lightsaber med inbyggd Blaster.")
    
        elif(weapon == 3):
            print("Du har två Lightsabers.")
    
        else:
            print("Du har en double-bladed Lightsaber.")
    

else:
    print("Du är inte force sensitive")
