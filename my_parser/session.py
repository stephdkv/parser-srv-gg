import pickle
import os

def read_session_file(filepath):
    try:
        # Загружаем данные из файла session.pkl
        with open(filepath, 'rb') as file:
            cookies = pickle.load(file)
        
        # Проверяем содержимое
        if isinstance(cookies, list) and all(isinstance(cookie, dict) for cookie in cookies):
            print("Файл session.pkl содержит правильные данные.")
            for cookie in cookies:
                cookie['secure'] = True
            print(cookies)
                                 
        else:
            print("Файл session.pkl содержит некорректные данные.")
        
        return cookies
    except (pickle.UnpicklingError, EOFError, AttributeError, ImportError, IndexError) as e:
        print(f"Ошибка при загрузке файла session.pkl: {e}")
        return None
    except FileNotFoundError:
        print(f"Файл {filepath} не найден.")
        return None

filepath = 'C:\project\parser-srv-gg\my_parser\session'
cookies = read_session_file(filepath)
{'name': '_ym_uid', 'value': '171860339420615418', 'path': '/', 'domain': '.srv-gg.ru', 'secure': False, 'httpOnly': False, 'expiry': 1750139393, 'sameSite': 'None'}
{'name': '_ym_d', 'value': '1718603394', 'path': '/', 'domain': '.srv-gg.ru', 'secure': False, 'httpOnly': False, 'expiry': 1750139393, 'sameSite': 'None'}
{'name': '_ym_isad', 'value': '2', 'path': '/', 'domain': '.srv-gg.ru', 'secure': False, 'httpOnly': False, 'expiry': 1718675394, 'sameSite': 'None'}
{'name': '_ym_visorc', 'value': 'w', 'path': '/', 'domain': '.srv-gg.ru', 'secure': False, 'httpOnly': False, 'expiry': 1718605194, 'sameSite': 'None'}