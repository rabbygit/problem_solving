/**
 * @author Rabby Hossain
 * [Problem ref]{@link  https://leetcode.com/problems/design-twitter/}
 * @description Design a simplified version of Twitter where users can post tweets,
 *  follow/unfollow another user,
 *  and is able to see the 10 most recent tweets in the user's news feed.
 */

// TODO Need to solve with heap or priority queue
class Twitter {
  constructor() {
    this.users = {};
    this.tweets = [];
  }

  /** 
   * @param {number} userId 
   * @param {number} tweetId
   * @return {void}
   */
  postTweet(userId, tweetId) {
    // create new user if user doesn't exist
    if (!this.users[userId]) this.createUser(userId);

    this.tweets.push({ tweetId, userId })
  }


  /** 
   * @param {number} userId
   * @return {number[]}
   */
  getNewsFeed(userId) {
    const user = this.users[userId];
    let feeds = [];
    if (!user) return feeds;

    let length = this.tweets.length;
    for (let index = length - 1; index >= 0 && feeds.length < 10; index--) {
      const tweet = this.tweets[index];
      if (tweet.userId === userId ||
        this.users[tweet.userId].followers.hasOwnProperty(userId)
      ) {
        feeds.push(tweet.tweetId);
      }
    }

    return feeds;
  }

  /** 
   * @param {number} followerId 
   * @param {number} followeeId
   * @return {void}
   */
  follow(followerId, followeeId) {
    // create users if not exists
    if (!this.users[followeeId]) this.createUser(followeeId);
    if (!this.users[followerId]) this.createUser(followerId);

    // add the follower to the followee's follower list
    const followee = this.users[followeeId];

    followee.followers[followerId] = true;
  }

  /** 
   * @param {number} followerId 
   * @param {number} followeeId
   * @return {void}
   */
  unfollow(followerId, followeeId) {
    // delete the follower from followee's follower list
    const followee = this.users[followeeId];
    delete followee.followers[followerId];
  }

  /**
   * @param {number} userId
   * @return {void}
   */
  createUser(userId) {
    this.users[userId] = {
      followers: {},
    }
  }
}