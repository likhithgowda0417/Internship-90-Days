class InstagramReel:
    def __init__(self, title, description, creator, location):
        self.title = title
        self.description = description
        self.creator = creator
        self.location = location
        self.likes = 0
        self.comments = []

    def like(self):
        self.likes += 1

    def dislike(self):
        if self.likes > 0:
            self.likes -= 1

    def add_comment(self, comment):
        self.comments.append(comment)

    def delete_last_comment(self):
        if self.comments:
            removed = self.comments.pop()
            print("deleted comment:", removed)
        else:
            print("no comments to delete")

    def display_details(self):
        print("title:", self.title)
        print("description:", self.description)
        print("creator:", self.creator)
        print("location:", self.location)
        print("likes:", self.likes)
        print("comments:", self.comments)


# object usage
reel1 = InstagramReel("food reel", "street food", "rahul", "bangalore")

reel1.like()
reel1.add_comment("nice video")
reel1.add_comment("looks tasty")
reel1.delete_last_comment()

reel1.display_details()
