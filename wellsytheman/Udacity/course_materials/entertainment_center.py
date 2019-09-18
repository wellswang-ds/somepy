import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that comes to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://www.upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Tease-Post",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.storyline)
#avatar.show_trailer()


HTTYD = media.Movie("How to Train Your Dragon",
                    "a boy and his dragon",
                    "https://upload.wikimedia.org/wikipedia/zh/thumb/5/54/Traindragon.jpg/250px-Traindragon.jpg",
                    "https://www.youtube.com/watch?v=oKiYuIsPxYk")
HTTYD.show_trailer()
