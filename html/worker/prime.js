function isprime(number) {
    for (let i = 2; i <= number ** 0.5; i++) {
        if (number % i == 0) return false;
    }
    return true
}

onmessage = function (e) {// worker 태스크 생성시 이 onmessage 이벤트가 생긴다.
    let parameters = {
        flag: isprime(parseInt(e.data.input)),
        val: e.data.input
    }
    postMessage(parameters);
}