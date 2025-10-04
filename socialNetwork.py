class User():

  def __init__(self, name, last_name, username, password):
    self.last_name = last_name
    self.username = f'@{username.lower()}'
    self.password = password
    self.name = name
    self.posts = []
    self.status = False
    self.followers = []
    self.following = []

  def __str__(self):
    return f'{self.username}'

  def publicar(self, message):
    post = Publicaciones(self, message)
    self.posts.append(post)

  def comentar(self, post, comment):
    if self.status != True:
      print('Accion no disponible. Por favor inicie sesión.')
    else:
      comment = Comentario(post, comment, self.username)

  def mostrar_publicaciones(self):
    if self.status != True:
      print('Accion no disponible. Por favor inicie sesión.')
    else:
      for i in self.posts:
        print(i)
        for j in i.comments:
          print(f'{j}')
        print('\n')

  def seguir(self, user):
    if self.status != True:
      print('Accion no disponible. Por favor inicie sesión.')
    else:
      self.following.append(user.username)
      user.followers.append(self.username)

  def mostrar_amigos(self):
      if self.status != True:
        print('Accion no disponible. Por favor inicie sesión.')
      else:
        print(f'<{self.username}>\n')
        print('Followers:')
        if self.followers == []:
          print('Sin seguidores.')
        else:
          for i in self.followers:
            print(f'\n{i}')
        print('\nFollowing:')
        if self.following == []:
          print('\nNo sigue a nadie.')
        else:
          for i in self.following:
            print(f'\n{i}')

  def loggedOut():
    print('Accion no disponible. Por favor inicie sesión.')

  def login(self, username, password):
    if f'@{username.lower()}' == self.username and password == self.password:
      self.status = True
    else:
      print('Datos Incorrectos. Intente de nuevo.')

  def logout(self):
    self.status = False

class Publicaciones():

  def __init__(self, user, message):
    self.user = user
    self.message = message
    self.comments = []

  def __str__(self):
    return f'{self.user}: {self.message}'

class Comentario():

  def __init__(self, post, comment, username):
    self.comment = comment
    self.user = username
    post.comments.append(f'\n\t>{username}: {self.comment}')

  def __str__(self):
    f'\n    >{self.user}: {self.comment}'

user1 = User('Arturo', 'Alvarez', 'vrboii', '1234')
user2 = User('Bryan', 'Alvarez', 'Kuro', '4321')
user1.login('vrboii', '1234')
user1.seguir(user2)
user1.publicar('post 1')
user2.comentar(user1.posts[0], 'post 1. comentario 1') #comentario sin hacer login

user2.login('kuro', '4321')
user2.comentar(user1.posts[0], 'post 1. comentario 1')
user1.mostrar_publicaciones()
#user1.mostrar_amigos()
user2.mostrar_amigos()
