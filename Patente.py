# Chiedo all'utente se ha la patente (S/N)

eta = int(input("Quanti anni hai? "))
patente = input("Ciao! Sei in possesso della licenza di guida? s/n: ")

#Se età >= 18 e patente == si: posso far stampare "true": altrimenti uscirà false 

guida =(eta >=18) and (patente == "si")
print(guida)




