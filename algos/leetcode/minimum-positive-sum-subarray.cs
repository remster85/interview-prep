#https://leetcode.com/problems/minimum-positive-sum-subarray/
public class Solution {
    public int MinimumSumSubarray(IList<int> nums, int l, int r) {
        int j=0;
        int min = 1000000;

        for(int i=0; i<nums.Count; i++){
            var sum=0;
            j=i;
            while(j < nums.Count && j-i<=r-1){
                sum+= nums[j];
                if(j-i>= l-1  && sum < min && sum > 0) min = sum;
                //Console.WriteLine($"i = {i} ; j = {j} ; j-i = {j-i} Min = {min} Sum {sum}");
                j++;       
            }
        }
        return (min == 1000000) ? -1 : min ;
    }
}