
class Rectangle {

    constructor(name, length, width, height)
    {
        this.name = name;
        this.length = length;
        this.width = width;
        this.height = height;
        console.log("object " + this.name + " has been created");
    }

    get name() {
        return this._name;
    }

    set name(name){
        this._name = name;
    } 

    set length(length){
        this._length = length;
    }

    set width(width){
        this._width = width;
    }

    set height(height){
        this._height = height;
    }
    
    get area() {
        return (this._length * this._width);
    }

    get volume() {
        return (this._length * this._width * this._height);
    }

    

}

function sum(num1, num2)
{
    return num1 + num2;
}

let arr = new Array(2, 4, 6, 8, 10);


let array = [1, 3, 5, 7, 9];
for(let i = 0; i < array.length; i++){
    console.log("from array " + array[i]);
}




// num1 = 27;
// num2 = 33;
// console.log("the sum of the two numbers is " + sum(num1, num2));

// rect1 = new Rectangle("wrecktangle", 20, 5, 10);
// console.log(rect1.area);
// console.log(rect1.volume);