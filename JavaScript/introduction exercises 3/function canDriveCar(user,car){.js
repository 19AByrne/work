function canDriveCar(user,car){
if (user['age'] >= 18 || car['engineSize'] >= 100){
    console.log(true)}
else{
    console.log(false);
}
}

let user1 = {'name':'John','age':21};
let car1 = {'engineSize':1200,'name':'Mazda 3'};
canDriveCar(user1,car1)