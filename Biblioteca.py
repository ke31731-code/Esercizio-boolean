# Utente entra in biblioteca se:
#1) non ha ritardi con le consegne di libri oppure è un abbonato premium
#Il programma stampa true se almeno una delle due condizioni è vera, mentre false negli altri casi

nome= input("Come ti chiami?")

ritardo = input("Sei in ritardo con la consegna di qualche libro usato,"+ nome + "?")

premium = input("Sei abbonato?s/n").lower

entra = (ritardo == "no") or (premium == "si")

print(entra)