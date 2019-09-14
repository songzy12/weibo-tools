from config import UID, ACCESS_TOKEN
from utils import home_page
import friendships

if __name__ == '__main__':
    follower_ids = friendships.follower_ids(UID, ACCESS_TOKEN)
    print("zombies:")
    for uid in follower_ids:
        print(home_page(uid))