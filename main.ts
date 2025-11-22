function timer2 (last: number) {
    timer = last
    basic.pause(1000)
    basic.showNumber(timer)
    timer += -1
    if (timer == 0) {
    	
    } else {
        timer2(last - 1)
    }
}
let timer = 0
timer2(10)
