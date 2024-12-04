import time

users = []
videos = []


class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


class Video:

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:

    def __init__(self, current_user=None):
        self.users = []
        self.videos = []
        self.current_user = current_user

    def log_in(self, nickname, password):

        for n in users:
            if self.nickname == n.nickname and self.password == n.password:
                self.current_user = n
                break

    def register(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age
        exist_ = 0

        for n in self.users:

            if self.nickname != n.nickname:
                continue
            else:
                exist_ = 1
                print('Такое имя уже существует')
                break
        if exist_ == 0:
            self.current_user = User(self.nickname, self.password, self.age)
            self.users.append(self.current_user)
            ur.log_in(self.nickname, self.password)

    def log_out(self, current_user):
        self.current_user = None
        exit()

    def add(self, *video):

        for n in range(len(video)):
            if video[n] in self.videos:
                break
            self.videos.append(video[n])
            continue

    def get_videos(self, word):

        self.word = word.lower()

        for n in self.videos:
            if not self.word in n.title.lower():
                continue
            else:
                print(n.title)
                break

                break

    def watch_video(self, title):
        flag_ = 0
        self.title = title

        for n in self.videos:
            if self.title == n.title:
                flag_ = 1
                self.current_video = n
                break

        if flag_ == 1:

            if self.current_video.adult_mode:
                if self.current_user.age < 18:
                    print('Вам нет 18 лет')
                    # self.log_out(self.current_user)
                else:
                    n = 0
                    while n < self.current_video.duration:
                        n += 1
                        print(f'{n}  ', end='')
                        time.sleep(1)
                    print('Конец видео')
            else:
                n = 0
                while n < self.current_video.duration:
                    n += 1
                    print(f'{n}  ', end='')
                    time.sleep(1)
                print('Конец видео')

        else:
            print("Нет такого видео")


ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)

v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео

ur.add(v1, v2)

# Проверка поиска

print(ur.get_videos('лучший'))
#
print(ur.get_videos('ДЕВ'))
#
#

# Проверка на вход пользователя и возрастное ограничение


ur.register('vasya_pupkin', 'lolkekcheburek', 13)

ur.watch_video('Для чего девушкам парень программист?')

ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)

ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)

# Попытка воспроизведения несуществующего видео

ur.watch_video('Лучший язык программирования 2024 года!')
