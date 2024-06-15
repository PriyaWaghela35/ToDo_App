import graphene

class User(graphene.ObjectType):
    id = graphene.ID()
    username = graphene.String()

class Query(graphene.ObjectType):
    user = graphene.Field(User, id=graphene.ID(required=True))

    def resolve_user(self, info, id):
        # For demonstration, return a static user object
        if id == "1":
            return User(id="1", username="john_doe")
        return None

schema = graphene.Schema(query=Query)
