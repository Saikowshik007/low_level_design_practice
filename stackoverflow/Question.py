import uuid
from threading import Lock


class Question:
    id = None
    content = None
    tags = None
    posted_user = None
    answers = None
    comments = None
    lock = None
    votes = None

    def __init__(self, content, tags, posted_user):
        self.id = uuid.uuid1()
        self.content = content
        self.tags = tags
        self.posted_user = posted_user
        self.answers = set()
        self.comments = set()
        self.lock = Lock()
        self.votes = 0

    def add_answer(self,answer_id):
        with self.lock:
            self.answers.add(answer_id)
        return True
    def add_comment(self, comment_id):
        with self.lock:
            self.comments.add(comment_id)
        return True

    def vote(self,sign):
        with self.lock:
            if sign == "up":
                self.votes+=1
            elif sign == "down":
                self.votes-=1
            else:
                raise ValueError("Invalid operation")