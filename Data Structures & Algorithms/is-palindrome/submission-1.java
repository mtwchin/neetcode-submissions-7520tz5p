class Solution {
    public boolean isPalindrome(String s) {
        if(s.length() == 0){
            return false;
        }else{
            StringBuilder str = new StringBuilder();
            for(char c : s.toCharArray()){
                if(Character.isLetterOrDigit(c)){
                    str.append(Character.toLowerCase(c));
                }
            }
            if(str.toString().equals(str.reverse().toString())){
                return true;
            }else{
                return false;
            }
        }
        
    }
}
