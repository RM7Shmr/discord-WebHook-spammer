import string ,json ,requests ,random 
from pystyle import Colorate ,Colors ,Center 
from os import system 
from time import sleep  # if u see me here fuck u man dont be a skid its
system ('cls')
boucle1 =True 
boucle2 =True 
failed_previous =False 
sent_count =0 
def random_number (OOOO00O0OOO0O0O0O ):
    O0O0000O0OOO0O00O =10 **(OOOO00O0OOO0O0O0O -1 )
    O00OO00OOO0OOOO0O =(10 **OOOO00O0OOO0O0O0O )-1 
    return random .randint (O0O0000O0OOO0O00O ,O00OO00OOO0OOOO0O )
def id_generator (OOO0O0OO0OO000000 =6 ,O0OOO0OOO000O0OOO =string .ascii_uppercase +string .digits ):
    return ''.join (random .choice (O0OOO0OOO000O0OOO )for _OO0OO0O0OO0OOO0O0 in range (OOO0O0OO0OO000000 ))
message =input ("Enter the message you want to send: ")
def send_message (OOOOOO0OO0O0O0OOO ,O0O0O0O00OOO0OO0O ) :
    O0O00O00OO0OO0000 =id_generator (80 )
    OO0O00OOO000OO0O0 ="https://picsum.photos/id/{}/300".format (random .randint (1 ,500 ))
    O00OOOOOOOO00000O =json .dumps ({"content":O0O0O0O00OOO0OO0O ,"username":O0O00O00OO0OO0000 ,"avatar_url":OO0O00OOO000OO0O0 ,"tts":False })
    O00OO00000O0000O0 ={"content-type":"application/json"}
    O00000O0OO00OO0O0 =requests .post (OOOOOO0OO0O0O0OOO ,O00OOOOOOOO00000O ,headers =O00OO00000O0000O0 )
    if not O00000O0OO00OO0O0 .ok :
        if O00000O0OO00OO0O0 .status_code ==429 :
            system ('cls')
            print (Colorate .Horizontal (Colors .black_to_red ,Center .XCenter (header_final )))
            print (Colorate .Horizontal (Colors .black_to_red ,"[/] ..."))
            sleep (2 )
        else :
            system ('cls')
            print (Colorate .Horizontal (Colors .black_to_red ,Center .XCenter (header_final )))
            print (Colorate .Horizontal (Colors .black_to_red ,"[!] Failed to send message !"))
            sleep (15 )
    try :
        system ('cls')
        print (Colorate .Horizontal (Colors .blue_to_green ,Center .XCenter (header_final )))
        print (Colorate .Horizontal (Colors .blue_to_green ,f"[+] Message sended ! [ {sent_count} ]"))
    except :
        system ('cls')
        print (Colorate .Horizontal (Colors .black_to_red ,Center .XCenter (header_final )))
        print (Colorate .Horizontal (Colors .black_to_red ,"[!] Failed to send message !"))
        sleep (15 )
    return True 
header_final ="""
██╗    ███████████████╗██╗  ██╗██████╗ ██████╗██╗  ██ 
██║    ████╔════██╔══████║  ████╔═══████╔═══████║ ██╔ 
██║ █╗ ███████╗ ██████╔█████████║   ████║   ███████╔╝ 
██║███╗████╔══╝ ██╔══████╔══████║   ████║   ████╔═██╗ 
╚███╔███╔█████████████╔██║  ██╚██████╔╚██████╔██║  ██ 
 ╚══╝╚══╝╚══════╚═════╝╚═╝  ╚═╝╚═════╝ ╚═════╝╚═╝  ╚═ 
                 
                 [+] Made by RM7
                 [+] Fuck Skidssssssssss
\n\n\n\n"""
while boucle1 :
    print (Colorate .Horizontal (Colors .yellow_to_red ,Center .XCenter (header_final )))
    print (Colorate .Horizontal (Colors .yellow_to_red ,"[-] Webhook URL ↓"))
    webhook_url =input ("")
    if webhook_url .startswith ("https://discord.com/api/webhooks/"):
        boucle1 =False 
        system ('cls')
    else :
        system ('cls')
        print (Colorate .Horizontal (Colors .black_to_red ,Center .XCenter (header_final )))
        print (Colorate .Horizontal (Colors .black_to_red ,"[!] Error valid link !"))
        sleep (2 )
        system ('cls')
while boucle2 :
    if (send_message (webhook_url ,message )):
        sent_count +=1 
