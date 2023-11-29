def doSomething3():
    pass
def doSomething():
    pass
def doSomething2():
    pass
doSomething()
doSomething2()
doSomething3()
# Create a function to run in our loopdef on_forever():    # Show this string on the micro:bit LED display    basic.show_string("Hello, World!")    # Show the heart image on the micro:bit LED display    basic.show_icon(IconNames.HEART)# call the on_forever function in a 'forever' loopbasic.forever(on_forever)
