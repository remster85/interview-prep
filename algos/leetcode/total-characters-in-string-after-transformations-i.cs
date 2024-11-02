#https://leetcode.com/problems/total-characters-in-string-after-transformations-i/

public class Solution {

    public string Transform(char c){
        if(c == 'z') return "ab";
        return ((char) (((int)c) + 1)).ToString();
    }

    public int LengthAfterTransformations(string s, int t) {
        String current = s;

        for(int i=0; i<t; i++){
            var sss = "";    
            foreach(var c in current){
                sss += Transform(c);
            }
            current = sss;
        }
        
        return current.Length;
    }
}
