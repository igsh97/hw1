import hashlib
import re
class Member():

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        encoded_password=password.encode()
        hexdigest=hashlib.sha256(encoded_password).hexdigest()
        self.password=hexdigest

    def display(self):
        print(f"회원 이름:{self.name}\n아이디:{self.username}")


class Post():
    def __init__(self, title, content,author):
        self.title = title
        self.content = content
        self.author = author


members = []
while True:
    name = input("회원 이름: ")
    username = input("아이디: ")
    password = input("비밀번호: ")
    member = Member(name=name, username=username, password=password)
    members.append(member)
    want_quit = input("입력 중지를 원하시면 'q'를 입력하세요(계속 입력할 경우 아무키나 입력하세요)")
    if want_quit == 'q':
        break
posts = []
for member in members:
    member.display()
    while True:
        title = input("제목: ")
        content = input("내용: ")
        post = Post(title=title, content=content, author=member.username)
        posts.append(post)
        want_quit = input("입력 중지를 원하시면 'q'를 입력하세요(계속 입력할 경우 아무키나 입력하세요)")
        if want_quit == 'q':
            break

target_name = input("어떤 회원의 게시글을 보고 싶으신가요? : ")
for post in posts:
    if target_name == post.author:
        print(f"제목:{post.title}")

target_word = input("어떤 단어가 있는 게시글을 보고 싶으신가요? : ")
target_regex=re.compile(rf"([\s\S])*{target_word}([\s\S])*")
for post in posts:
    if target_regex.match(post.content):
        print(f"글쓴이: {post.author}\n제목:{post.title}")