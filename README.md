# Virksomheds-search

## Hvad er dette?
Programmet bruger [CVRAPI's](https://cvrapi.dk) API til at søge efter virksomheder der er indregistreret i danmark. Programmet kan bruges til at finde informationer omkring hvad end registreret virksomhed såsom addresse, mail, telefon nummer osv, man ku også kalde det en [who.is](who.is) for virksomheder i stedet for domæner.

## Første Snippet
Der enligt ikke så meget at sige andet end at det er et simpelt api request program der prettifier outputtet.


## STATUS
Jeg har mistet alle idéer til hvordan jeg kan bygge videre på den så planen er i den nære fremtid optimerere jeg koden/adder funktioner, har du noget input du gerne vil se må du meget gerne skrive til mig på [kontakt\@1ia.tech](mailto:kontakt@1ia.tech?subject=idéer)


## Hvordan fungere programmet?
### Søg Virksomhed
Det er faktisk forholdsvis simpelt. Vi starter med at modtage et input fra brugeren. Derefter tjekker vi, om der er noget mellemrum, og hvis der er, bliver det erstattet med %20. Dette gør vi, fordi API'en ikke kan modtage mellemrum som et input. Derefter sender vi en POST-request til API'en, hvor vi vil modtage et output i et JSON-format. Jeg valgte at sige, at det ikke er overskueligt bare at lade al dataen blive printet. Derfor gav jeg valgmuligheden for at vælge, hvad du vil se.


### Søg Telefon nummer
Her får du kun information om, hvilken virksomhed der står bag telefonnummeret. Men da formatet for, hvordan folk skriver telefonnumre, er så forskelligt, har jeg været nødt til at erstatte både mellemrum og fjerne "+45", hvis det er angivet. Det gør jeg her: ```user_input.replace(" ", "").replace("+45", "")```. API'en tager nemlig kun imod nummeret uden "+45" og uden mellemrum.
