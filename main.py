from datetime import date
from carrello_spesa import lista_spesa, prodotto, negozio

data_odierna = date.today()
catalogo_prodotti =[
    prodotto("Latte", 10, date(2025, 8, 5)),
    prodotto("Pane", 15, date(2025, 4, 20)),
    prodotto("Pasta", 30, date(2026, 1, 10)),
    prodotto("Uova", 12, date(2025, 7, 25)),
    prodotto("Biscotti", 25, date(2025, 10, 1)),
    prodotto("Mele", 20, date(2025, 7, 24)),
    prodotto("Tonno", 18, date(2026, 5, 15)),
    prodotto("Yogurt", 8, date(2025, 7, 19)),
]
Catalogo = negozio()
for p in catalogo_prodotti:
    Catalogo.ordina_prodotto(p)

while True:
    choice = input("Vuoi acquistare un prodotto? (y/n): ").lower()
    if choice != 'y':
        break

    lista = lista_spesa()


    nome = input("Nome del prodotto: ")

    try:
        quantità = int(input("Quantità desiderata: "))
        if quantità <= 0:
            print(" Inserisci una quantità maggiore di zero.")
            continue
    except ValueError:
        print(" Quantità non valida. Deve essere un intero.")
        continue

    try:
        prodotto_da_acquistare = prodotto(nome, quantità, data_odierna)
    except ValueError as e:
        print(f"Errore nella creazione del prodotto: {e}")
        continue

#Flag di controllo
    trovato_nome = False
    quantità_disponibile = False
    scadenza_valida = False
    try:
        for p in Catalogo.getcatalogo():
             if prodotto_da_acquistare.get_attribute("nome").lower() == p.get_attribute("nome").lower():
                trovato_nome = True
                if prodotto_da_acquistare.get_attribute("quantità") <= p.get_attribute("quantità"):
                    quantità_disponibile = True
                    if p.get_attribute("data_scadenza") > data_odierna:
                        scadenza_valida = True
                        lista.inserisci_prodotto(prodotto_da_acquistare)
                        Catalogo.aggiorna_catalogo(prodotto_da_acquistare)
                        print("✅ Prodotto aggiunto con successo!")
                        break  
        if not trovato_nome:
            print("Prodotto non presente in catalogo.")
        elif not quantità_disponibile:
            print("Quantità richiesta non disponibile.")
        elif not scadenza_valida:
            print("Prodotto scaduto, meglio evitare.")
    except ValueError:
        print("prova con un altro prodotto")
        continue

