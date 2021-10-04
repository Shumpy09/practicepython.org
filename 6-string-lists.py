text = str(input("Podaj tekst: "))
rev_text = text[::-1]

if text == rev_text:
    print(f"Twoj tekst: '{text}' jest palindromem: {rev_text}.")
else:
    print(f"Twoj tekst: '{text}' nie jest palindromem.")
