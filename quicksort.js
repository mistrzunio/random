function qs (a) {
    if (a.length <= 1)
        return a;
    let a1 = [];
    let a2 = [];
    let piv = a.pop();
    while (a != 0)
        (curr = a.pop()) < piv ? a1.push(curr) : a2.push(curr)
    return qs(a1).concat(piv, qs(a2))    
}
