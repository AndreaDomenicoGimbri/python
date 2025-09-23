class Prodotti_distributore:
    def __init__(self,nome,quantità,costo):
        if nome is None or quantità==0 or costo==0.00:
            print("parametri prodotto non validi")
            raise ValueError
        self.nome=nome
        self.quantità=quantità
        self.costo=costo
    
    def get_attribute(self, nome_attr):
        if hasattr(self, nome_attr):
            return getattr(self, nome_attr)
        else:
            raise AttributeError(f"L'attributo '{nome_attr}' non esiste.")
    
    def stampa(self):
        if(self.quantità>0):
            return print(f"prodotto{self.nome}con costo{self.costo} è disponibile in quantità {self.quantità}")
        return print(f"prodotto{self.nome}con costo{self.costo} non è piu disponibile")


class dispenser:

    def __init__(self,lista_prodotti_disponibili):
        if not lista_prodotti_disponibili:
            self.lista_prodotti_disponibili=[]
        else:
            self.lista_prodotti_disponibili=lista_prodotti_disponibili
    
    def aggiungi_prodotto(self,Prodotti_distributore):
        for p in self.lista_prodotti_disponibili:
            if p.nome==Prodotti_distributore.nome:
                p.quantità+=Prodotti_distributore.quantità
                return
        self.lista_prodotti_disponibili.append(Prodotti_distributore)

    def elimina_prodotto(self,Prodotti_distributore):
        eliminato=False
        for p in self.lista_prodotti_disponibili:
            if p.nome==Prodotti_distributore.nome :
                if p.quantità>0:
                    p.quantità-=1
                    eliminato=True
                    print ("prodotto eliminaton con successo")
                        
                else:
                    print("prodotto terminato")
        else:
            print("prodotto non presente in catalogo")
        return eliminato

    def acquista_prodotto(self ,prodotto):
        if not self.elimina_prodotto(prodotto):
            return print("prodotto non acquistato con successo")
        return print("prodotto acquistato con successo")

        

        

        



    





        
    



    
        
    


    
 
        



        
