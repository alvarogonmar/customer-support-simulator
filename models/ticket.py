class Ticket:
    def __init__(self, id, description, priority, category):
        self.id = id
        self.description = description
        self.priority = priority
        self.category = category
        self.status = "Pending"
        self.assigned_agent = None