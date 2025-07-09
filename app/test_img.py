import cv2
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# Caminho da imagem gxf4x m888e w76f7
caminho = r"E:\001-DOC\git-projects\llm-analyzer\imgs\w76f7.png"
img=Image.open(caminho)
texto = pytesseract.image_to_string(img, config='--psm 7 -c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
print("Texto extraído pad:", texto)


# Carrega imagem em escala de cinza
img = cv2.imread(caminho, cv2.IMREAD_GRAYSCALE)
texto = pytesseract.image_to_string(img, config='--psm 7 -c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
print("Texto extraído cinza:", texto)

# Aplica binarização adaptativa (dá melhor contraste que apenas .convert('L'))
img = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2
)
texto = pytesseract.image_to_string(img, config='--psm 7 -c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')

print("Texto extraído binarização:", texto)

# Remove ruído com filtro morfológico (opcional)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# Salva imagem tratada (para debug opcional)
cv2.imwrite("tratada.png", img)

# OCR
custom_config = r'--psm 7 -c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
texto = pytesseract.image_to_string(img, config='--psm 7')

print("Texto extraído:", texto)