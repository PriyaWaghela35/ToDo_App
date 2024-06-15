from graphene import ObjectType, String, Boolean
class User(ObjectType):
    id = String()
    Task = String()
    completed = Boolean()
    
