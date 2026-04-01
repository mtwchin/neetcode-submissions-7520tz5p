class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        /* 
        - first, create a hashmap for cur str
        - 
        */
        Map<String, List<String>> vals = new HashMap<>();
        for(String s : strs){
            char[] c_arr = s.toCharArray();
            Arrays.sort(c_arr);
            String sortedS = new String(c_arr);
            vals.putIfAbsent(sortedS, new ArrayList<>());
            vals.get(sortedS).add(s);
        }

        return new ArrayList<>(vals.values());
    }
}
