import os
import glob

import pandas as pd
import numpy as np
import cv2
import dlib

def gerar_bancos():
    '''
    Funcao para gerar os dados
    '''

    #Libs Facial
    detectorFace = dlib.get_frontal_face_detector()
    detectorPontos = dlib.shape_predictor("res/shape_predictor_68_face_landmarks.dat")
    reconhecimentoFacial = dlib.face_recognition_model_v1("res/dlib_face_recognition_resnet_model_v1.dat")
    
    if os.path.exists('banco_local.csv'):
        df = pd.read_csv('banco_local.csv')
    else:
        df = pd.DataFrame(columns=['encodings', 'pessoa', 'enviado_banco', 'enviado_descritores'])
     
    for f in os.listdir("Dataset_Treinamento"):
            
        # Define o caminho de cada pessoa
        videoPath = f'Dataset_Treinamento/{f}'
        pessoa = f

        #Insert nos bancos
        for arquivo in glob.glob(f'{videoPath}/Frames/*'):

            if '_OK' not in str(arquivo):
                imagem = cv2.imread(arquivo)
                facesDetectadas = detectorFace(imagem, 1)

                #Renomeando para evitar repeticao no banco
                os.rename(arquivo, arquivo.replace('.', '_OK.'))

                for face in facesDetectadas:

                    ### Salvando descritores
                    pontosFaciais = detectorPontos(imagem, face)
                    descritorFacial = reconhecimentoFacial.compute_face_descriptor(imagem, pontosFaciais)
                    listaDescritorFacial = [df for df in descritorFacial]
                    npArrayDescritorFacial = np.asarray(listaDescritorFacial, dtype=np.float64)
                    npArrayDescritorFacial = npArrayDescritorFacial[np.newaxis, :]
                    lista = npArrayDescritorFacial.tolist()

                    ### Jogando no banco_local.csv
                    df2 = pd.DataFrame([[str(lista[0]), pessoa, '-', '-']], columns=['encodings', 'pessoa', 'enviado_banco', 'enviado_descritores'])
                    df = df.append(df2)
                    df.to_csv('banco_local.csv', index=False)

            elif '_OK' in str(arquivo):
                imagem = cv2.imread(arquivo)
                facesDetectadas = detectorFace(imagem, 1)

                #Renomeando para evitar repeticao no banco
                os.rename(arquivo, arquivo.replace('.', '_OK.'))

                for face in facesDetectadas:

                    ### Salvando descritores
                    pontosFaciais = detectorPontos(imagem, face)
                    descritorFacial = reconhecimentoFacial.compute_face_descriptor(imagem, pontosFaciais)
                    listaDescritorFacial = [df for df in descritorFacial]
                    npArrayDescritorFacial = np.asarray(listaDescritorFacial, dtype=np.float64)
                    npArrayDescritorFacial = npArrayDescritorFacial[np.newaxis, :]
                    lista = npArrayDescritorFacial.tolist()

                    ### Jogando no banco_local.csv
                    df2 = pd.DataFrame([[str(lista[0]), pessoa, '-', '-']], columns=['encodings', 'pessoa', 'enviado_banco', 'enviado_descritores'])
                    df = df.append(df2)
                    df.to_csv('banco_local.csv', index=False)

                    
    print("Bancos gerados!")
    