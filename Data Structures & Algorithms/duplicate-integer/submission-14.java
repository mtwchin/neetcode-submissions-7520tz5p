class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> vals = new HashSet<>();
        for(int i = 0; i < nums.length; i++){
            if(vals.contains(nums[i])){
                return true;
            }else{
                vals.add(nums[i]);
            }
        }
        return false;
    }
}