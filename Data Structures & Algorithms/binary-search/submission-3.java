class Solution {
    public int search(int[] nums, int target) {
        int L = 0;
        int R = nums.length - 1;

        while (L <= R){
            int C = (L+R)/2;
            if(nums[C] == target){
                return C;
            }else if(target < nums[C]){
                R = C - 1;
            }else if(target > nums[C]){
                L = C + 1;
            }
        }
        return -1;
    }
}
