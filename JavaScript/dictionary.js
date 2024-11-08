let myObject = {'a':1,'b':2,'c':3};
console.log(myObject)

// to loop through keys
for (key in myObject){
    console.log(key, myObject[key]);
}


// to return a list of keys
let myKeys = Object.keys(myObject);
console.log(myKeys);

// to return a list of values
let myValues = Object.values(myObject);
console.log(myValues);

// to return a key, value pair
let myKVpairs = Object.entries(myObject);
console.log(myKVpairs);

// The forEach method can be used with an array
// it passes every value in the arry into a function
function doubleValues(valueIn){
    console.log(valueIn*2);
}
myValues.forEach(doubleValues);
// for... of will loop through each value in an array (list comprehension and map())



for (let v of myValues){
    console.log(v);
}

// To make an object from a list
let myDictionary = Object.fromEntries(myKVpairs);
