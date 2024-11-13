function getBiggestNumberInArrays(numbers1, numbers2){
    let max1 = numbers1[0]
    let max2 = numbers2[0]
    for(i in numbers1){
        if (numbers1[i] > max1){
            max1 = numbers1[i]}}
    for(i in numbers2){
        if (numbers2[i] > max2){
            max2 = numbers2[i]}}
    
    if(max1>max2){
        return max1
    } else{
        return max2
    }
    
    
}

console.log(getBiggestNumberInArrays([1,2,3,45],[1,2,3,6]))

