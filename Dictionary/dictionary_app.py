import json
#oletuksena oleva sanakirja
my_dictionary = {
    "wizard": "velho",
    "witch": "noita",
    "wand": "sauva",
    "magic": "taika"
    }

print("Tämä on englanti-suomi sanakirja.")

# avataan sanakirja ja poikkeuksien käsittelyä
try:
    with open("sanakirja.json", "r") as f:
        my_dictionary = json.load(f)
        print("Sanakirjan lataus onnistui.\n")
except OSError:
    print("Ongelmia sanakirjan lataamisessa. Käytetään sanakirjan perusvalikoimaa.\n")
except ValueError:
    print("Sanakirja on korruptoitunut\n")

#ohjelma ja jos sanaa ei löydy voi käyttäjä määritellä sen uutena sanana sanakirjaan
while True:
    word = input("Anna sana englanniksi (tai paina enter poistuaksesi): ").lower().strip()
    #.lower() muuttaa kirjaimet pieniksi, .strip() poistaa välit sanan edestä ja lopusta
    
    if not word:
        break #lopettaa ohjelman jos käyttäjä painaa enteriä
    
    if not word.isalpha(): #.isalpha() tarkistaa onko sanassa vain kirjaimia
        print("Syötä vain kirjaimia.\n")
        continue
    
    if word in my_dictionary:
        print(f"{word} = {my_dictionary[word]}\n")
    
    else:
        new_def = input(f"{word} ei ole sanakirjassa! Ole hyvä ja syötä käännös tai paina enter peruuttaaksesi toiminnon): ").lower().strip()
        print("")
        
        if not new_def.isalpha():
            print("Numerot eivät ole sallittuja.\n") #kieltää numeroiden syöttämisen järjestelmään

        if new_def.isalpha():
            my_dictionary[word] = new_def #lisää sanan kirjastoon

#luodaan uusi sanakirja, jos tiedostoa ei ole olemassa, ja tallennetaan sanakirjan json muotoon
try:
    with open("sanakirja.json", "w") as f:
        json.dump(my_dictionary, f)
        print("Sanakirja tallennettu. Kiitos kun käytit ohjelmaa! ")
except OSError:
    print("Sanakirjan tallentaminen epäonnistui.")
except ValueError:
    print("Sanakirja on korruptoitunut\n")