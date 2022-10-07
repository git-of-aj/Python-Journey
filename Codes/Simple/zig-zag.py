import time, sys
indent = 0 # How many spaces to indent.
indentIncreasing = True # Whether the indentation is increasing or not.

try:
    while True: # The main program loop.
        print(' ' * indent, end='')  #it turns the line .. both end + indenet line
        print('🙋‍♂️🙋‍♂️🙋‍♂️🙋‍♂️')
        time.sleep(0.0001) # Pause for 1/10000 of a second.

        if indentIncreasing:
            # make it move to right By Increase the number of spaces:
            indent = indent + 1
            if indent == 20: # tilt the line till this line number
                # Change direction:
                indentIncreasing = False

        else:
            # Decrease the number of spaces and make it move to left:
            indent = indent - 1
            if indent == 0:
                # Change direction:
                indentIncreasing = True
except KeyboardInterrupt:
    print('Finally, out of the Game !')
    sys.exit()
