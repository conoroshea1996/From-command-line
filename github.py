##### Github RepCreater ######
from github import Github
token = input('Enter your token key : \n >')

g = Github("{0}".format(token))

user_name = input('Enter your github username : \n >')
user = g.get_user('{0}'  .format(user_name))
print(user)

authed = g.get_user()
repo_name = input('Enter the name of your new repo: \n >')
repo = authed.create_repo('{0}'.format(repo_name))
print('New repo has been created')
