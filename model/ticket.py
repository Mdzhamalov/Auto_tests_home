

class Ticket:
    def __repr__(self):
        return "%s:%s" % (self.topic, self.message)