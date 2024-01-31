


# Sample data
users = {}
posts = {}
followers = {}

# Models
class User(BaseModel):
    username: str
    password: str

class Post(BaseModel):
    content: str
    author: str
