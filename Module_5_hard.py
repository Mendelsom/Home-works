import time


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

    def __init__(self, users=None, videos=None, current_user=None, nickname=None, password=None):
        self.users = users
        self.videos = videos
        self.current_user = None  # User(1, 1, 1)
        self.current_video = None  # Video(1, 1)
        self.nickname = nickname
        self.password = password
        self.need_to_register = False

    def __str__(self):
        return ur.current_user.nickname

    def log_in(self, nickname, password):

        for n in users:
            if nickname == n.nickname:
                self.current_user = n
                break

            self.need_to_register = False
            break

    def register(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age
        for n in users:
            if nickname == n.nickname:
                print('Такое имя уже существует')
                break

        self.current_user = User(self.nickname, self.password, self.age)
        users.append(self.current_user)
        ur.log_in(self.nickname, self.password)

    def log_out(self, current_user):
        self.current_user = None
        exit()

    def add(self, *video):

        for n in range(len(video)):
            if video[n] in videos:
                break
            videos.append(video[n])
            continue

    def get_videos(self, word=" "):
        word = word.lower()
        for n in videos:
            if word in n.title:
                print(n.title)

    def watch_video(self, title):
        flag_ = 0

        for n in videos:
            if title == n.title:
                flag_ = 1
                self.current_video = n
                break

        if flag_ == 1:

            if self.current_video.adult_mode:
                if self.current_user.age < 18:
                    print('Вам нет 18 лет')
                   
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
videos = []
users = []
v1 = Video('Лучший язык программирования 2024 года', 5)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
ur.add(v1, v2)
print(ur.get_videos('парень'))
print(ur.get_videos('ПРОГ'))

ur.register('vasya', '123321', 19)

ur.watch_video('Для чего девушкам парень программист?')
ur.register('danya', '11112', 6)

ur.watch_video('Лучший язык программирования 2024 года')
ur.register('lisa', '22222', 90)
ur.watch_video('Для чего девушкам парень программист?')
print(ur.current_user.nickname)
