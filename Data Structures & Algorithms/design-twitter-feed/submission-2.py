class Twitter:

    def __init__(self):
        self.follower = defaultdict(set)
        self.posts = defaultdict(list) # maps user_id to tweet_id
        self.count = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append([self.count, tweetId])
        self.count -= 1
    
    def getNewsFeed(self, userId: int) -> List[int]:

        minHeap = []
        res = []
        self.follower[userId].add(userId)
        for followeeId in self.follower[userId]:
            if followeeId in self.posts:
                latestPost = len(self.posts[followeeId]) - 1
                count, tweetId = self.posts[followeeId][latestPost]
                heapq.heappush(minHeap, [count, tweetId, followeeId,latestPost-1])
        
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.posts[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        

        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follower[followerId]:
            self.follower[followerId].remove(followeeId)
        
