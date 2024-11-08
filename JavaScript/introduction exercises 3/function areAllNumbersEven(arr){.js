function areAllNumbersEven(arr){
    let evenCount = 0
    for (i in arr){
        console.log(arr[i]);
        if (arr[i] % 2 == 0){
            evenCount++
        }
    
    }
    if (evenCount == arr.length){
        console.log('all numbers even')
    }
}

areAllNumbersEven([2,4])