from hashlib import md5 #librairie permettant de hacher un mot de passe
ALPHABET="abcdefghijklmnopqrstuvwxyz"
def break_with_dict(hashes_filename,dict_filename):
    with open(hashes_filename,"r") as hashes:#On ouvre le fichier contenant les mots de passe hachés
        ALL_HASHES=hashes.read().split("\n")#On recupere les haches dans une listes
        with open(dict_filename,"r") as dict_words:#On ouvre le fichier contenant le dictionnaire de mots 
            found_words=[]
            for word in dict_words.read().split("\n"):
                if(md5(str(word).encode()).hexdigest() in ALL_HASHES):#On hache chaque mot du dictionnaire et on verifie s'il est dans les hachés
                    found_words.append(str(word))#On enregistre dans le mot  trouvé dans une liste 
        return found_words #On renvoie la liste 
#found_words=[hashlib.md5(str(word).encode()).hexdigest()  for word in break_with_dict("hashes.txt","dict.txt")]


def brute_force(pwd,pos,siz,chars):
        
    if (pos < siz):
        for  ch in chars:
            brute_force(pwd + ch, pos + 1, siz,chars)
    else:
        if(md5(str(pwd).encode()).hexdigest() in ALL_HASHES):
            print("{} , {}".format(pwd,md5(str(pwd).encode()).hexdigest()),)      

def brute_force_len(chars,len_word,found_words=[]):
    for i in range(1,len_word+1):
        brute_force("",0,i,chars)
    
