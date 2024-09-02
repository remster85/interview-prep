#https://leetcode.com/problems/longest-palindromic-substring/

class Solution {
    public String longestPalindrome(String s) {

        if(s == null || s.length() == 0) return "";

        Map<Character, List<Integer>> map = new HashMap<Character, List<Integer>>();
        for(int i=0; i<s.length(); i++){
            var c = s.charAt(i);
            if(!map.containsKey(c)) map.put(c, new ArrayList<Integer>());
            var indicesForChar = map.get(c);
            indicesForChar.add(i);
        }
        System.out.println(map);

        var longest = String.valueOf(s.charAt(0));
        var maxBound = s.length();
        
        for(int i=0; i<maxBound; i++){
            var c = s.charAt(i);
            var matchingIndices = map.get(c);
            for(var matchingIndice : matchingIndices){
                if(matchingIndice > i){
                    //System.out.println("matching indice " + matchingIndice);
                    var currentpal = "";
                    var j = i;
                    var k = matchingIndice;
                    var isPalin = true;
                    while(k>=j && k>=0 && j>=0){
                        j = j+1;
                        k = k-1;
                        if(!(s.charAt(j) == s.charAt(k))){
                            isPalin = false;
                            break;
                        }
                    }
                    if(isPalin){
                        currentpal = s.substring(i, matchingIndice + 1);
                        if(currentpal.length() >= longest.length()) longest = currentpal;
                    }
                }
            }
        }


        return longest;
    }
}