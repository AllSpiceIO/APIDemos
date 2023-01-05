class Team(object):
    # units_map is the read/write permissions
    def __init__(self, name, description, readWrite, canCreateOrgRepo, includesAllRepos, units_map, memberEmails):
        self.name = name
        self.units_map = units_map
        self.memberEmails = memberEmails
        self.description = description
        self.readWrite = readWrite
        self.canCreateOrgRepo = canCreateOrgRepo
        self.includesAllRepos = includesAllRepos
    def __str__(self) -> str:
        teamStr = f'{self.name}, {self.units_map}, {self.memberEmails}'
        return teamStr

    name = "teamName"
    description = "teamDesc"
    units_map = {}
    memberEmails = []
    readWrite = "foo"
    canCreateOrgRepo = False
    includesAllRepos = False

