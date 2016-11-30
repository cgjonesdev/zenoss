from pprint import pprint


class ParticleAnimation(object):

    def animate(self, speed, init):
        # Create result list and insert initial positions replaced with 'X'
        results = [init.replace('R', 'X').replace('L', 'X')]

        # Create lists to store separate movement of right and left
        moving_right = []
        moving_left = []

        # Track movements by storing particle indices
        positions = dict(enumerate(init))
        for k, v in positions.items():
            if v == 'R':
                # Make sure we don't add indices above the list bounds
                if k < len(init):
                    moving_right.append(k)
            if v == 'L':
                # Make sure we don't add indices below the list bounds
                if k >= 0:
                    moving_left.append(k)

        # Create and set bidiredctional temp lists since even casting incoming
        # `init` param to a list and changing it's values will destroy needed
        # position references as the clock ticks and would provide only a way
        # to service one direction at a time - but we need both!
        tempR = []
        tempL = []
        for i in init:
            tempR.append(i) if i != 'R' else tempR.append('.')
            tempL.append(i) if i != 'L' else tempL.append('.')

        # Start the clock and store new positions in temp lists with each tick
        for i in range(len(init)):
            for j, r in enumerate(moving_right):
                try:
                    tempR[moving_right[j]] = '.'
                    moving_right[j] += speed
                except:
                    pass
            for j, l in enumerate(moving_left):
                try:
                    tempL[moving_left[j]] = '.'
                    moving_left[j] -= speed
                except:
                    pass
            for r in moving_right:
                try:
                    tempR[r] = 'X'
                except:
                    pass
            for l in moving_left:
                if l >= 0:
                    try:
                        tempL[l] = 'X'
                    except:
                        pass  

            # Create temp list containing all "."'s to be replaced by an 'X'
            # where it exists in either tempR or tempL lists
            temp = list('.' * len(init))

            # Loop through zipped tempR and tempL and check for 'X'. Replace
            # '.' with 'X' where it exists in tempR and tempL.
            for i, (r, l) in enumerate(zip(tempR, tempL)):
                if r == 'X' or l == 'X':
                    temp[i] = 'X'
                # print temp

            # Add result of clock tick to results list for final display
            results.append(''.join(temp))

            # Check that we're not adding extraneous rows of dots at the end
            # due to unused clock ticks
            if all([t == '.' for t in temp]):
                break 

        return results                             


if __name__ == '__main__':
    print '\nExample 0:\n'
    pprint(ParticleAnimation().animate(2,  '..R....'))
    print '\nExample 1:\n'
    pprint(ParticleAnimation().animate(3,  'RR..LRL'))
    print '\nExample 2:\n'
    pprint(ParticleAnimation().animate(2,  'LRLR.LRLR'))
    print '\nExample 3:\n'
    pprint(ParticleAnimation().animate(10, 'RLRLRLRLRL'))
    print '\nExample 4:\n'
    pprint(ParticleAnimation().animate(1,  '...'))
    print '\nExample 5:\n'
    pprint(ParticleAnimation().animate(1, 'LRRL.LR.LRR.R.LRRL.'))
