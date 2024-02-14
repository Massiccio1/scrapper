
import csv
from googlesearch import search
# from webbrowser import open

headerList = ['Azienda', 'link1', 'link2', 'link3']
  
open CSV file and assign header 
with open("parsed.csv", 'w') as file: 
    dw = csv.DictWriter(file, delimiter=',',  
                        fieldnames=headerList) 
    dw.writeheader() 


with open('nomi_aziende.csv', 'r') as csvfile:

    # Creare un lettore CSV
    reader = csv.reader(csvfile, delimiter=',')

    # Creare uno scrittore CSV
    
    # Saltare l'intestazione
    next(reader, None)
    
    
    with open('parsed.html', 'a') as f:
            f.write("<table border=\"1\">")
            
    

    # Iterare sulle righe del file CSV
    for row in reader:

        # Ottenere il nome dell'azienda
        azienda = row[0]
        
        # Creare la query di ricerca per Google
        query = f"sito web {azienda}"
        
        print("sto cerdando: ", azienda)
        
        row=[azienda]
        
        for url in search(query, num=1, stop=3, pause=1):
            # Aggiungere l'URL alla riga
            print(url)
            row.append(url)
        
        while len(row)<4:
            row.append("placeholder")
            
        # 'a' per append
        with open('parsed.csv', 'a', newline='') as output:
            writer = csv.writer(output, delimiter=',')
            writer.writerow(row)
        
        with open('parsed.html', 'a') as f:
            htmlstring=f'<tr>\
                <td>{row[0][:70]}</td>\
                <td><a target=\"_blank\" href=\"{row[1]}\">{row[1][:30]}</a></td>\
                <td><a target=\"_blank\" href=\"{row[2]}\">{row[2][:30]}</a></td>\
                <td><a target=\"_blank\" href=\"{row[3]}\">{row[3][:30]}</a></td>\
            </tr>\n'
            f.write(htmlstring)

        # Aprire la pagina di ricerca Google in un nuovo tab del browser
        # g_url = f"https://www.google.com/search?q={query}"
        # webbrowser.open(g_url)
    with open('parsed.html', 'a') as f:
        f.write("</table>")
print("-"*20)
print("FINE")
