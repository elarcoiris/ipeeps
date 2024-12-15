from instaloader import Instaloader, Profile
from sys import argv

# Instaloader instantiation - you may pass additional arguments to the constructor here
L = Instaloader()

try:
    PROFILE = argv[1]
except IndexError:
    raise SystemExit("Pass profile name as argument!")

# Load session previously saved with `instaloader -l USERNAME`
L.load_session_from_file(PROFILE)

profile = Profile.from_username(L.context, PROFILE)

followers = set(profile.get_followers())
following = set(profile.get_followees())

not_followers = following - followers

for not_follower in not_followers:
    print(not_follower.username)