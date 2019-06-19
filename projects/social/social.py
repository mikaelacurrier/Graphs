import random
from util import Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        # self.lastID = 0
        # self.users = {}
        # self.friendships = {}


        # Add users
        for i in range(numUsers):
            self.addUser(self.lastID+1)

        # Create friendships
        for user in self.users:
            for i in range(random.randrange(0,avgFriendships+1)):
                friend = random.randrange(1,len(self.users))

                if friend == user or friend in self.friendships.get(user):
                    i -= 1
                elif friend < user:
                    self.addFriendship(friend, user)
                else:
                    self.addFriendship(user, friend)


    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}
        q = [ [userID] ]
        v = self.friendships

        for i in range(len(v)):
            path = q.pop(0)
            visit = path[-1]
            branch = set(self.unvisited_edge(visit, visited))
            for i in branch:
                full_path = path + [i]
                visited[i] = full_path
                q.append(full_path)
            if len(q) == 0:
                break

        return visited
    def unvisited_edge(self, vertex, visited):
        v = self.friendships
        return [i for i in v.get(vertex) if i not in visited]

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 3)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
