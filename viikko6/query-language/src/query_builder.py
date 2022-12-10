from matchers import And, PlaysIn, HasAtLeast, All, Not, HasFewerThan, Or

class QueryBuilder:
    def __init__(self, queries = All()):
        self.queries = queries
    
    def playsIn(self, team):
        return QueryBuilder(And(self.queries, PlaysIn(team)))
    
    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self.queries, HasAtLeast(value, attr)))
    
    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self.queries, HasFewerThan(value, attr)))
    
    def oneOf(self, query1, query2):
        return QueryBuilder(Or(query1, query2))

    def build(self):
        return self.queries