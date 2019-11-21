#! python3
import pickle


class CatNames(object):
   def __init__(self):
       self.names=[]
   def __str__(self):
        return "Customer Class CatNames: "+str(self.names)
   def add_name(self,name):
        self.names.append(name)

a_cat=CatNames()
a_cat.add_name('Thuner')
a_cat.add_name('Apple')
a_cat.add_name('Gracie')
a_cat.add_name('Kitty')

pickle_file = open('custom_class.pkl','W')
pickle.dump(a_cat,pickle_file)
pickle_file.close
