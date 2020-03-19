class Task:

    def __init__(self, title, details):
        self.title = title
        self.details = details
        self.is_done = False

    def __str__(self):
        return '{}\n{}\nis done: {}'.format(self.title, self.details, self.is_done)

    def set_is_done(self, is_done):
        self.is_done = is_done