
import csv
import requests
from googlesearch import search
# from webbrowser import open

# Aprire il file CSV in modalità lettura e scrittura

links = []

with open('nomi_aziende.csv') as csvfile:

    # Creare un lettore CSV
    reader = csv.reader(csvfile, delimiter=',')

    # Creare uno scrittore CSV
    
    # Saltare l'intestazione
    next(reader, None)

    # Iterare sulle righe del file CSV
    for row in reader:

        # Ottenere il nome dell'azienda
        azienda = row[0]
        
        # Creare la query di ricerca per Google
        query = f"sito web {azienda}"
        
        print("sto cerdando: ", azienda)
        
        row=[azienda]
        
        for url in search(query, num=3, stop=1):
            # Aggiungere l'URL alla riga
            row.append(url)
            
        # 'a' per append
        with open('parsed.csv', 'a', newline='') as output:
            writer = csv.writer(output, delimiter=',')
            writer.writerow(row)
            

        # Aprire la pagina di ricerca Google in un nuovo tab del browser
        # g_url = f"https://www.google.com/search?q={query}"
        # webbrowser.open(g_url)
    
exit(0)

with open('parsed.csv') as csvfile:
        
    writer = csv.writer(csvfile, delimiter=',')

        # Scrivere la riga aggiornata sul file CSV
        # writer.writerow(row)
        
    


# Funzione per trovare l'URL del sito web
def trova_url_sito_web(query):

    # Inviare la query di ricerca a Google
    risposta = requests.get(f"https://www.google.com/search?q={query}")

    # Trovare il primo link nei risultati di ricerca
    url = re.findall(r"(?<=href=\").+?(?=\")", risposta.text)[0]

    # Restituire l'URL
    return url
