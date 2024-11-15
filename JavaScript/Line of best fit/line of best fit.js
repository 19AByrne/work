let points = [[8,3],[2,10],[11,3],[6,6],[5,8],[4,12],[12,1],[9,4],[6,9],[1,14]]

let meanx = 0
for (i in points){
    meanx = meanx + (points[i][0])
}
meanx = meanx/10
console.log(meanx)

let meany = 0
for (i in points){
    meany = meany + (points[i][1])
}
meany = meany/10
console.log(meany)

function vmeanv(v,meanv){
    return (v-meanv)}

points[0]