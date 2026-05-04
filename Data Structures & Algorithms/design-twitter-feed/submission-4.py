from collections import defaultdict

class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.followers = defaultdict(set)
        self.unfollowed = defaultdict(set)
        self.timestamp = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        self.tweets[userId].append((self.timestamp, tweetId))
       
    def getNewsFeed(self, userId: int) -> List[int]:
        
        def bruteForce(self, userId):
            feed = self.tweets[userId].copy()
            for followerId in self.get_followers(userId):
                feed.extend(self.tweets[followerId])
            return list(
                map(
                    lambda x: x[1],
                    sorted(feed, reverse=True)
                )
            )[:10]
        
        return bruteForce(self, userId)

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.unfollowed[followerId]:
            self.unfollowed[followerId].remove(followeeId)
        if followeeId not in self.followers[followerId]:
            self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.unfollowed[followerId].add(followeeId)
    
    def get_followers(self, userId: int) -> List[int]:
        return [
            x for x in self.followers[userId]
            if x not in self.unfollowed[userId] and x != userId
        ]