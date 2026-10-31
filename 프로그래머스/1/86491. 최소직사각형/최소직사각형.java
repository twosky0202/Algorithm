class Solution {
    public int solution(int[][] sizes) {
        // 가로, 세로 정렬 -> 가로 제일큰, 세로 제일큰
        int wmax = 0;
        int hmax = 0;
        for (int i=0; i<sizes.length; i++) {
            if(sizes[i][0] < sizes[i][1]) {
                int temp = 0;
                temp = sizes[i][0];
                sizes[i][0] = sizes[i][1];
                sizes[i][1] = temp;
            }
            wmax = Math.max(wmax, sizes[i][0]);
            hmax = Math.max(hmax, sizes[i][1]);
        }
        int answer = 0;
        answer = wmax * hmax;
        return answer;
    }
}