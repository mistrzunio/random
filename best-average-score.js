find_max_avg = function(scores) {
    agr = [];
    max_avg = 0;
    for (i in scores) 
        if (agr[scores[i][0]]) {
            agr[scores[i][0]].push(scores[i][1]);
            max_avg=Math.max(max_avg,agr[scores[i][0]].reduce((acc,curr)=>acc+curr)/agr[scores[i][0]].length)
        } else {
            agr[scores[i][0]]=[scores[i][1]];
            max_avg=Math.max(max_avg,scores[i][1])
        }
    //console.log(agr);  
    return(max_avg);
}

input = [["Bob", 52],["Ala", 92],["Mark", 37],["Bob", 48]];
