"""
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
 

Example 1:

Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2"

Note: 
    Time Complexity: 
        set() -> O(1) (recall, searching and inserting into a hashmap is constant time)
        get() -> O(log n) (recall, time complexity of binary search is O(log n))
    Space Complexity:
        set() -> O(n)
        get() -> O(1)
"""
class TimeMap:
    def __init__(self):
        self.keyValueStore = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyValueStore:
            self.keyValueStore[key] = []
        self.keyValueStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.keyValueStore.get(key, []) # if the key is not found, it returns an empty list

        # binary search logic
        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + r) // 2
            if values[mid][1] == timestamp:
                res = values[mid][0]
                return res 
            elif values[mid][1] < timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1 
        return res



# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
obj.set("foo","bar1",1)
obj.set("foo", "bar2", 4)
param_2 = obj.get("foo",1)
param3 = obj.get("foo", 3)
param4 = obj.get("foo", 4)
param5 = obj.get("foo", 5)

print(param_2)
print(param3)
print(param4)
print(param5)
