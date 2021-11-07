import sys
import time
import os
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(4./100)

def vraag1():
    os.system("cls")
    slowprint('''
    Je zit rustig spaanse duif te luisteren en tijdens het luisteren wordt je onderbroken door lawaai 
    A: je gaat kijken B: Je gaat verder luisteren''')
   
    inputText = input()
    slowprint(inputText)
    if inputText == "A" or inputText == "a":
     vraag2()
    elif inputText == "B" or inputText == "b":
        vraag10()

#story line 1
def vraag2():
    os.system("cls")
    slowprint(''' 
    Je loopt naar buiten en vraagt aan de buurvrouw Wat is er aan de hand waarom is iedereen zo aan het stressen
     A:Je schrikt van het aantwoord en begint actie te ondernemen 
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraag3()
   

def vraag3():
    os.system("cls")
    slowprint(''' 
    Je hoort van de buurvrouw dat nederland wordt aangevallen door de taliban je ben hier erg van gechrokken
    je begint je gezin te roepen en uit te leggen wat er aan de hand is je begint plannen te maken om te vluchten je moet eerst 
    eten en drinken inslaan en een manier vinden om het land uit tekomen
    A:Jullie gaan met de auto  B: jullie besluiten op de voet te gaan
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraag4()
    elif inputText == "B" or inputText == "b":
        vraag23()

def vraag4():
    os.system("cls")
    slowprint(''' 
    Jullie stappen in de auto en beginnen te rijden alle wegen zitten helemaal vol met auto's die het land uit willen
    wat er voor zorgt dat er files op alle wegen staan
    A:jullie stappen uit en gaan verder te voet B:je wacht in de auto tot het verkeer door rijdt
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraag23()
    elif inputText == "B" or inputText == "b":
        vraag9()


def vraag9():
    os.system("cls")
    slowprint(''' 
    je wordt uit de auto getrokken door iemand van de taliban en wordt neer geschoten
    EINDE.
    ''')
 

def vraag10():
    os.system("cls")
    slowprint(''' 
    Je begint verder te luisteren en gaat daarna een film kijken
    nog steeds hoor je buiten chaos
    A:ga toch wel naar buiten om te kijken wat er aan de hand is B: je blijft film kijken 
     ''')
   
    inputText = input()
    slowprint(inputText)
    if inputText == "A" or inputText == "a":
     vraag31()
    elif inputText == "B" or inputText == "b":
        vraag11()

def vraag11():
    os.system("cls")
    slowprint('''
    midden  in de film hoor je schiet geluiden en schreeuwen (maar je denkt dat het in de film is )
    daarna hoor je geklop op de deur wat langzaam veranderd naar bonken
    je loopt naar benden en ziet 2 manen met wapens in een outfit die je nog nooit hebt gezien 
    A: je doet de deur open B:je verstopt je 
    ''')
   
    inputText = input()
    slowprint(inputText)
    if inputText == "A" or inputText == "a":
     vraag28()
    elif inputText == "B" or inputText == "b":
        vraag12()

def vraag12():
    os.system("cls")
    slowprint('''
    maar waar ga je je verstoppen
     A:in de trapkast achter de spullen  B:onder je bed
     ''')
   
    inputText = input()
    slowprint(inputText)
    if inputText == "A" or inputText == "a":
     vraag13()
    elif inputText == "B" or inputText == "b":
        vraag14()

def vraag14():
    os.system("cls")
    slowprint('''
    je verstopt je onder je bed en hoort je gezin schreeuwen nadat ze 1 voor 1 gevangen worden genomen
    ze kijken rond het huis en gaan alle kamers rond uiteindelijk komen ze in jouw kamer en ze beginnen te zoeken
    ze kijken onder het bed en ze hebben je gevonden

    Je wordt ook meegenomen

    The end
        ''')
   
def vraag13():
    os.system("cls")
    slowprint(''' 
    je houdt je adem in en je hoort ze langs lopen ze openen de trapkast en kijken snel rond ze zien je niet
    en je wacht ongeveer een uur in de trapkast totdat je zeker bent dat het veilig is je begint langzaam de deur open te doen 
    je gaat de trapkast uit en schrikt dat iedereen weg is tot verbazing is je kleine broertje 
    uit de handen gebleven van de taliban (hij verstopte zich in de  openhaard)
    A: je gaat vluchten met je broertje 
    ''')
   
    inputText = input()
    slowprint(inputText)
    if inputText == "A" or inputText == "a":
     vraag15()
    

    

def vraag15():
    os.system("cls")
    slowprint(''' 
    je grijpt je broertje en begint de deur uit te rennen jullie pakken onderweg allebei een rugtas en vullen die in met water, eten 
    en gereedschap dat handig is om bij je te hebben
    jullie beginnen een plan te maken om uit het land te komen 
    A:jullie gaan richting het water en proberen nederland te verlaten per boot
    
    ''')
   
    inputText = input()
    slowprint(inputText)
    if inputText == "A" or inputText == "a":
     vraag16()
    


def vraag16():  #keuze vrouw verbandoos broertje leven of dood
    os.system("cls")
    slowprint(''' 
    jullie beginnen te lopen naar de zee jullie moeten nog erg ver lopen dus jullie stoppen voor een kleine pauze. 
    onderweg komen jullie een vrouw tegen die hulp nodig heeft ze is gewond en je kan haar helpen maar dat levert je wel vertraging op
    A:je helpt de vrouw     B:je zegt dat je haar niet kan helpen 
    
    ''')
   
    inputText = input()
    slowprint(inputText)
    if inputText == "A" or inputText == "a":
     vraag17()
    elif inputText == "B" or inputText == "b":
        vraag21()

def vraag17():
    os.system("cls")
    slowprint(''' 
    je helpt de  vrouw en ze zegt bedankt je vraagt haar of ze weet welke richting de zee is en ze wijst naar het westen 
    jullie beginnen richting het westen te lopen om bij de zee te komen moet je langs een hoog hek 
    A:je zoekt een manier om onder het hek door te komen  B: je gaat over het hek 
    
    ''')
   
    inputText = input()
    slowprint(inputText)
    if inputText == "A" or inputText == "a":
     vraag30()
    elif inputText == "B" or inputText == "b":
        vraag18()

def vraag18():
    os.system("cls")
    slowprint(''' 
    je klimt over het hek en komt veilig aan de anderen kant je broertje klimt ook over het hek maar 
    zijn voet glijd weg en hij valt van het hek af je probeert hem te vangen maar hij valt met ze ruggengraat op een steen
    je  begint je broertje te helpen maar merkt al snel dat hij niet kan bewegen
    A:je draagt hem op je rug    
    ''')
   
    inputText = input()
    slowprint(inputText)
    if inputText == "A" or inputText == "a":
     vraag21()
    
def vraag21():
    os.system("cls")
    slowprint(''' 
    je loopt met je broertje op je rug richting de waterkant en ziet een motorbootje liggen 
    jij begint het bootje in het water te duwen en jullie varen richting engeland

    The End
    
    ''')

def vraag19():
    os.system("cls")
    slowprint(''' 
    Je laat je broertje achter en gaat verder zonder hem je haalt het naar het water en vindt een boot
    je vaart naar engeland maar je boot wordt geraakt door een vloedgolf 
    en slaat om  je hebt geen eten en drinken en na 2 dagen overlijd je door uitdroging

    The End
    
    ''')

    
def vraag20():
    os.system("cls")
    slowprint(''' 
    je hebt er voor gekozen om de vrouw niet te helpen en jullie lopen met toeval richting het westen 
    jullie komen voor een groot hek te staan 

    A:je klimt er over B: je zoekt een manier om er onder te gaan
    ''')
   
    inputText = input()
    slowprint(inputText)
    if inputText == "A" or inputText == "a":
     vraag18()
    elif inputText == "B" or inputText == "b":
        vraag30()


def vraag30():
    os.system("cls")
    slowprint('''
    Jullie besluiten dat het hek erg hoog is en dat jullie er niet overheen gaan klimmen
    jullie zoeken een manier om eronder door te komen door geluk vinden jullie een schep op de grond
    je gebruikt hem om een kleine kuil te graven waar door je onder het hek door kan 
    A:jullie gaan er onder door B:jullie gaan er toch overheen
    ''')
   
    inputText = input()
    slowprint(inputText)
    if inputText == "A" or inputText == "a":
     vraag22()
    elif inputText == "B" or inputText == "b":
        vraag18()

def vraag22():
    os.system("cls")
    slowprint('''
    jullie komen met succes aan bij het water en zien een bootje liggen jullie gebruiken het om naar engeland
    te varen na een paar dagen op de gevaarlijke zee redden jullie het naar engeland

    The end
    ''')
   

def vraag23():
    os.system("cls")
    slowprint('''
    je begint een plan te maken met je gezin over welke richting jullie opgaan
    jullie besluiten dat jullie richting de duitse grens gaan na een lange dag lopen besluiten jullie om een tussenstop te maken en uit terusten
    jullie hebben het koud en proberen op te warmen
    A: je maakt een kampvuur B:je maakt geen kampvuur voor de zekerheid want straks zien ze je
    ''')
   
    inputText = input()
    slowprint(inputText)
    if inputText == "A" or inputText == "a":
     vraag24()
    elif inputText == "B" or inputText == "b":
        vraag26()

def vraag24():
    os.system("cls")
    slowprint('''
    je hebt besloten om een kampvuur te maken je gaat er lekker dichtbij zitten aangezien het erg koud is
    todat je in de verte geschreeuw hoort je hoort wapens die afgevuurd worden je begint te rennen met je gezin 
    na 5 minuten rennen vinden jullie een oude schuur waar jullie je snel in verstoppen 
    na een half uur wachten is de kust veilig je blijft daar slapen morgen vroeg gaan jullie weer verder op pad
    jullie komen in de buurt van de duitse grens waneer je in 1 keer een hand op je schouder krijgt 
    een man met een hoofdoek spreekt je aan en spreekt amper engels 
    hij zegt ik kan jullie helpen te onstnappen maar daar staat een prijs tegenover hij wilt al je bezitingen hebben
    A:je geeft je spullen op en wordt geholpen B: je zegt nee tegen de hulp
    ''')
   
    inputText = input()
    slowprint(inputText)
    if inputText == "A" or inputText == "a":
     vraag25()
    elif inputText == "B" or inputText == "b":
        vraag27()


def vraag25():
    os.system("cls")
    slowprint('''
   jullie geven jullie spullen op en lopen mee met de man na een paar minuten lopen komen jullie aan op een vluchtelingen kamp
   die goed bewaakt is je wacht hier 2 weken voordat je eindelijk geholpen wordt je stapt met je gezin in een bus vol met andere vluchtelingen
   de bus begint te rijden richting de duitse grens na een lange tocht in de bus komen jullie eindelijk aan in duitsland 
   jullie voelen je opgelucht dat jullie eindelijk veilig zijn

   The end 
   ''')
   
def vraag26():
    os.system("cls")
    slowprint('''
    je hebt er voor gekozen om de hulp af te slaan jullie beginnen verder te lopen richting het oosten het lijkt eeuwig te duren 
    na een lange dag lopen gaan jullie weer rusten jullie merken dat er nog erg weinig eten en drinken is
    jullie verdelen het eerlijk en gaan slapen jullie worden niet fijn wakker want jullie hebben het koud en de grond ligt niet lekker
    jullie beginnen weer te lopen en uiteindelijk hebben jullie de duitse grens gevonden en vertellen tegen de grens bewaking 
    waarom jullie hier zijn ze laten jullie binnen en helpen jullie naar een opvang kamp

    The end
    ''')
   
   
def vraag27():
    os.system("cls")
    slowprint('''
    jullie hebben besloten geen kampvuur te maken en gaan slapen jullie worden wakker en zien in de verte1 een man rond lopen
    je loopt er naar toe om hem om hulp te vragen nadat je weet dat hij geen vijand is roep je je familie 
    jullie komen in de buurt van de duitse grens waneer je in 1 keer een hand op je schouder krijgt 
    een man met een hoofdoek spreekt je aan en spreekt amper engels 
    hij zegt ik kan jullie helpen te onstnappen maar daar staat een prijs tegenover hij wilt al je bezitingen hebben
    A:je geeft je spullen op en wordt geholpen B: je zegt nee tegen de hulp
    ''')
   
    inputText = input()
    slowprint(inputText)
    if inputText == "A" or inputText == "a":
     vraag25()
    elif inputText == "B" or inputText == "b":
        vraag26()



def vraag28():
    os.system("cls")
    slowprint('''
    je hebt besloten de deur open te doen en je wordt begroet met een harde klap in je gezicht waarna je wordt meegenomen 
    en gevangen gezet

    The end
    ''')
   
    inputText = input()
    slowprint(inputText)
    if inputText == "A" or inputText == "a":
     vraag2()
    elif inputText == "B" or inputText == "b":
        vraag10()




def vraag31():
    os.system("cls")
    slowprint(''' 
   je besluit om toch buiten te gaan kijken je ziet mensen rennen voor hun leven je schrikt hiervan en gaat terug naar binnen
   A:je rent terug naar boven
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraag11()
   
vraag1()