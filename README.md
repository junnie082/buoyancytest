# buoyancytest

## Action Space
0: do nothing
1: go up
2: go right
3: go down
4: go left

Discrete(4)

## Observation Space
1280x800 image of diver and underwater.

## Rewards
+10 whenever the shark reaches the left side line of the screen.
+300 whenever the diver eats the prize. 
For example, if you avoided 10 sharks and ate 1 prize, you get 10 * 10 + 300 = 400 points.

## Starting State
The diver starts from the left side middle of the screen.

## Episode Termination
The episode finishes when the diver hits one shark.

## Reset Arguments
screen_size will be 1280, 800 (width, height) by default, but can be set freely.
 
