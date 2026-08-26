class Twitter {
private:
    int timestamp;
    unordered_map<int, vector<std::pair<int, int>>> user_tweets;
    unordered_map<int, unordered_set<int>> follows;
public:
    Twitter() {
        timestamp = 0;
    }
    
    void postTweet(int userId, int tweetId) {
        user_tweets[userId].push_back({timestamp++, tweetId});
    }
    
    vector<int> getNewsFeed(int userId) {
        vector<int> feed;
        unordered_set<int> authors = follows[userId];
        authors.insert(userId);

        using TweetNode = tuple<int, int, int, int>;
        priority_queue<TweetNode> pq;

        for (int authorId: authors) {
            const auto& tweets = user_tweets[authorId];
            if (!tweets.empty()) {
                int lastIdx = tweets.size() - 1;
                pq.push({tweets[lastIdx].first, tweets[lastIdx].second, authorId, lastIdx - 1});
            }
        }

        while (!pq.empty() && feed.size() < 10) {
            auto [time, tweetId, authorId, nextIdx] = pq.top();
            pq.pop();
            feed.push_back(tweetId);

            if (nextIdx >= 0) {
                const auto& tweets = user_tweets[authorId];
                pq.push({tweets[nextIdx].first, tweets[nextIdx].second, authorId, nextIdx - 1});
            }
        }

        return feed;
    }
    
    void follow(int followerId, int followeeId) {
       if (followerId != followeeId) {
        follows[followerId].insert(followeeId);
       } 
    }
    
    void unfollow(int followerId, int followeeId) {
       if (followerId != followeeId) {
        follows[followerId].erase(followeeId);
       } 
    }
};
