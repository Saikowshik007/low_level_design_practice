import uuid


class Comment:
    id = None
    content = None
    posted_user = None
    reference_id = None

    def __init__(self, content, posted_user, reference_id):
        self.id = uuid.uuid1()
        self.content = content
        self.posted_user = posted_user
        self.reference_id = reference_id