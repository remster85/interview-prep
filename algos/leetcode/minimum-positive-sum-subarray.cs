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

#optimize
public class Solution {
    public int MinimumSumSubarray(IList<int> nums, int l, int r) {
        int n = nums.Count;
        int min = int.MaxValue;

        for (int start = 0; start < n; start++) {
            int sum = 0;
            for (int end = start; end < n && end - start + 1 <= r; end++) {
                sum += nums[end];
                if (end - start + 1 >= l && sum > 0) {
                    min = Math.Min(min, sum);
                }
            }
        }

        return min == int.MaxValue ? -1 : min;
    }


}