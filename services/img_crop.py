from PIL import Image, ImageOps


def crop_img_center(filename:str,width:int = 300, height:int = 300) -> str:
    """
    Функция для обрезки изображения по центру.
    Принимает имя файла и размер стороны: width, height
    Сохраняет новое изображение в формате с приставкой '_thumbnail'
    Возвращает 'ок' или сообщение об ошибке
    """
    # Создаем новое имя
    filename_list = filename.split('.')
    filename_list[-2] = filename_list[-2]+'_thumbnail'
    new_filename = '.'.join(filename_list)

    # Открываем изображение и обрезаем
    pil_img = Image.open(filename)
    new_img =  ImageOps.fit(pil_img, (width,height), method=Image.LANCZOS)

    try:
        new_img.save(new_filename, quality=95)
    except Exception as e:
        return e
    return 'ok'

#im_new = crop_img_center('2.png', 300, 300)

