from captcha.image import ImageCaptcha
from captcha.audio import AudioCaptcha
import string
import random
import os


def generate_image(text: str | None = None, path: str | None = None, format: str = 'png') -> ImageCaptcha:
    """
    Генерация изображения с капчей (4 символа).

    :param text:  текст капчи
    :param path: путь сохранения изображения
    :param format: формат изображения
    """
    image = ImageCaptcha()

    if not text:
        text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    if not path:
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

