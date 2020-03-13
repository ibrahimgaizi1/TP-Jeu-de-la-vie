#Implémentation sans numpy

def calcul_nb_voisins(Z):
    forme = len(Z), len(Z[0])
    N = [[0, ] * (forme[0]) for i in range(forme[1])]
    for x in range(1, forme[0] - 1):
        for y in range(1, forme[1] - 1):
               N[x][y] = Z[x-1][y-1] + Z[x][y-1]+Z[x+1][y-1] + Z[x-1][y] + 0 +Z[x+1][y] + Z[x-1][y+1]+Z[x][y+1]+Z[x+1][y+1]
 
 
 
 
    return N 
    
    
    
-----------------
# On définit la fonction iteration_jeu comme suit :

def iteration_jeu(Z):

    forme = len(Z), len(Z[0])
    N = calcul_nb_voisins(Z)
    for x in range(1, forme[0]-1):
        for y in range(1, forme[1]-1):
            if Z[x][y] == 1 and (N[x][y] < 2 or N[x][y] > 3):
                Z[x][y] = 0
            elif Z[x][y] == 0 and N[x][y] == 3:
                Z[x][y] = 1
    return Z






-----------------------

def calcul_nb_voisins_np(X):
    

    
    X = np.array(X)
    nb_voisins_np = np.zeros(X.shape) 
    nb_voisins_np[1:-1, 1:-1] = X[1:-1, :-2] + \
    X[1:-1, 2:] + X[:-2, 1:-1] + X[2:, 1:-1]+ \
    X[:-2, :-2] + X[:-2, 2:] + X[2:, 2:] + X[2:, :-2]
    return(nb_voisins_np)

Z = [[0, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0],
     [0, 1, 0, 1, 0, 0],
     [0, 0, 1, 1, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0]]

calcul_nb_voisins_np(Z)

-----------------------







def iteration_jeu_np(Z): 
    

    
    forme = len(Z), len(Z[0]) 
    Z = np.array(Z) # la modification qu'on va avoir est d'utiliser des array 
    #                 et non des listes de listes
    N = calcul_nb_voisins_np(Z) # On travaille avec calcul_nb_voisins_np(Z) 
    #                             et non calcul_nb_voisins(Z)
    for x in range(1, forme[0]-1): # le reste du code est le même que pour calcul_nb_voisins
        for y in range(1, forme[1]-1): 
            if Z[x][y] == 1 and (N[x][y] < 2 or N[x][y] > 3): 
                Z[x][y] = 0 
            elif Z[x][y] == 0 and N[x][y] == 3: 
                Z[x][y] = 1 
    return Z
   
   
------------------------------



def jeu_np(Z_in, nb_iter):
   
    for j in range(1, nb_iter+1):
        Z_in = iteration_jeu_np(Z_in)
    return(Z_in)
------------------------------



def animate(i):
    jeu_np(Z_huge, 1)
    im = plt.imshow(Z_huge)
    return im,

----------------------------



def animate(i):
    jeu_np(Z_huge, 1)
    shw = plt.imshow(Z_huge)
    return shw,
---------------------------


def imshow_jeu_de_la_vie(Z):
    fig, ax = plt.subplots()
    # On commence par afficher l'état initial de la matrice:
    plt.imshow(np.array(Z))
    plt.title("Etat initial de la matrice")


imshow_jeu_de_la_vie(Z_huge)


def Jeudevie(Z):

    fig, ax = plt.subplots()
    plt.imshow(np.array(Z))
    plt.title("jeu de vie")
    for i in range(1, 10):
        fig, ax = plt.subplots()
        iteration_jeu_np(Z)
        A = np.array(Z)
        plt.imshow(A)
        plt.title("Jeu de la vie  " 
                  + str(i))
        plt.show()
-----------------------------



def Jeudevie(Z):

    fig, ax = plt.subplots()
    plt.imshow(np.array(Z))
    plt.title("jeu de vie")
    for i in range(1, 10):
        fig, ax = plt.subplots()
        iteration_jeu_np(Z)
        A = np.array(Z)
        plt.imshow(A)
        plt.title("Jeu de la vie  " 
                  + str(i))
        plt.show()
-----------------------------




def Jeudevie(Z):

    fig, ax = plt.subplots()
    plt.imshow(np.array(Z))
    plt.title("jeu de vie")
    for i in range(1, 10):
        fig, ax = plt.subplots()
        iteration_jeu_np(Z)
        A = np.array(Z)
        plt.imshow(A)
        plt.title("Jeu de la vie  " 
                  + str(i))
        plt.show()


--------------------------


    def __init__(self, init_state, _time_T):
        self.init_state = init_state # on commence par initialiser self
        self.n_1 = init_state.shape[0] # self 1 et self 2 correspondent aux dimension 
        self.n_2 = init_state.shape[1]# de la matrice init_state
        self._historic_state = np.ndarray((self.n_1, self.n_2, _time_T+1))# on crée un tenseur
        self._historic_state[:, :, 0] = self.init_state # Tridimensionne
    def play(self):
        t = 1
        while(t <= self._time_T):
            self._historic_state[:, :, t-1] = \
                iteration_jeu_np(self._historic_state[:, :, t])
            self.average_life = np.mean(self._historic_state, axis=(2))
            t = t + 1

    def __plot__(self, init_state, _time_T):
        self.average_life = 1/_time_T*self.average_life
        fig, ax = plt.subplots()
        plt.imshow(self.average_life)
        fig.suptitle("moyenne des vie des cellules")
        plt.show()
-------------------------------------------------------------------------------------

