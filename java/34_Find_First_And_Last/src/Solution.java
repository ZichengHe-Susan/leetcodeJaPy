import java.util.*;

class Solution {
    public static int[] searchRange(int[] nums, int target){
        int small = lowerBound(nums, target);
        if( small == nums.length || nums[small] != target){
            return new int[]{-1, -1};
        }
        int large = lowerBound(nums,target + 1) - 1;

        return new int[]{small, large};
    }
    private static int lowerBound(int[] nums, int target){
        int left = 0;
        int right = nums.length - 1;
        while( left <= right ){
            int mid = left + (right - left) /2;
            if(nums[mid]  < target){
                left = mid + 1;
            }else{
                right = mid - 1;
            }
        }
        return left;
    }
    public static void main(String[] args){
        int[] nums1 = new int[]{1,2,3,4,5,5,5,8};
        int target1 = 5;
        int[] res1 = searchRange(nums1, target1);
        System.out.printf("searchRange Result of nums1 and target1:%d, %d", res1[0], res1[1]);
    }
}