from django.contrib.auth.backends import UserModel


def run(*args):
    if not UserModel.objects.filter(email='test@test.com').exists():
        print("Run User seeds")
        user = UserModel.objects.create_user(email='test@test.com', username='test', password='test123')
        print("Users Created")
