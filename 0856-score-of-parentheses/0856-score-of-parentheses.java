class Solution {
    public int scoreOfParentheses(String s) {
        Stack<Integer> stk = new Stack<>();
        stk.push(0);
        for(char ch : s.toCharArray()){
            if(ch == '('){
                stk.push(0);
            }else{
                int inside = stk.pop();
                int b;
                if(inside == 0){
                    b = 1;
                }else{
                    b = 2*inside;
                }
                stk.push(stk.pop() + b);
            }
        }
        return stk.pop();
    }
}