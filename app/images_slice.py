import cv2
import numpy as np

def trocear_imagen(img, tile_h, tile_w):
    h, w = img.shape[:2]
    tiles = []
    
    for y in range(0, h, tile_h):
        for x in range(0, w, tile_w):
            tile = img[y:y+tile_h, x:x+tile_w]
            tiles.append((y, x, tile))
    
    return tiles


def reconstruir_imagen(tiles, shape):
    h, w = shape[:2]
    result = np.zeros(shape, dtype=np.uint8)

    for y, x, tile in tiles:
        result[y:y+tile.shape[0], x:x+tile.shape[1]] = tile

    return result


# ------------------- USO -------------------

img = cv2.imread("imagen_grande.jpg")

tile_h, tile_w = 512, 512

tiles = trocear_imagen(img, tile_h, tile_w)

# Aquí aplicarías tus filtros
tiles_procesados = []
for y, x, tile in tiles:
    # ejemplo: pasar a gris (solo para demo)
    procesado = cv2.cvtColor(tile, cv2.COLOR_BGR2GRAY)
    procesado = cv2.cvtColor(procesado, cv2.COLOR_GRAY2BGR)
    
    tiles_procesados.append((y, x, procesado))


img_final = reconstruir_imagen(tiles_procesados, img.shape)

cv2.imwrite("resultado.jpg", img_final)