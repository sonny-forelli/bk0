class Book:

    def __init__(self,path):
        self.read(path)
        

    def read(self,path):
        self.words=[]
        with open(path,'r') as f:
            
            for line in f:
                line=line.lower()
                line=line.replace('--',' ')
                for word in line.split():
                    
                    self.words.append(word.strip(' “”’‘’\'\".,?/!;:-_()[]&'))
            
                """
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                self.words=[word.strip(' .,!')
                            for word in line.lower().replace('--',' ').split()]
"""
#############################################

                
ok=False
while not ok:
    p=input('path:\n')
    try:
        b=Book(p)
        ok=True
    except UnicodeDecodeError:
        print('wrong file')
    except FileNotFoundError:
        print('file not found')
    except:
        print('unknown error')

