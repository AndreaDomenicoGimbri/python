from datetime import date

data_odierna=date.today()

class prodotto:

    def __init__(self,nome,quantità,data_scadenza):
        
        if nome==None or quantità<=0:
            print("selezione non consentità ritentare")
            raise ValueError
        else:
            self.nome=nome
            self.quantità=quantità
            self.data_scadenza=data_scadenza

    
    
    def get_attribute(self, nome_attr):
        if hasattr(self, nome_attr):
            return getattr(self, nome_attr)
        else:
            raise AttributeError(f"L'attributo '{nome_attr}' non esiste.")
    
    
    def stampa(self):
        print(f"nome :{self.nome} quantità: {self.quantità} scadenza : {self.data_scadenza}")


class lista_spesa:

    def __init__(self):
        self.lista_prodotti=[]

    def inserisci_prodotto(self,prodotto):
        if(data_odierna>prodotto.get_attribute("data_scadenza")):
            print("prodotto scaduto inseriscine un altro con una scadenza valida")
            raise ValueError
        else:
            for p in self.lista_prodotti:
                if p.nome.lower()==prodotto.nome.lower():
                    p.quantità+=prodotto.quantità
                    return
               
        self.lista_prodotti.append(prodotto)

    
    def elimina_prodotto(self,prodotto):
        for p in self.lista_prodotti:
            if p.nome.lower()==prodotto.nome.lower():
                if(p.quantità>prodotto.quantità):
                    p.quantità-=prodotto.quantità
                else:
                    self.lista_prodotti.remove(p)
            else:
                print("prodotto non presente nella lista")
    
    def stampa_lista(self):
        if not self.lista_prodotti:
            print("lista vuota che cazzo vuoi stampare mongolo")
        else:
            for p in self.lista_prodotti:
                p.stampa()
    

class negozio:

    def __init__(self):
            self.lista_prodotti_disponibili=[]


        
    def ordina_prodotto(self,prodotto):
        for p in self.lista_prodotti_disponibili:
            if p.nome.lower()==prodotto.nome.lower():
                p.quantità+=prodotto.quantità
                return
        self.lista_prodotti_disponibili.append(prodotto)

        
    def aggiorna_catalogo(self,prodotto):
        for p in self.lista_prodotti_disponibili:
            if p.nome.lower()==prodotto.nome.lower():
                if(p.quantità>prodotto.quantità):
                    p.quantità-=prodotto.quantità
                    return
                else:
                    self.lista_prodotti_disponibili.append(p)
        print("prodotto non presente in catalogo")
        


    def stampa_catalogo(self):
        if not self.lista_prodotti_disponibili:
            print("non puoi acquistare un cazzo non c'è niente mongolo")
            return
        for p in self.lista_prodotti_disponibili:
            p.stampa()

    def getcatalogo(self):
        return self.lista_prodotti_disponibili


               
            
    