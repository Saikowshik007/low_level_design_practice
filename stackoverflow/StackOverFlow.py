from threading import RLock, Lock

from stackoverflow.Answer import Answer
from stackoverflow.Comment import Comment
from stackoverflow.Question import Question
from stackoverflow.User import User


class StackOverFlow:
    instance = None
    lock = None
    questions = None
    users = None
    answers = None
    comments = None
    def __init__(self):
        self.lock = RLock()
        self.questions = dict()
        self.users = dict()
        self.answers = dict()
        self.comments = dict()
    @staticmethod
    def get_instance():
        if StackOverFlow.instance is None:
            StackOverFlow.instance = StackOverFlow()
        return StackOverFlow.instance

    def add_question(self, content, tags, user_id):
        with self.lock:
            question = Question(content, tags, user_id)
            self.questions[question.id] = question
            self.users[user_id].add_reputation("question", question.id)
        return question.id
    def add_answer(self, content, user_id, question_id):
        with self.lock:
            question = self.questions[question_id]
            user = self.users[user_id]
            answer = Answer(content, user_id, question_id)
            self.answers[answer.id] = answer
            question.add_answer(answer.id)
            user.add_reputation("answer",answer.id)
        return answer.id

    def add_user(self, name,email):
        for user_id,user in self.users.items():
            if self.users[user_id].email is email:
                raise ValueError(f"User with email id:{email} already exists!!")
        user = User(name,email)
        self.users[user.id] = user
        return user

    def add_comment_to_question(self,question_id, content, user_id):
        with self.lock:
            if question_id is None or user_id is None:
                raise ValueError("Question id or user id cannot be null!!")
            question = self.questions.get(question_id)
            comment = Comment(content,user_id,question.id)
            self.comments[comment.id] = comment
            question.add_comment(comment.id)
            self.users[user_id].add_reputation("comment",comment.id)
        return True
    def vote_question(self, question_id, sign):
        with self.lock:
            question = self.questions[question_id]
            user = self.users[question.posted_user]
            if sign >0:
                question.vote("up")
                user.add_reputation("vote_up")
            else:
                question.vote("down")
                user.add_reputation("vote_down")
    def vote_answer(self, answer_id, sign):
        with self.lock:
            answer = self.answers[answer_id]
            user = self.users[answer.posted_user]
            if sign >0:
                answer.vote("up")
                user.add_reputation("vote_up")
            else:
                user.add_reputation("vote_down")
                answer.vote("down")

    def add_comment_to_answer(self,answer_id, content, user_id):
        with self.lock:
            if answer_id is None or user_id is None:
                raise ValueError("Question id or user id cannot be null!!")
            answer = self.answers.get(answer_id)
            comment = Comment(content,user_id,answer.id)
            self.comments[comment.id] = comment
            answer.add_comment(comment.id)
            self.users[user_id].add_reputation("comment", comment.id)
        return True

    def search(self, filter):
        result = []

        # Tag search
        if filter.startswith("@"):
            for question in self.questions.values():
                for tag in question.tags:
                    if tag.value in filter:
                        result.append(question)
        elif ".com" in filter:
            for user_id, user in self.users.items():
                if user.email == filter:
                    for question in self.questions.values():
                        if question.posted_user == user_id:
                            result.append(question)

        # Keyword search
        else:
            for question in self.questions.values():
                if filter.lower() in question.content.lower():
                    result.append(question)

        return result




