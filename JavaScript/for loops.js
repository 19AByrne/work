//  for loops

for (let i = 0;i <= 10; i=i+1){
    if (i%2 ==1){
        console.log(i);
        console.log(i*2);
    }
    else if(i%2 ==0){
        console.log('Even number found,', i);
    }
    else{
        console.log('unknown number')
    }
}


function addTwoNumbers(number1, number2){
    let sum = number1+number2;
    return sum;
}

let answer = addTwoNumbers(0.1,0.2);
console.log(answer);