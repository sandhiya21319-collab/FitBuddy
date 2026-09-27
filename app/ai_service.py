def generate_workout_plan(name, age, weight, goal, intensity):

    plan = f"""
7-Day Personalized Workout Plan

User: {name}
Age: {age}
Weight: {weight} kg
Goal: {goal}
Intensity: {intensity}

Day 1 - Full Body Workout
• Warm-up: 5-10 minutes
• Squats: 3 sets × 12 reps
• Push-ups: 3 sets × 10 reps
• Lunges: 3 sets × 10 reps
• Plank: 3 sets × 30 seconds
• Cool-down: 5 minutes

Day 2 - Lower Body
• Warm-up: 5-10 minutes
• Bodyweight Squats: 3 × 15
• Lunges: 3 × 12
• Glute Bridges: 3 × 15
• Calf Raises: 3 × 15
• Stretching: 5 minutes

Day 3 - Cardio & Core
• Jumping Jacks: 3 × 30 seconds
• High Knees: 3 × 30 seconds
• Mountain Climbers: 3 × 20
• Bicycle Crunches: 3 × 15
• Plank: 3 × 30 seconds

Day 4 - Active Recovery
• Light walking: 20-30 minutes
• Full body stretching
• Breathing exercises

Day 5 - Upper Body
• Push-ups: 3 × 10
• Shoulder Taps: 3 × 12
• Triceps Dips: 3 × 10
• Superman: 3 × 12
• Plank: 3 × 30 seconds

Day 6 - Full Body
• Squats: 3 × 15
• Lunges: 3 × 10
• Push-ups: 3 × 10
• Mountain Climbers: 3 × 20
• Plank: 3 × 40 seconds

Day 7 - Rest Day
• Complete rest
• Light stretching
• Stay hydrated

Nutrition Tips
• Drink sufficient water.
• Include protein-rich foods.
• Eat fresh fruits and vegetables.
• Avoid excessive processed food.
• Maintain a balanced diet.

Safety
• Start slowly.
• Maintain correct exercise form.
• Stop if you experience pain or dizziness.
"""

    return plan.strip()