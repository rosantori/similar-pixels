import cv2
import numpy as np 

def mouse_click(event, x, y, flags, params):
    global img, init, real_x, real_y, b, g, r
    if event == cv2.EVENT_LBUTTONDOWN:
        init = True
        real_x = x
        real_y = y 
        print('\n\nPixel selecionado em x,y = (', x,',', y,').')
        if opt == '1' or opt == '3' or opt == '5':
            b = img[y,x,0]
            g = img[y,x,1]
            r = img[y,x,2]
            print("Valores RGB:\nR = ", r,"G = ", g, "B = ", b)
            matrix = np.square(np.subtract(img.astype('int32'), np.array([b, g, r])))
            matrix = np.sqrt(np.sum(matrix, axis = 2))
            img2 = np.copy(img)
            img2[matrix<13] = np.array([0, 0, 255])
            cv2.imshow(':)',img2)

        elif opt == '2' or opt == '4' or opt == '6' :
            print('Valor em GRAYSCALE:\nG = ',img[y,x],'.\n')
            g = img[y,x]
            matrix = np.abs(np.subtract(img.astype('int32'), g))
            img2 = np.reshape(img,(img.shape[0], img.shape[1], 1))
            img2 = np.repeat(img2, 3, axis = 2)
            img2[matrix<13] = np.array([0, 0, 255])
            cv2.imshow(':)',img2)

def image(img) :
    print('Aperte \'Esc\' para sair.\n')
    cv2.imshow('Matrix', img)
    cv2.setMouseCallback('Matrix', mouse_click)

    while cv2.waitKey(1) != 27:
        pass
    cv2.destroyAllWindows()

def video():
    global img, init, real_x, real_y, b, g, r, cap
    print('Aperte \'Esc\' para sair.\n')
    while(cap.isOpened()) :
        ret,img = cap.read()
        if (opt == '4' or opt == '6') and img is not None:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        if img is not None:   
            cv2.imshow('Matrix', img)
        cv2.setMouseCallback('Matrix', mouse_click)
        k = cv2.waitKey(25)
        if k == 27:
            break

        if init and img is not None:
            if opt == '1' or opt == '3' or opt == '5':
                matrix = np.square(np.subtract(img.astype('int32'), np.array([b, g, r])))
                matrix = np.sqrt(np.sum(matrix, axis = 2))
                img2 = np.copy(img)
                img2[matrix<13] = np.array([0, 0, 255])
                cv2.imshow(':)',img2)

            elif opt == '2' or opt == '4' or opt == '6' :
                matrix = np.abs(np.subtract(img.astype('int32'), g))
                img2 = np.reshape(img,(img.shape[0], img.shape[1], 1))
                img2 = np.repeat(img2, 3, axis = 2)
                img2[matrix<13] = np.array([0, 0, 255])
                cv2.imshow(':)',img2)
        elif img is None:
            cap = cv2.VideoCapture('../data/video.avi')

    cap.release()
    cv2.destroyAllWindows()

while(True):
    opt = input('Requisitos 1 e 2\n\t\
1 - Imagem Colorida\n\t2 - Imagem Cinza\nRequisito 3\n\t3 - Vídeo Colorido\n\t4 - Vídeo Cinza\n\
Requisito 4\n\t5 - Câmera Colorida\n\t6 - Câmera Cinza\n\n\t7 - Sair\n\n')
    init = False
    if opt == '1':
        img = cv2.imread('../data/image.jpg',cv2.IMREAD_COLOR)
        if img is not None: 
            image(img)
    elif opt == '2':
        img = cv2.imread('../data/image.jpg',cv2.IMREAD_GRAYSCALE)
        if img is not None: 
            image(img)
    elif opt == '3':
        cap = cv2.VideoCapture('../data/video.avi')
        video()
    elif opt == '4':
        cap = cv2.VideoCapture('../data/video.avi')

        video()
    elif opt == '5':
        cap = cv2.VideoCapture(0)
        video()
    elif opt == '6':
        cap = cv2.VideoCapture(0)
        video()
    elif opt == '7':
        break
    else : 
        print('Escolha uma opção válida.\n')