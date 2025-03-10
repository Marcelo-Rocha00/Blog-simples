# blog/utils.py
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

def resize_image(image, max_width=400, max_height=400):
    """
    Redimensiona a imagem mantendo a proporção, ajustando para a largura e altura máximas.
    """
    img = Image.open(image)
    
     # Converte para RGB se a imagem for RGBA (transparente)
    if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
        img = img.convert('RGB')
    
    # Redimensiona a imagem mantendo a proporção
    img.thumbnail((max_width, max_height))
    
    # Salva a imagem redimensionada em um objeto InMemoryUploadedFile
    image_io = BytesIO()
    img.save(image_io, format='JPEG')
    image_io.seek(0)
    
    # Cria um novo arquivo a partir do arquivo redimensionado
    new_image = InMemoryUploadedFile(image_io, None, image.name, 'image/jpeg', image_io.tell(), None)
    
    return new_image
