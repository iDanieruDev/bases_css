def cero():
  return False

def uno():
  return False

def dos():
  return True

def tres():
  return False

def cuatro():
  return True

def cinco():
  return False

def seis():
  return True

def siete():
  return False

def ocho():
  return True

def nueve():
  return False

def diez():
  return True       

def quien_sabe():
  print("hay un 50'%' de que sea par ;)")      

def es_par(a):
    numero = {
        1: uno,
        2: dos,
        3: tres,
        4: cuatro,
        5: cinco,
        6: seis,
        7: siete,
        8: ocho,
        9: nueve,
        10: diez
    }    
    func = numero.get(a, quien_sabe)    
    func()