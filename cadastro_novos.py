import os
import time
import cv2

def cadastrar():
    
    nome = input('Digite seu primeiro e seu segundo nome(Ex.: Rafael_Souza)')
    nome = nome.replace(' ','_')
    
    if os.path.exists(f'Dataset_Treinamento/') == False:
        os.mkdir(f'Dataset_Treinamento/')
        
    if os.path.exists(f'Dataset_Treinamento/{nome}') == True:
        if os.listdir(f'Dataset_Treinamento/{nome}') != []:
            print('Usuário já cadastrado!')
            exit()
    
    if os.path.exists(f'Dataset_Treinamento/{nome}') == False:
        os.mkdir(f'Dataset_Treinamento/{nome}')
    
    video = cv2.VideoCapture(0) 
   
    if (video.isOpened() == False):  
        print("Error reading video file") 
        
    frame_width = int(video.get(3)) 
    frame_height = int(video.get(4)) 
    size = (frame_width, frame_height) 

    result = cv2.VideoWriter(f'Dataset_Treinamento/{nome}/Video_{nome}.avi',  
                            cv2.VideoWriter_fourcc(*'MJPG'), 
                            10, size) 
    inicio = time.time()
    while(True): 
        
        ret, frame = video.read() 
    
        if ret == True:  
            result.write(frame) 
            cv2.imshow('Frame', frame) 
            if cv2.waitKey(1) & 0xFF == ord('q'): 
                    break
            fim = time.time() - inicio 
            if fim >= 7:
                break
        else: 
            break
    
    video.release() 
    result.release() 
    cv2.destroyAllWindows() 
    
    print("Video do usuário salvo") 