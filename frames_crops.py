import os
import glob
import math
from PIL import Image

import cv2
import dlib


detectorFace = dlib.get_frontal_face_detector()

def imagens():
    for f in os.listdir("Dataset_Treinamento"):
        
        # Define o caminho de cada pessoa
        videoPath = f'Dataset_Treinamento/{f}'
        pessoa = f
        
        #Verifica se existe algum arquivo dentro do diretorio
        if os.listdir(f'{videoPath}/') != []:

            #Verifica os paths Frames
            i=0
            if os.path.exists(f'{videoPath}/Frames') == False:
                    os.makedirs(f'{videoPath}/Frames')
                    
                    #Faz os frames
                    for vid in glob.glob(f'{videoPath}/*'):
                        cap= cv2.VideoCapture(vid)
                        frameRate = cap.get(5) # Frame rate
                        while True:
                            frameId = cap.get(1) # Current frame number
                            ret, frame = cap.read()
                            
                            if ret == False:
                                break
                            
                            if (frameId % math.floor(frameRate) == 0): # Save 1 frame per video second
                                facesDetectadas, pont, idx = detectorFace.run(frame)
                                for pos, face in enumerate(facesDetectadas):
                                    if pos == 0:
                                        cv2.imwrite(videoPath+'/Frames/'+pessoa+str(i)+'.png', frame)
                                        print(f'FRAME {pessoa, str(i)} SAVED')
                                        i+=1
            
    print('Frames e Crops gerados!')