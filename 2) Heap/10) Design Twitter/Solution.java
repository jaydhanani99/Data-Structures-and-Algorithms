// https://leetcode.com/problems/design-twitter/

class Tweet{
    public int id, time;
    Tweet(int id, int time) {
        this.id = id;
        this.time = time;
    }
}
class Twitter {
    public HashMap<Integer, List<Tweet>> userOwnTweets;
    public HashMap<Integer, HashSet<Integer>> followerList;
    public int tweetTimestamp;
    public Twitter() {
        userOwnTweets = new HashMap<Integer, List<Tweet>>();
        followerList = new HashMap<Integer, HashSet<Integer>>();
        tweetTimestamp = 0;
    }
    
    public void postTweet(int userId, int tweetId) {
        List<Tweet> ownTweet;
        if (!userOwnTweets.containsKey(userId)) {
            ownTweet = new ArrayList<Tweet>();
        } else {
            ownTweet = userOwnTweets.get(userId); 
        }
        ownTweet.add(new Tweet(tweetId, tweetTimestamp));
        tweetTimestamp++;
        userOwnTweets.put(userId, ownTweet);
    }
    
    public List<Integer> getNewsFeed(int userId) {
        PriorityQueue<Tweet> pq = new PriorityQueue<Tweet>((t1, t2) ->(t1.time - t2.time));
        
        // Adding follower tweets and own tweets
        HashSet<Integer> follower = followerList.get(userId);
        if (follower == null) {
            follower = new HashSet<Integer>();
        }
        follower.add(userId);
        
        int counter = 0;
        for(int currentUserId :follower) {
            List<Tweet> tweets = userOwnTweets.get(currentUserId);
            if (tweets != null) {
                for (Tweet tweet: tweets) {
                    counter++;
                    if (counter > 10) pq.remove();
                    pq.offer(tweet);
                }
            }
        }
        
        List<Integer> ans = new ArrayList<>();
        while (!pq.isEmpty()) {
            ans.add(pq.poll().id);
        }
        Collections.reverse(ans);
        return ans;
    }
    
    public void follow(int followerId, int followeeId) {
        if (followerList.containsKey(followerId)) {
            followerList.get(followerId).add(followeeId);
        }else {
            HashSet<Integer> followerSet = new HashSet<>();
            followerSet.add(followeeId);
            followerList.put(followerId, followerSet);
        }
        
    }
    
    public void unfollow(int followerId, int followeeId) {
        if (followerList.containsKey(followerId)) followerList.get(followerId).remove(followeeId);
    }
}

/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter obj = new Twitter();
 * obj.postTweet(userId,tweetId);
 * List<Integer> param_2 = obj.getNewsFeed(userId);
 * obj.follow(followerId,followeeId);
 * obj.unfollow(followerId,followeeId);
 */