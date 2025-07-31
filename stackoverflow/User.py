import uuid


class User:
    id = None
    name = None
    reputation = None
    email = None

    def __init__(self, name, email):
        self.id = uuid.uuid4()
        self.name = name
        self.email = email
        self.reputation = {"question": [[],0], "answer":[[],0], "comment":[[],0], "votes_up":0, "votes_down":0}

    def add_reputation(self, rep, reference_id):
        if rep == "question":
            self.reputation[rep][1]+=5
        if rep == "answer":
            self.reputation[rep][1]+=15
        if rep == "comment":
            self.reputation[rep][1]+=2
        if rep == "votes_up":
            self.reputation[rep]+=1
            return True
        if rep == "votes_down":
            self.reputation[rep]-=1
            return True
        self.reputation[rep][0].append(reference_id)
        return True

    def reduce_reputation(self, rep, reference_id):
        if rep == "question":
            self.reputation[rep][1]-=5
        if rep == "answer":
            self.reputation[rep][1]-=15
        if rep == "comment":
            self.reputation[rep][1]-=2
        self.reputation[rep][0].remove(reference_id)
        return True

