
class Solution {
    public boolean isPalindrome(String s) {
        String lower = s.toLowerCase();
        int p1 = 0;
        int p2 = s.length() - 1;
        while(p1 <= p2){
            if(!Character.isLetterOrDigit(lower.charAt(p1))){
                p1++;
            }else if(!Character.isLetterOrDigit(lower.charAt(p2))){
                p2--;
            }else{
                if(lower.charAt(p1) != lower.charAt(p2)){
                    return false;
                }
                p1++;
                p2--;
            }
        }
        return true;
    }
}
