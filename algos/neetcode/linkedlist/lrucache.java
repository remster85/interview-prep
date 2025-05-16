https://stackoverflow.com/questions/27475797/use-linkedhashmap-to-implement-lru-cache

class LRUCache {

     private LinkedHashMap<Integer, Integer> linkHashMap;

     public LRUCache(int capacity) {
        linkHashMap = new LinkedHashMap<Integer, Integer>(capacity, 0.75F, true) {
          @Override
          protected boolean removeEldestEntry(Map.Entry<Integer, Integer> eldest) {
             return size() > capacity;
          }
       };
     }

     public void put(int key, int value) {
        linkHashMap.put(key, value);
     }

     public int get(int key) {
       return linkHashMap.getOrDefault(key, -1);
     }

 } 
