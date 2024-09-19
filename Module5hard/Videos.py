class Video:
    def __init__(self, title: str,
                 duration: int,
                 adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def get_title(self):
        return self.title


class Videos:
    def __init__(self):
        self.videos: list[Video] = []
        self.video_titles: list[str] = []

    def __contains__(self, item) -> bool:
        return item in self.video_titles

    def add_videos(self, *args):
        if all(tuple(map(lambda x: isinstance(x, Video), args))):
            self.videos.extend(args)
            self.video_titles.extend(tuple(map(Video.get_title, args)))
            return True
        else:
            return False

    def get_video(self, video_title: str):
        video_title = video_title.lower()
        _video_titles = list(map(str.lower, self.video_titles))
        is_contain_title: list = list(map(lambda x: video_title in x, _video_titles))
        if any(is_contain_title):
            founded_videos_titles = []
            for video_index in range(len(self.videos)):
                if is_contain_title[video_index]:
                    founded_videos_titles.append(self.video_titles[video_index])
            return True, founded_videos_titles
        else:
            return False, None


if __name__ == "__main__":
    video = Video("Хрень про чёрные дыры", 666)
    videos = Videos()
    videos.add_videos(video, video)
    print(videos.get_video("хрень")[1])
