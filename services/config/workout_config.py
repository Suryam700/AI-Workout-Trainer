EXERCISE_OPTIONS = [
    "Squats", 
    "Push-ups", 
    "Bicep Curls (Dumbbell)", 
    "Shoulder Press", 
    "Lunges"
]

POSE_CONNECTIONS = [
    (11, 12), (11, 13), (13, 15), (12, 14), (14, 16), # line of shoulders and arms
    (11, 23), (12, 24), (23, 24), # line of torso and hips
    (23, 25), (24, 26), (25, 27), (26, 28), (27, 29), (28, 30), (29, 31), (30, 32), (27, 31), (28, 32) # line of legs
]