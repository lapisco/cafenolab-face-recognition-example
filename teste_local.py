import os

import cv2
import dlib
import numpy as np


def teste():
    detector = dlib.get_frontal_face_detector()
    detectorPontos = dlib.shape_predictor("res/shape_predictor_68_face_landmarks.dat")
    reconhecimentoFacial = dlib.face_recognition_model_v1("res/dlib_face_recognition_resnet_model_v1.dat")
    
    indices = np.load("res/indices.pickle", allow_pickle=True)
    descritoresFaciais = np.load("res/descritores.npy", allow_pickle=True)

    limiar = 0.45
    cap = cv2.VideoCapture(0)
    nome = ''
    while True:

        ret_val, frame = cap.read()
        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        dets = detector(rgb_image)
        for det in dets:
            e, t, d, b = (int(det.left()), int(det.top()), int(det.right()), int(det.bottom()))
            cv2.rectangle(frame,(det.left(), det.top()), (det.right(), det.bottom()), (0, 255, 0), 2)
            pontos = detectorPontos(frame, det)
            descritorFacial = reconhecimentoFacial.compute_face_descriptor(frame, pontos)
            listaDescritorFacial = [fd for fd in descritorFacial]
            npArrayDescritorFacial = np.asarray(listaDescritorFacial, dtype=np.float64)
            npArrayDescritorFacial = npArrayDescritorFacial[np.newaxis, :]
            
            distancias = np.linalg.norm(npArrayDescritorFacial - descritoresFaciais, axis=1) # Calculo das distancias euclidianas

            minimo = np.argmin(distancias)
            distanciaMinima = distancias[minimo-1]
            if distanciaMinima <= limiar:
                nome = os.path.split(indices[minimo-1])[1].split(".")[0]
                # e, t, d, b = (int(det.left()), int(det.top()), int(det.right()), int(det.bottom()))
                cv2.rectangle(frame,(det.left(), det.top()), (det.right(), det.bottom()), (0, 255, 0), 2)
                texto = f"{nome} {distanciaMinima:.4f}"
                cv2.putText(frame, texto, (d, b), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 2)
                cv2.putText(frame, texto, (d, b), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 0), 1)
                print(f'RECONHECIDO')
                print(nome)

            else:
                nome = "Nao registrado"

                print(f'NAO RECONHECIDO' )
                print(nome)
                # e, t, d, b = (int(det.left()), int(det.top()), int(det.right()), int(det.bottom()))
                cv2.rectangle(frame,(det.left(), det.top()), (det.right(), det.bottom()), (0, 0, 255), 2)
            
                texto = f"{nome} {distanciaMinima:.4f}"
                cv2.putText(frame, texto, (d, b), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 2)
                cv2.putText(frame, texto, (d, b), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 1)
        cv2.imshow('Cam', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
    cap.release()
    cv2.destroyAllWindows()
