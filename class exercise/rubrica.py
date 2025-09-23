class ElementoRubrica:

    def __init__(self, numero, identificativo_proprietario):
        if len(numero) != 10:
            raise ValueError("Numero di cifre non corretto (devono essere 10)")
        self.numero = numero
        self.identificativo_proprietario = identificativo_proprietario

    def stampa(self):
        print(f" Contatto: {self.identificativo_proprietario} | Numero: {self.numero}")


class Rubrica:

    def __init__(self, contatti=None):
        self.contatti = contatti if contatti else {}

    def aggiungi_contatto(self, elemento):
        nome = elemento.identificativo_proprietario
        numero = elemento.numero

        if nome in self.contatti:
            scelta = input(f"⚠️ Il contatto '{nome}' esiste già. Vuoi aggiornare il numero? (y/n): ").lower()
            if scelta == 'y':
                self.contatti[nome] = numero
                print("Numero aggiornato.")
            else:
                print(" Numero mantenuto invariato.")
        else:
            self.contatti[nome] = numero
            print(" Contatto aggiunto.")

    def elimina_contatto(self, elemento):
        nome = elemento.identificativo_proprietario
        if nome in self.contatti:
            del self.contatti[nome]
            print("🗑️ Contatto eliminato.")
        else:
            print(" Contatto non presente.")

    def stampa_rubrica(self):
        if not self.contatti:
            print(" Rubrica vuota.")
            return
        for nome, numero in self.contatti.items():
            print(f"{nome} → {numero}")

    def cerca_contatto(self, elemento):
        nome = elemento.identificativo_proprietario
        if nome in self.contatti:
            print(f" Contatto trovato: {nome} → {self.contatti[nome]}")
        else:
            print(" Contatto non trovato.")
