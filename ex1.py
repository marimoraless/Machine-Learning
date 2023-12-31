import cv2

def imprimir_info(img):
    altura, largura, canais = img.shape
    tipo_de_dado = img.dtype
    tom_de_cinza_max = 255 if tipo_de_dado == "uint8" else 65535
    tom_de_cinza_medio = int(0.5 * tom_de_cinza_max)
    tom_de_cinza_min = 0

    print("Informações da imagem:")
    print(f"- Altura: {altura}")
    print(f"- Largura: {largura}")
    print(f"- Canais de cor: {canais}")
    print(f"- Tipo de dado: {tipo_de_dado}")
    print(f"- Tom de cinza máximo: {tom_de_cinza_max}")
    print(f"- Tom de cinza médio: {tom_de_cinza_medio}")
    print(f"- Tom de cinza mínimo: {tom_de_cinza_min}")

caminho_da_imagem = ('./imagens/mll.imagem.jpg')

img = cv2.imread(caminho_da_imagem)
imprimir_info(img)