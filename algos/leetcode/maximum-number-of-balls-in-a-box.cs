#https://leetcode.com/problems/maximum-number-of-balls-in-a-box/
public class Solution {
    
    public int GetBoxNumber(int i){
        String number = i.ToString();
        int value = 0;
        foreach(Char c in number){
            value += int.Parse(c.ToString());
        }
        return value;
    }
    
    public int CountBalls(int lowLimit, int highLimit) {
        
        int maxBalls = 0;
        
        Dictionary <int, int> boxMap = new Dictionary <int, int>();
        for(int i=lowLimit; i<=highLimit; i++){
            var key = this.GetBoxNumber(i);
            if(!boxMap.ContainsKey(key)) boxMap[key] = 0;
            boxMap[key] += 1;
            if(boxMap[key] > maxBalls) maxBalls = boxMap[key];
        }
        
        return maxBalls;
    }
}


public class Solution
{
    public int CountBalls(int low, int high)
    {
        return Enumerable.Range(low, high - low + 1).GroupBy(DigitsSum).Max(g => g.Count());
    }
    private int DigitsSum(int n) => n.ToString().Sum(c => c - '0');
}