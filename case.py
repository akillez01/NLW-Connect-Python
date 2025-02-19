class MinhaClase:
    def __enter__(self):
      print("entrei!!!")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Sai!!!")
        
        
with MinhaClase() as mc:
  print("Estou aqui dentro!!")