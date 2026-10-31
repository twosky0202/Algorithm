import java.util.*;

class Solution {
    Set<Integer> set = new HashSet<>();
    
    public int solution(String numbers) {
        int answer = 0;
        
        set.clear();
        
        boolean[] visited = new boolean[numbers.length()];
        
        // 모든 숫자 조합 만들기
        dfs(numbers, "", visited);

        // 소수 개수 세기
        for (int num : set) {
            if (isPrime(num)) {
                answer++;
            }
        }
        return answer;
    }
    
    // DFS로 가능한 숫자 만들기
    public void dfs(String numbers, String current, boolean[] visited) {

        if (!current.isEmpty()) {
            set.add(Integer.parseInt(current));
        }

        for (int i = 0; i < numbers.length(); i++) {
            if (!visited[i]) {
                visited[i] = true;

                dfs(numbers, current + numbers.charAt(i), visited);

                visited[i] = false;
            }
        }
    }

    // 소수 판별
    public boolean isPrime(int n) {
        if (n < 2) return false;

        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                return false;
            }
        }

        return true;
    }
}