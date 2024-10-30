#https://leetcode.com/problems/lru-cache/solutions/3781030/c-solution-for-lru-cache-problem/
public class LRUCache {

    private readonly int capacity;
    private readonly Dictionary<int, LinkedListNode<CacheItem>> cacheMap;
    private readonly LinkedList<CacheItem> cacheList;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        cacheMap = new Dictionary<int, LinkedListNode<CacheItem>>(capacity);
        cacheList = new LinkedList<CacheItem>();
    }
    
    public int Get(int key) {
        if (cacheMap.TryGetValue(key, out var node))
        {
            cacheList.Remove(node);
            cacheList.AddFirst(node);
            return node.Value.Value;
        }
        return -1;
    }
    
    public void Put(int key, int value) {
        if (cacheMap.TryGetValue(key, out var node))
        {
            node.Value.Value = value;
            cacheList.Remove(node);
            cacheList.AddFirst(node);
        }
        else
        {
            if (cacheMap.Count >= capacity)
            {
                var lastNode = cacheList.Last;
                cacheMap.Remove(lastNode.Value.Key);
                cacheList.RemoveLast();
            }

            var newNode = new LinkedListNode<CacheItem>(new CacheItem(key, value));
            cacheMap.Add(key, newNode);
            cacheList.AddFirst(newNode);
        }
    }

    private class CacheItem
    {
        public int Key { get; }
        public int Value { get; set; }

        public CacheItem(int key, int value)
        {
            Key = key;
            Value = value;
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.Get(key);
 * obj.Put(key,value);
 */
