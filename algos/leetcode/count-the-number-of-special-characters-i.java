#https://leetcode.com/problems/count-the-number-of-special-characters-i
class Metrics{
    public boolean upper;
    public boolean lower;
    public boolean special;
    
    public Metrics(){
    }
    
}

class Solution {
    public int numberOfSpecialChars(String word) {
        var myMap = new HashMap<String, Metrics>();
        
         for (Character c : word.toCharArray()) {
            var key = c.toString().toLowerCase();
            if(!myMap.containsKey(key)) myMap.put(key, new Metrics());
            var metric = myMap.get(key);
            if(metric.special) continue;
             
            if(c.toString().equals(key)){
                //lower
                if(!metric.lower) metric.lower = true; 
                if(metric.upper) metric.special = true; 
            }else{
                //upper
                if(!metric.upper) metric.upper = true;   
                if(metric.lower) metric.special = true; 
            }             
            
        
        }
        return myMap.values().stream().filter(m -> m.special).toList().size();
    }
}