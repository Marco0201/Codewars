# Task

# Each day a plant is growing by upSpeed meters. Each night that plant's height decreases by downSpeed meters due to the lack of sun heat. Initially, plant is 0 meters tall. We plant the seed at the beginning of a day. We want to know when the height of the plant will reach a certain level.
# Example

# For upSpeed = 100, downSpeed = 10 and desiredHeight = 910, the output should be 10.

# After day 1 --> 100
# After night 1 --> 90
# After day 2 --> 190
# After night 2 --> 180
# After day 3 --> 280
# After night 3 --> 270
# After day 4 --> 370
# After night 4 --> 360
# After day 5 --> 460
# After night 5 --> 450
# After day 6 --> 550
# After night 6 --> 540
# After day 7 --> 640
# After night 7 --> 630
# After day 8 --> 730
# After night 8 --> 720
# After day 9 --> 820
# After night 9 --> 810
# After day 10 --> 910

# For upSpeed = 10, downSpeed = 9 and desiredHeight = 4, the output should be 1.

# Because the plant reach to the desired height at day 1(10 meters).

# After day 1 --> 10

# Input/Output

#     [input] integer upSpeed

#     A positive integer representing the daily growth.

#     Constraints: 5 ≤ upSpeed ≤ 100.

#     [input] integer downSpeed

#     A positive integer representing the nightly decline.

#     Constraints: 2 ≤ downSpeed < upSpeed.

#     [input] integer desiredHeight

#     A positive integer representing the threshold.

#     Constraints: 4 ≤ desiredHeight ≤ 1000.

#     [output] an integer

#     The number of days that it will take for t
def growing_plant(upSpeed, downSpeed, desiredHeight):
    num = 0
    output = 0
    while num <= desiredHeight:
        num += upSpeed
        output += 1
        if num < desiredHeight:
            num -= downSpeed
        else:
            return output

# or this solution also works


def growing_plant(upSpeed, downSpeed, desiredHeight):
    num = upSpeed  # make num == upSpeed, for the first day
    output = 1  # since num is equal to upSpeed then output should equal 1 to reflect the first day
    while num < desiredHeight:  # loop until you get the desired number
        # add upSpeed to num, but before that substract upSpeed by downSpeed
        num += (upSpeed - downSpeed)
        output += 1  # this is the amount of days it takes for num to equal desiredHeight
    return output
