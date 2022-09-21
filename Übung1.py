f = input("Herzlich Wilkommen wenn du Rechnen möchtest drücke Bitte Enter")

while True:

 num1 = input("Gib die erste Zahl ein: ")
 oper = input("Welche Rechenoperation soll durchgefuehrt werden? (+,-,/.,*): ")
 num2 = input("Gib die zweite Zahl ein: ")

 num1 = int(num1)
 num2 = int(num2)

 if (oper == "+"):
    print("Deine Rechnung:", num1, " + ", num2)
    print("Ergebnis:", num1 + num2)

 elif(oper == "-"):
    print("Deine Rechnung:", num1, " - ", num2)
    print("Ergebnis:", num1 + num2)
    
 elif(oper == "/"):
    print("Deine Rechnung:", num1, " / ", num2)
    print("Ergebnis:", num1 / num2)
    
 elif(oper == "*"):
    print("Deine Rechnung:", num1, " * ", num2)
    print("Dein Ergebnis:", num1 * num2)
 else:
    print("Deine Eingaben sind nicht gueltig")

 jein = input("Willst du weiter rechnen? (Ja/Nein)")

 jein = str(jein)

 if 'ja' in jein:
    print("sSS")
    
 else:
    print("Bye Bye ")
    break
 
