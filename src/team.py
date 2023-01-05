class Team(object):
    def __init__(self, name, permissions, memberEmails):
        self.name = name
        self.permissions = permissions
        self.memberEmails = memberEmails
    def __str__(self) -> str:
        teamStr = f'{self.name}, {self.permissions}, {self.memberEmails}'
        return teamStr

    name = "teamFoo"
    permissions = {}
    memberEmails = []


