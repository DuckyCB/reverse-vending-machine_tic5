import cv2
from pyzbar import pyzbar
from datetime import datetime

def read_barcodes(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y , w, h = barcode.rect
        barcode_info = barcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)
        time_now = datetime.now()
        current_time = time_now.strftime("%d_%m_%Y-%H_%M_%S")
        cv2.imwrite(f"output/{current_time}.jpg", frame)
        with open(f"output/{current_time}.txt", mode ='w') as file:
            file.write(barcode_info + ' ' + time_now.strftime("%d/%m/%Y %H:%M:%S"))
    return frame

def main():
    camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    
    camera.set(cv2.CAP_PROP_FPS, 30.0)
    camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('m','j','p','g'))
    camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('M','J','P','G'))
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    ret, frame = camera.read()
    while ret:
        ret, frame = camera.read()
        frame = read_barcodes(frame)
        cv2.imshow('Barcode/QR code reader', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    camera.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
