meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "AFK":"Away From Keyboard",
            "NPC": "Non-Person Chracter"
    
            }

word=input("Sormak istediğiniz kelimeyi yazınız")
if word in meme_dict:
    print(meme_dict[word])
else:
    print("Aradıınız kelime malesef YOK!")
