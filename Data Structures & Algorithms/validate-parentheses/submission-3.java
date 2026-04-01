class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        java.util.Map<Character, Character> closeToOpen = new java.util.HashMap<>();
        closeToOpen.put(')', '(');
        closeToOpen.put(']', '[');
        closeToOpen.put('}', '{');

        for(int i = 0; i < s.length(); i++){
            if (closeToOpen.containsKey(s.charAt(i))){
                if(!stack.isEmpty() && stack.peek() == closeToOpen.get(s.charAt(i))){
                    stack.pop();
                }else{
                    return false;
                }
            }else{
                stack.push(s.charAt(i));
            }
        }
        return stack.isEmpty();
    }
}
