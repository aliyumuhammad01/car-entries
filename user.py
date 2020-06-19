class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.age =0
        self.gender = ''
        self.login_attempt = 0
    def set_attempt(self):
        self.login_attempt +=1
    def reset_attempt(self):
        self.login_attempt =0
    def describe_user(self):
        longname = self.first_name+ " "+ self.last_name
        return longname

    def greetuser(self):
        return "hello" + self.describe_user()

user =User("alice","brian")
user.set_attempt()
user.set_attempt()
user.set_attempt()

print(user.describe_user())
print(user.greetuser())
print("login attempt: "+str(user.login_attempt))
user.reset_attempt()
print("attempt rest to: "+str(user.login_attempt))

