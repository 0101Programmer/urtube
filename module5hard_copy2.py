import time


class User:
    def __str__(self):
        return f'Логин: {self.nickname}, пароль: {self.password}, возраст: {self.age}'

    def __eq__(self, other):
        return self.nickname == other.nickname

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        password_h = hash(password)
        self.age = int(age)


class Video:
    def __str__(self):
        return f'Название: "{self.title}", продолжительность: {self.duration} сек, секунда остановки: {self.time_now}, подходит для детей: {self.ad_mode}'

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = str(title)
        self.duration = int(duration)
        self.time_now = int(time_now)
        self.adult_mode = bool(adult_mode)
        if not self.adult_mode:
            self.ad_mode = 'нет'
        else:
            self.ad_mode = 'да'


class UrTube:
    from time import sleep

    def __init__(self, users=None, videos=None, current_user=User):
        self.users = users
        if self.users is None:
            self.users = []
        self.videos = videos
        if self.videos is None:
            self.videos = []
        self.current_user = current_user

    def log_in(self, nickname, password):
        for i in self.users:
            if nickname == i.nickname and password == i.password:
                self.current_user = nickname
                print(f'Вход успешно выполнен, привет, {nickname}')
            # else:
            #     print(f'Такого пользователя не существует')

    def register(self, nickname, password, age):
        new_ur = User(nickname, password, age)
        if new_ur not in self.users:
            self.users.append(new_ur)
            self.current_user = nickname
            print(f'Пользователь {nickname} успешно зарегистрирован')
        else:
            print(f'Пользователь {nickname} уже существует')

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for i in args:
            self.videos.append(i)

    def get_videos(self, search_word):
        get_videos_list = []
        for i in self.videos:
            if search_word.lower() in i.title.lower():
                get_videos_list.append(i.title)
        print(get_videos_list)

    def watch_video(self, key_word):
        if self.current_user is not None:
            for i in self.videos:
                if key_word in i.title:
                    print(f'Воспроизводится: "{i.title}", текущая секунда просмотра:')
                    for j in range(i.duration):
                        print(f'\r{j:3}', end='')
                        time.sleep(0.05)
                    print(f'\nКонец видео')
                    i.time_now = 0
                    break
                elif key_word not in i.title:
                    print(f'Видео по запросу: "{key_word}" не найдено')
                    break
        elif self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')


ur = UrTube()

# работает:
ur.register('Poppy', 'qwerty123', 11)
ur.register('Poppy', '231', 11)
ur.register('Molly', 'wrqo', 18)
ur.register('Brown', 14930, 24)
ur.register('Chuck', 11001, 8)
ur.log_out()
print(ur.current_user)
ur.log_in('Smith', 987654321)
ur.log_in('Brown', 14930)
print(ur.current_user)
ur.log_in('Molly', 'wrqo')
ur.log_out()
print(ur.current_user)
# v1 = Video('Белый конь', 111)
# v2 = Video('Пушистые бЕлки', 59)
# v3 = Video('Полосатый в БЕЛую полоску', 59)
# v4 = Video('Snow', 59)
#
# ur.add(v1, v2, v3, v4)
# # ur.get_videos('бел')
# ur.watch_video('Белый конь')
