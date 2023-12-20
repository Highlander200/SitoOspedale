from flask import Flask,render_template

app = Flask(__name__)

LeMieVisite={
    1:["Cardiologia","Una visita specialistica in cardiologia è un appuntamento medico finalizzato alla valutazione della salute cardiaca di un paziente. Comprende la registrazione dei parametri vitali, un colloquio dettagliato sulla storia medica e uno specifico esame fisico concentrato sul cuore. Possono essere eseguiti test diagnostici come l'elettrocardiogramma e, se necessario, ulteriori indagini come l'ecocardiogramma. Il medico discuterà quindi dei risultati, fornirà una diagnosi preliminare e proporrà eventuali piani di trattamento o follow-up. La comunicazione aperta e la condivisione completa delle informazioni sono cruciali durante la visita.","Cardiologo esperto con un approccio empatico."],
    2:["Chirurgia ortopedica","Una visita specialistica in chirurgia ortopedica è un appuntamento medico finalizzato all'esame e alla valutazione di problemi muscolo-scheletrici. Durante la visita, il paziente può sottoporsi a un esame fisico mirato alla zona interessata, potrebbero essere richieste radiografie o altri esami di imaging per una diagnosi più precisa. Il chirurgo ortopedico discuterà dei sintomi, della storia medica e delle opzioni di trattamento disponibili. La visita potrebbe concludersi con la raccomandazione di terapie conservative, interventi chirurgici o terapie fisiche, a seconda della gravità del problema. La comunicazione aperta e la comprensione del piano di trattamento proposto sono essenziali per il paziente durante questa visita.","Chirurgo ortopedico rinomato per riparazioni articolari e ossee."],
    3:["Psichiatria","Una visita specialistica in psichiatria è un appuntamento medico finalizzato alla valutazione e al trattamento dei disturbi mentali e delle condizioni psicologiche. Durante la visita, il paziente avrà un colloquio approfondito con il medico psichiatra, in cui verranno discussi sintomi, storia medica e eventuali fattori di stress. Il medico potrebbe esplorare l'umore, i pensieri, i comportamenti e le relazioni sociali del paziente. A seconda della situazione, potrebbero essere prescritti farmaci psicotropi o consigliate terapie psicologiche come la terapia cognitivo-comportamentale. La visita può servire anche a stabilire un piano di trattamento a lungo termine e a pianificare eventuali follow-up. La comunicazione aperta e la collaborazione tra il paziente e il medico sono fondamentali per il successo del trattamento.","Psichiatra dedicata al benessere mentale dei pazienti."]
}
IMieiMedici={
    1:["Gianfranco di Svevia","Cardiologo","img/DiSvevia.jpg"],
    2:["Marco Bianchi","Chirurgo Ortopedico","img/Bianchi.jpg"],
    3:["Lucia Ferrara","Psichiatra","img/Ferrara.jpg"]        
}
LeMieAnalisi={
    1:["Emocromo completo","L'emocromo completo è un esame del sangue che fornisce informazioni sulla quantità e sulla salute delle cellule del sangue. I principali parametri misurati includono l'emoglobina, che trasporta l'ossigeno nel sangue, l'ematocrito che indica la percentuale di volume occupato dalle cellule del sangue, il numero di globuli rossi responsabili del trasporto dell'ossigeno, il numero di globuli bianchi che combattono le infezioni, e il numero di piastrine coinvolte nella coagulazione del sangue. La formula leucocitaria fornisce la percentuale di diversi tipi di globuli bianchi. Altri parametri come il volume corpuscolare medio, l'emoglobina corpuscolare media e la concentrazione di emoglobina corpuscolare media forniscono ulteriori dettagli sulla dimensione e sulla concentrazione dell'emoglobina nei globuli rossi. Questi dati sono essenziali per diagnosticare o monitorare condizioni come anemie, infezioni e disordini della coagulazione.","Misura delle cellule del sangue per diagnosticare anemie e infezioni."],
    2:["Analisi delle urine","L'analisi delle urine fornisce informazioni cruciali sullo stato del sistema urinario e può rivelare indicazioni su condizioni mediche. Esaminando aspetti come il colore e l'aspetto, la densità urinaria, il pH, la presenza di proteine, glucosio, corpi chetonici, bilirubina e urobilinogeno, è possibile ottenere una panoramica della funzionalità renale, del metabolismo e dello stato di idratazione dell'organismo. Inoltre, la presenza di elementi come emazie, leucociti e cilindri può suggerire eventuali infezioni o problemi renali. L'analisi delle urine è uno strumento diagnostico importante per valutare la salute generale e identificare eventuali condizioni mediche.","Esame per rilevare infezioni urinarie, calcoli renali e problemi renali o metabolici."],
    3:["Profilo lipidico","Il profilo lipidico è un esame del sangue che fornisce informazioni sul livello di lipidi nel sangue. Questo include il colesterolo totale, il colesterolo LDL (lipoproteine a bassa densità), il colesterolo HDL (lipoproteine ad alta densità) e i trigliceridi. Il colesterolo totale è la somma di LDL, HDL e altre lipoproteine. Il colesterolo LDL è spesso chiamato \"colesterolo cattivo\" perché un eccesso può depositarsi sulle pareti delle arterie, aumentando il rischio di malattie cardiovascolari. Al contrario, il colesterolo HDL è noto come \"colesterolo buono\" perché può aiutare a rimuovere il colesterolo in eccesso dalle arterie. I trigliceridi sono un tipo di grasso nel sangue, e livelli elevati possono essere collegati a problemi cardiaci. L'analisi del profilo lipidico è utile per valutare il rischio di malattie cardiovascolari e determinare eventuali interventi necessari per mantenere livelli lipidici sani.","Valuta i livelli di colesterolo e trigliceridi per valutare il rischio cardiovascolare."]
}

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/analisi/')
def analisi():
    return render_template("analisi.html",analisi=LeMieAnalisi)

@app.route('/visite/')
def visite():
    return render_template("visite.html",visite=LeMieVisite)

@app.route('/prenotaVisite/')
def prenotaVisite():
    return render_template("prenotaVisite.html",visite=LeMieVisite)

@app.route('/prenotaAnalisi/')
def prenotaAnalisi():
    return render_template("prenotaAnalisi.html",analisi=LeMieAnalisi)

@app.route('/login/')
def login():
    return render_template("login.html")
  
@app.route('/register/')
def register():
    return render_template("register.html")

@app.route('/medici/')
def medici():
    return render_template("medici.html",medici=IMieiMedici)

app.run(host='0.0.0.0', port=81, debug=True)
