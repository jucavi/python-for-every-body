import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **balls):
        if not balls:
            raise AttributeError("You must provide at least one ball")
        self.contents = [key for key, value in balls.items() for _ in range(value)]
        
    def draw(self, num_balls_drawn):
        if num_balls_drawn > len(self.contents):
            return self.contents
        return [self.contents.pop(random.randint(0, len(self.contents) - 1)) for _ in range(num_balls_drawn)]
         
            
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    event_success = 0
    for _ in range(num_experiments):
        copy_hat = copy.deepcopy(hat)
        balls_drawn = copy_hat.draw(num_balls_drawn)
        match = all(balls_drawn.count(ball) >= expected_balls[ball] for ball in expected_balls if ball in balls_drawn)
        match = match and all(ball in balls_drawn for ball in expected_balls)
        
        if match:
            event_success += 1
        
    return event_success / num_experiments