/**
 * @author Rabby Hossain
 * [Problem ref]{@link  https://leetcode.com/problems/design-twitter/}
 * @description Design a simplified version of Twitter where users can post tweets,
 *  follow/unfollow another user,
 *  and is able to see the 10 most recent tweets in the user's news feed.
 */

// TODO Time limit exceed
class TwetNode {
  constructor(tweetId, next = null, tweet_by, timestamp) {
    this.tweetId = tweetId;
    this.next = next;
    this.tweet_by = tweet_by;
    this.timestamp = timestamp;
  }
}

class Twitter {
  constructor() {
    this.users = {};
    this.timestamp = 0;
  }

  /** 
   * @param {number} userId 
   * @param {number} tweetId
   * @return {void}
   */
  postTweet(userId, tweetId) {
    // create new user if user doesn't exist
    if (!this.users[userId]) this.createUser(userId);

    // add the tweet to user's tweet linked list
    const user = this.users[userId];
    const new_tweet = new TwetNode(tweetId, user.feed, userId, this.timestamp);
    user.feed = new_tweet;

    // add the feed to own feed list
    const new_own_tweet = new TwetNode(tweetId, user.own_feed, userId, this.timestamp);
    user.own_feed = new_own_tweet;

    this.timestamp++;

    if (user.followers_count) {
      let followers = user.followers;
      // add the tweet to every follower's tweet linked list
      for (const follower in followers) {
        let user = this.users[follower];
        const new_tweet = new TwetNode(tweetId, user.feed, userId);
        user.feed = new_tweet;
      }
    }
  }


  /** 
   * @param {number} userId
   * @return {number[]}
   */
  getNewsFeed(userId) {
    const user = this.users[userId];
    let tweets = [];
    if (!user) return tweets;

    let tweetCount = 10;
    let feed = user.feed;
    while (feed && tweetCount) {
      const followee = this.users[feed.tweet_by];

      if (userId in followee.followers || userId === feed.tweet_by) {
        tweets.push(feed.tweetId);
        tweetCount--;
      }
      feed = feed.next;
    }

    return tweets;
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
    const follower = this.users[followerId];

    if (!followee.followers.hasOwnProperty(followerId)) {
      followee.followers[followerId] = true;
      followee.followers_count++;

      // add the tweets of followee's to followers
      if (follower.feed) {
        let runner = follower.feed;
        let previos_node = null;
        while (runner) {
          previos_node = runner;
          runner = runner.next;
        }
        previos_node.next = followee.own_feed;
        console.log("Before", follower.feed)
        follower.feed = mergeSort(follower.feed)
        console.log("after", follower.feed)
      } else {
        follower.feed = followee.own_feed
      }
    }

  }

  /** 
   * @param {number} followerId 
   * @param {number} followeeId
   * @return {void}
   */
  unfollow(followerId, followeeId) {
    // delete the follower from followee's follower list
    const followee = this.users[followeeId];
    delete followee.followers[followerId]
    followee.followers_count--;
  }

  /**
   * @param {number} userId
   * @return {void}
   */
  createUser(userId) {
    this.users[userId] = {
      feed: null,
      own_feed: null,
      followers_count: 0,
      followers: {},
    }
  }
}

function sortedMerge(a, b) {
  var result = null;
  /* Base cases */
  if (a == null)
    return b;
  if (b == null)
    return a;

  /* Pick either a or b, and recur */
  if (a.timestamp >= b.timestamp) {
    result = a;
    result.next = sortedMerge(a.next, b);
  } else {
    result = b;
    result.next = sortedMerge(a, b.next);
  }
  return result;
}

function mergeSort(h) {
  // Base case : if head is null
  if (h == null || h.next == null) {
    return h;
  }

  // get the middle of the list
  var middle = getMiddle(h);
  var nextofmiddle = middle.next;

  // set the next of middle node to null
  middle.next = null;

  // Apply mergeSort on left list
  var left = mergeSort(h);

  // Apply mergeSort on right list
  var right = mergeSort(nextofmiddle);

  // Merge the left and right lists
  var sortedlist = sortedMerge(left, right);
  return sortedlist;
}

// Utility function to get the middle
// of the linked list
function getMiddle(head) {
  if (head == null)
    return head;

  var slow = head, fast = head;

  while (fast.next != null && fast.next.next != null) {
    slow = slow.next;
    fast = fast.next.next;
  }
  return slow;
}