/**
 * @author Rabby Hossain
 * [Problem ref]{@link  https://leetcode.com/problems/cheapest-flights-within-k-stops/}
 * @description There are n cities connected by some number of flights. 
 * You are given an array flights where flights[i] = [fromi, toi, pricei] 
 * indicates that there is a flight from city fromi to city toi with cost pricei.
 * You are also given three integers src, dst, and k, 
 * return the cheapest price from src to dst with at most k stops. 
 * If there is no such route, return -1.
 */


/**
 * @param {number} n
 * @param {number[][]} flights
 * @param {number} src
 * @param {number} dst
 * @param {number} k
 * @return {number}
 */
const findCheapestPrice = function(n, flights, src, dst, k) {
    let previous = Array(n).fill(Number.POSITIVE_INFINITY) // keep shortest path using at most (k-1)th edges
    let current = Array(n).fill(Number.POSITIVE_INFINITY) // keep shortest path using at most (k)th edges

    // using no edges we can only go to the src node itself.so,cost is 0
    previous[src] = 0

    for (let index = 1; index < k+2; index++) {
        current[src] = 0

        flights.forEach(([previous_flight,current_flight,cost]) => {
            // path relaxation for every edge if needed
            if (previous[previous_flight] + cost < current[current_flight]) {
                current[current_flight] = previous[previous_flight] + cost
            }
        });

        // after every iteration update the previous state
        previous = [...current]
    }

    if (current[dst] === Number.POSITIVE_INFINITY) {
        return -1
    }

    return current[dst]
};