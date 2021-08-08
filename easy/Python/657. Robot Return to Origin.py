#Date: Aug 07, 2021
#Question:
#There is a robot starting at position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.

#The move sequence is represented by a string, and the character moves[i] represents its ith move. Valid moves are R (right), L (left), U (up), and D (down). If the robot returns to the origin after it finishes all of its moves, return true. Otherwise, return false.

#Note: The way that the robot is "facing" is irrelevant. "R" will always make the robot move to the right once, "L" will always make it move left, etc. Also, assume that the magnitude of the robot's movement is the same for each move.
#Type: Easy

#Comment: solved it first try, just need to look up .count method google

#Thoughts:

#Since it's a 2D plane, as long as Up, Down && Left, Right matches, then it'll be back at origin.
#so simply count the amount of time U/D/L/R occured and have a if statement, done

def judgeCircle(self, moves: str) -> bool:
    up = moves.count('U')
    down = moves.count('D')
    left = moves.count('L')
    right = moves.count('R')
    if up == down and left == right:
        return True
    else:
        return False

#Runtime: 32 ms, faster than 94.88% of Python3 online submissions for Robot Return to Origin.
#Memory Usage: 14.5 MB, less than 51.55% of Python3 online submissions for Robot Return to Origin.
#08/07/2021 21:20	Accepted	32 ms	14.5 MB	python3        
            
