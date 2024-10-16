#assignment 2
#s.encode() muuttaa binääriksi, tarvitaan sivuston tietojen noudossa
#s.decode() muuttaa binäärit luettavaan muotoon
import re
from urllib.error import URLError
from urllib.request import urlopen

print("Ohjelma tarkistaa sisältääkö sivusto vaarallisia sanoja.\n")

while True:
    webpage = input("Syötä tarkistettavan verkkosivun osoite (tai poistu ohjelmasta enterillä): ").strip()

    if not webpage: 
        break

    else:
        try:
            with urlopen(webpage) as response:
                data = response.read().decode("utf-8")
                dangerous_words = re.findall(r"\b(bomb|kill|murder|terror|terrorist|terrorists|terrorism)\b", data, re.IGNORECASE)
                print("Sisältää vaarallisia sanoja: ", len(dangerous_words), "kpl")
                
                data2 = data.encode()
                user_filename = input("Tallennetaan verkkosivusto. Anna tiedostolle nimi ja tiedostomuoto (esim. testi.html): ").strip()
                with open(user_filename, "wb") as output_file: #tallentaminen
                    output_file.write(data2)
                    output_file.close()
                print("Sivuston sisältö tallennettu tiedostoon", user_filename, "\n")
        
        #virheen käsittely, jos tiedostomuoto ei tue UTF-8 muotoa    
        except UnicodeDecodeError: 
            print("Tiedostomuoto ei tue UTF-8.")
            user_filename2 = input("Tallennetaan sellaisenaan. Anna tiedostolle nimi ja tiedostomuoto (esim. kuva.jpg): ").strip()
            with urlopen(webpage) as response:
                data3 = response.read()
                
                with open(user_filename2, "wb") as f:
                    f.write(data3)
                print("Tiedosto tallennettu nimellä", user_filename2, "\n")
        
        #virheen käsittelyä, verkkosivusto ei toimi, tallentaminen ei onnistu, osoite väärin
        except URLError:
            print("Sivustoon", webpage, "ei saada yhteyttä.")
        
        except OSError:
            print("Tiedoston käsittely epäonnistui/keskeytettiin.")

        except ValueError:
            print("Sivuston osoite on virheellinen")