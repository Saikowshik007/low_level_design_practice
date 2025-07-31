import uuid
from threading import Lock


class Answer:
    id = None
    content = None
    posted_user = None
    comments = None
    question_id = None
    lock = None
    votes = None

    def __init__(self, content, posted_user, question_id):
        self.id = uuid.uuid1()
        self.content = content
        self.posted_user = posted_user
        self.comments = set()
        self.question_id = question_id
        self.lock = Lock()
        self.votes = 0

    def add_comment(self, comment_id):
        with self.lock:
            self.comments.add(comment_id)
        return True

    def remove_comment(self, comment_id):
        with self.lock:
            if comment_id not in self.comments:
                raise ValueError(f"No comment found with the provided id: {comment_id}")
            self.comments.remove(comment_id)
        return True
    def vote(self,sign):
        with self.lock:
            if sign == "up":
                self.votes+=1
            elif sign == "down":
                self.votes-=1
            else:
                raise ValueError("Invalid operation")
