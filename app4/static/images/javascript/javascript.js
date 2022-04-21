function setnumber(n) {
    document.getElementById('display').value += n;
    console.log(hiii);
}

function operation(op) {
    firstnum = document.getElementById('display').value;
    opnum = op;
    document.getElementById('display').value = '';
}

function result() {

    secondnum = document.getElementById('display').value;
    console.log(opnum);
    console.log(firstnum);
    console.log(secondnum);

    if (opnum == '+') {
        document.getElementById('display').value = Number(firstnum) + Number(secondnum);


    }
    if (opnum == '-') {
        document.getElementById('display').value = Number(firstnum) - Number(secondnum);
    }

    if (opnum == '*') {
        document.getElementById('display').value = Number(firstnum) * Number(secondnum);
    }

    if (opnum == '/') {
        document.getElementById('display').value = Number(firstnum) / Number(secondnum);
    }
}