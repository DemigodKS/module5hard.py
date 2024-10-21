import time

class Video:
    def __init__(self, title, duration,  time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class UrTube:
    def __init__(self):
        self.users = {}
        self.videos = []
        self.current_user = None

    def register(self, nickname, password):
        if nickname not in self.users:
            self.users[nickname] = password
            #print(self.users)
        else:
            print(f'Пользователь {nickname} уже существует')

    def log_in (self, nickname, password):
        for key, value in self.users.items():
            if key == nickname and hash(value) == hash(password):
                self.current_user = key
                print(hash(value), hash(password))
                print('Вы ввели верные данные')
                return
        print("Неверный логин или пароль")

    def log_out(self, current_user):
        if current_user is not None:
            current_user_ = self.users.pop(current_user, None)
        print(f'{current_user} вышла/вышел из сети')

    def add(self, title, duration, adult_mode = False):
            self.videos.append(title)
            print(self.videos)

    def get_videos(self, word, title):
        for www in title:
            if www.lower() in word.lower():
                return True
        return False

    def watch_video(self, nickname, age, title, adult_mode = False):
        if nickname not in self.users:
            print(f'{nickname}, войдите в аккаунт, чтобы смотреть видео')
        else:
            print(f'Пользователь {nickname} в сети')
            if title not in self.videos:
                print('Такого видео нет в списке')

            if age < 18 and adult_mode == True:
                print(f'{nickname}, Вам нет 18 лет, пожалуйста покиньте страницу')
            else:
                if age >= 18 and adult_mode == False:
                    for second in range(1, 7):
                        time.sleep(1)
                        print(second, end=' ')
                    print('Конец видео')

class User:
    def __init__(self, nickname, age, password):
        self.nickname = nickname
        self.age = age
        self.password = password



if __name__ ==  '__main__':
    ur = UrTube()
    ur.register('Den', 3425)
    ur.register('Ksu', 'fgft569')
    # проверяем существует ли пользователь
    ur.register('Den', 3425)
    #проверяем вход в систему
    ur.log_in('Ksu', 'fgft569')
    ur.log_in('Rita', 'fgft569')
    #выходим из системы
    ur.log_out('Ksu')
    print(ur.users)

    ur.add('Для чего девушкам парень программист?', 200)
    ur.add('Лучший язык программирования 2024 года', 544, adult_mode=True)

    print(ur.get_videos('URBan', 'Urban the best'))
    print(ur.get_videos('луЧШий', 'Лучший язык программирования 2024 года'))

    #пользователь в сети, но видео нет в списке
    ur.watch_video('Den',17, 'Urban the best', adult_mode=True)
    print()
    ur.register('Rita', 'fgft5764')
    ur.watch_video('Rita', 17, 'Лучший язык программирования 2024 года', adult_mode=True)
    print()
    #проверяем в сети ли человек
    ur.watch_video('Ksu', 20,'Urban the best')

    ur.register('Ksu', 'fgft569')
    ur.watch_video('Ksu', 20, 'Лучший язык программирования 2024 года')

    print()
    print('Новый пользователь')
    ur.register('Nik', '9gdhs7')
    ur.watch_video('Nik', 19, 'Для чего девушкам парень программист?')
    print()
    ur.register('Vika', '9g987s7')
    ur.watch_video('Vika', 15, 'Для чего девушкам парень программист?', adult_mode=True)

    print()
    print(ur.users)
    for key in ur.users.keys():
        print(f'{key} - в режиме онлайн')
    print()

    ur.log_out('Ksu')
    ur.log_out('Nik')
    for key in ur.users.keys():
        if key not in ur.users.keys():
            print(f'{key}')









































