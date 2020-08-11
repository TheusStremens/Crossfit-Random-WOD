from collections import defaultdict
from random import randint


abs_muscles = ["upper", "lower", "lateral"]
other_muscles = ["shoulder", "biceps", "back", "chest", "hamstring", "quadriceps"]

abs_exercises = defaultdict(list)
abs_exercises["upper"].append("Crunch")
abs_exercises["upper"].append("Sit-up")
abs_exercises["upper"].append("Montain Climber")
abs_exercises["lower"].append("Leg Lever")
abs_exercises["lower"].append("Dragon Flag")
abs_exercises["lateral"].append("Dumbbell Side Bend")
abs_exercises["lateral"].append("Oblique Side Crunch")
abs_exercises["lateral"].append("Sit-ups to Twist")
abs_exercises["lateral"].append("Side Planks")

other_exercises = defaultdict(list)
other_exercises["shoulder"].append("Dumbbell Shoulder Press")
other_exercises["shoulder"].append("Front Raise")
other_exercises["shoulder"].append("Bent-Over Dumbbell Lateral Raise")
other_exercises["shoulder"].append("Dumbbell Lateral Raise")
other_exercises["shoulder"].append("Pike Push-up")
other_exercises["shoulder"].append("Thruster")
other_exercises["shoulder"].append("Overhead Dumbbell Reverse Lunge")

other_exercises["biceps"].append("Standing Dumbbell Curl Alternate")
other_exercises["biceps"].append("Standing Dumbbell Curl")
other_exercises["biceps"].append("Hammer Curl")
other_exercises["biceps"].append("Dumbbell Concentration Curl")

other_exercises["back"].append("Dumbbell Single Arm Row")
other_exercises["back"].append("Bent-Over Barbell Row")
other_exercises["back"].append("Dumbbell Pull-Over")
other_exercises["back"].append("Superman")
other_exercises["back"].append("Pull-up")

other_exercises["chest"].append("Push-up")
other_exercises["chest"].append("Fly")
other_exercises["chest"].append("Bench Press")
other_exercises["chest"].append("Decline Push-up")
other_exercises["chest"].append("Dips")
other_exercises["chest"].append("Diamond Push-up")
other_exercises["chest"].append("Wide Push-up")
other_exercises["chest"].append("Hand-release Push-up")

other_exercises["hamstring"].append("Deadlift")
other_exercises["hamstring"].append("Sumo deadlift")
other_exercises["hamstring"].append("Single-Leg Dumbbell Straight-Leg Deadlift")

other_exercises["quadriceps"].append("Squat")
other_exercises["quadriceps"].append("Step-up")
other_exercises["quadriceps"].append("Reverse Lunge")
other_exercises["quadriceps"].append("Walking Lunge Dumbbell")

number_abs_exercises = randint(1, 2)

print("------------------- WOD -------------------")
for _ in range(number_abs_exercises):
    chosen_muscle = randint(0, len(abs_muscles) - 1)
    chosen_exercise = randint(0, len(abs_exercises[abs_muscles[chosen_muscle]]) - 1)
    for muscle, exercise in abs_exercises.items():
        if muscle == abs_muscles[chosen_muscle]:
            print(f"Exercise for {muscle} abs: {exercise[chosen_exercise]}")
    del abs_exercises[abs_muscles[chosen_muscle]][chosen_exercise]

num_exercises = randint(4, 8)

for _ in range(num_exercises):
    chosen_muscle = randint(0, len(other_muscles) - 1)
    chosen_exercise = randint(0, len(other_exercises[other_muscles[chosen_muscle]]) - 1)
    for muscle, exercise in other_exercises.items():
        if muscle == other_muscles[chosen_muscle]:
            print(f"Exercise for {muscle} : {exercise[chosen_exercise]}")
    del other_exercises[other_muscles[chosen_muscle]][chosen_exercise]
print("-------------------------------------------")