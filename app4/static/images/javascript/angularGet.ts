class point {
    private _x?:number
    constructor() {

    }
    set x(value) {
        if (value < 0){
            throw new Error('x')

        }
        this._x = value;

    }
    get x() {
        return this._x;
    }
}

let c1=new point();
c1.x=10;
var y=c1.x;
console.log(y)
