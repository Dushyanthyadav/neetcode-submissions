class Twitter {
private:
    int time = 0;
    priority_queue<pair<int, pair<int, int>>> recent_post;
    unordered_map<int, unordered_set<int>> follower_list; 
public:
    Twitter() {
        
    }
    
    void postTweet(int userId, int tweetId) {
        recent_post.push({time++, {userId, tweetId}});
    }
    
    vector<int> getNewsFeed(int userId) {
        vector<int> result;
        vector<pair<int, pair<int, int>>> not_interest;

        while (!recent_post.empty()) {
            auto recent = recent_post.top();
            if (follower_list[userId].contains(recent.second.first) || recent.second.first == userId) {
                if (result.size() == 10) {
                    break;
                }
                result.push_back(recent.second.second);
            }
            recent_post.pop();
            not_interest.push_back(recent);
        }
        
        while (!not_interest.empty()) {
            auto recent = not_interest[not_interest.size() - 1];
            not_interest.pop_back();
            recent_post.push(recent);
        }

        return result;
    }
    
    void follow(int followerId, int followeeId) {
        if (followerId == followeeId) {
            return;
        }
        follower_list[followerId].insert(followeeId);
    }
    
    void unfollow(int followerId, int followeeId) {
        if (followerId == followeeId) {
            return;
        }
        if (follower_list[followerId].contains(followeeId)) {
            follower_list[followerId].erase(followeeId);
        }
    }
};
