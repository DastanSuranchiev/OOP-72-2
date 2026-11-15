import time

def is_admin(func):
    def wrapper(self):
        if self.role == "admin":
            return func(self)
        else:
            return "У вас нет доступа"

    return wrapper

def timer(func):
    def wrapper(self):
        return func(self)
    return wrapper

class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    @is_admin
    def delete_video(self):
        return "Видео удалено"

    @timer
    def download_video(self):
        time.sleep(2)
        return ("Видео загружено \n"
                "Время выполнения: 2.0 секунд")






dastan = User("dastan", 'admin')
print(dastan.delete_video())
print(dastan.download_video())

