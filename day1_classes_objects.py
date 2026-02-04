class InstagramReel:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.likes = 0

    def display_title(self):
        print("title:", self.title)

    def display_description(self):
        print("description:", self.description)

    def like(self):
        self.likes += 1

    def dislike(self):
        if self.likes > 0:
            self.likes -= 1

    def display_likes(self):
        print("likes:", self.likes)


# object creation
reel1 = InstagramReel("travel vlog", "trip to goa")
reel2 = InstagramReel("gym reel", "leg day workout")

reel1.like()
reel1.like()
reel2.like()

reel1.display_likes()
reel2.display_likes()

print("reel1 memory:", id(reel1))
print("reel2 memory:", id(reel2))
