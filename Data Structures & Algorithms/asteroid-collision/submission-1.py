class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        '''
        create stack and res
        if asteroids[i] > 0:
            stack.append(asteroids[i])
        else:
            n = stack.peek()
            if n < -1 * asteroids[i]:
                stack.pop()
                allow loop to continue because asteroids[i] will be processed again
            elif n == -1 * asteroids[i]:
                destroy asteroids[i] and stack.pop() and continue
            elif n > -1 * asteroids[i]:
                destroy asteroids[i]
        return res
        if the current number in asteroids > top of stack, destroy top of stack 
        '''
        res, i = [], 0
        # process list of 2, go until 1 because 0, 1
        while i < len(asteroids):
            if asteroids[i] > 0 or not res or res[-1] < 0: # if current asteroid is negative
                res.append(asteroids[i])
            else: # if cur asteroid is negative
                topnum = res[-1]
                ast = -1 * asteroids[i]
                if topnum < ast: # if asteroid destroys stack top value
                    res.pop()
                    i -= 1
                elif topnum == ast:
                    res.pop()
            i += 1
        return res


