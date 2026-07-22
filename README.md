# RoboGrip: CNN vs. Classical Antipodal Grasp Detection
Team Member: Pranav Venkatraman 

Project Details: RoboGrip is a system that predicts where and at what angle a robotic gripper should grasp an object directly from an RGB-D image, using a CNN trained on the Cornell Grasp Dataset. Instead of only reporting the CNN's accuracy, RoboGrip runs a controlled comparison against a classical geometry-based baseline: antipodal grasp detection (the pre-deep-learning approach), evaluated with the same IoU/angle correctness metric used in published research. RoboGrip also analyzes where the learned model's advantage actually comes from by breaking results down by object shape category.

