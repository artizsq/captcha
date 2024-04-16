from captcha.image import ImageCaptcha
from captcha.audio import AudioCaptcha
import string
import random
import os


def generate_image(text: str = None, path: str = None, format: str = 'png', image = ImageCaptcha()) -> ImageCaptcha:
    """
    Генерация изображения с капчей (4 символа).

    :param text:  текст капчи
    :param path: путь сохранения изображения
    :param format: формат изображения
    """

    if text is None:
        text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    if path is None:
        path = f'{text}.{format}'

    return image.write(text, path, format)

    

def generate_captcha() -> str:
    """
    Генерация текста капчи (4 символа).
    """
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))

    


def check_captcha(captcha: str, text: str) -> bool:
    """
    Проверка капчи.
    """
    return captcha == text


