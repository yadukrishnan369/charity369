var point = /** @class */ (function () {
    function point() {
    }
    Object.defineProperty(point.prototype, "x", {
        get: function () {
            return this._x;
        },
        set: function (value) {
            if (value < 0) {
                throw new Error('x');
            }
            this._x = value;
        },
        enumerable: false,
        configurable: true
    });
    return point;
}());
var c1 = new point();
c1.x = 10;
var y = c1.x;
console.log(y);
