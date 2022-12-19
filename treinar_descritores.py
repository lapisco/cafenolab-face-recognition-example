import os

import numpy as np
import pandas as pd
import pickle 


def treinar():
    indice = {}
    if os.path.exists('res/descritores.npy') == True: 
        descritoresFaciais = np.load('res/descritores.npy', allow_pickle=True)
    else:
        descritoresFaciais = None
    df = pd.read_csv('banco_local.csv')
    for i in range(len(df)):
        
        vetor = df.values[i][0]
        vetor = vetor[1:-1]
        vetor = vetor.split(',')
        vetor = [float(i) for i in vetor]

        if df.values[i][3] != 'OK':
            listaDescritorFacial = vetor
            npArrayDescritorFacial = np.asarray(listaDescritorFacial, dtype=np.float32)
            npArrayDescritorFacial = npArrayDescritorFacial[np.newaxis, :]
            if descritoresFaciais is None:
                descritoresFaciais = npArrayDescritorFacial
            
            descritoresFaciais = np.concatenate((descritoresFaciais, npArrayDescritorFacial), axis=0)
            df.values[i][3] = 'OK'
            indice[i] = df.values[i][1]
           
            print(f'Descritor {i} adicionado')

    df.to_csv('banco_local.csv')
    np.save("res/descritores.npy", descritoresFaciais)
    
    with open("res/descritores.pickle", 'wb') as f:
        pickle.dump(descritoresFaciais, f)

    with open("res/indices.pickle", 'wb') as f:
        pickle.dump(indice, f)

    print('Descritores locais treinados')