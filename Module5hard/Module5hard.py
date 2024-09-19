from Users import Users, User
from Videos import Videos, Video
import time
from consoleTextStyle import ConsoleTextStyle as CoTeSt


class Urtube:
    def __init__(self):
        self.users = Users()
        self.videos = Videos()
        self.current_user: User = None

    def add(self, *args):
        if self.videos.add_videos(*args):
            print(f"{CoTeSt.Color.BLUE}Видео успешно добавлены{CoTeSt.Color.WHITE}")
            return
        else:
            print(f"{CoTeSt.Color.RED}Ошибка, добавьте только видео-файлы{CoTeSt.REGULAR}")

    def get_videos(self, title):
        found_videos_titles = self.videos.get_video(title)
        if found_videos_titles[0]:
            return found_videos_titles[1]
        else:
            print(f"{CoTeSt.Color.DARKCYAN}Видео не было найдено{CoTeSt.Color.WHITE}")

    def log_in(self, nickname: str,
               password: str):
        if nickname in self.users:
            if hash(password) == self.users.get_user(nickname)[1].password:
                self.current_user = self.users.get_user(nickname)[1]
                print(f"{CoTeSt.Color.BLUE}Пользователь {nickname} авторизован{CoTeSt.REGULAR}")
            else:
                print(f"{CoTeSt.Color.DARKCYAN}Логин или пароль не подходят{CoTeSt.REGULAR}")
        else:
            print(f"{CoTeSt.Color.DARKCYAN}Логин или пароль не подходят{CoTeSt.REGULAR}")

    def log_out(self):
        print(f"{CoTeSt.Color.BLUE}Пользователь {self.current_user.nickname} вышел из аккаунта{CoTeSt.REGULAR}")
        self.current_user = None

    def register(self, nickname: str,
                 password: str,
                 age: int):
        user = User(nickname, password, age)
        if self.users.add_user(user):
            self.log_in(nickname, password)
        else:
            print(f"{CoTeSt.Color.DARKCYAN}Пользователь {self.current_user.nickname} уже существует{CoTeSt.REGULAR}")

    def watch_video(self, title_video: str):
        if title_video in self.videos:
            video_index = self.videos.video_titles.index(title_video)
            founded_video = self.videos.videos[video_index]
            if founded_video.adult_mode:
                if self.current_user:
                    if self.current_user.age < 18:
                        print(f"{CoTeSt.Color.RED}Это видео недоступно лицам недостигшим 18 лет")
                        return
                else:
                    print("Зайдите в свой аккаунт")
                    return
            print(f"Воспроизводится видео \"{founded_video.title}\"")
            for second in range(1, founded_video.duration + 1):
                time.sleep(1)
                print(f"{CoTeSt.Color.PURPLE}{second}", end=" ")
            else:
                print(f"{CoTeSt.ITALIC}Конец видео{CoTeSt.REGULAR}")
        else:
            print("Данного видео не существует")


if __name__ == "__main__":
    tube = Urtube()
    video1 = Video("Хрень для теста", 10)
    video2 = Video("Фигня для теста - полная хрень", 2, adult_mode=True)

    tube.add(video1, video2)

    print(tube.get_videos("фигня"))
    print(tube.get_videos("хрень"))
    print(tube.get_videos("хорошее видео"))

    tube.register("Nogibator228", "123", 13)
    tube.register("Nogibator228", "123", 13)
    tube.watch_video("Фигня для теста - полная хрень")
    tube.register("chelovek", "321", 29)
    tube.watch_video("Фигня для теста - полная хрень")

    tube.log_out()
    tube.log_in("Nogibator228", "1234")
    tube.log_in("Nogibator228", "123")

