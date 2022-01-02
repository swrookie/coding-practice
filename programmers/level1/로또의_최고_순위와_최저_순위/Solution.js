function solution(lottos, win_nums) {
    var answer = [];

    let match = 0;
    let zeros = 0;

    lottos.forEach(lotto => {
        if (lotto === 0) {
            zeros++;
        }
    });

    win_nums.forEach(win_num => {
        match += lottos.filter(lotto => win_num === lotto).length;
    });

    answer[0] = 7 - (match + zeros) < 7 ? 7 - (match + zeros) : 6;
    answer[1] = 7 - match < 7 ? 7 - match : 6;

    return answer;
}

function init() {
    lottos = [44, 1, 0, 0, 31, 25];
    win_nums = [31, 10, 45, 1, 6, 19];

    console.log(solution(lottos, win_nums));
}

init();