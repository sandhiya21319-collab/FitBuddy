from .ai_service import generate_text


def generate_workout_gemini(
    name,
    age,
    weight,
    goal,
    intensity,
):

    prompt = f"""
You are FitBuddy, a safety-conscious fitness
planning assistant.

Create a practical, beginner-friendly 7-day
fitness plan for this profile:

Name: {name}

Age: {age}

Weight: {weight} kg

Goal: {goal}

Intensity: {intensity}


Return plain text with exactly 7 day sections.

For every day include:

- Focus
- Warm-up (5–10 minutes)
- Main workout
- Exercise names
- Sets/repetitions OR duration
- Rest/recovery guidance
- Cool-down


Include at least one recovery/rest-focused day.

Avoid dangerous, extreme or medically prescriptive
advice.

Do not recommend:

- Starvation
- Dehydration
- Unsafe supplements
- Extreme weight-loss practices


If the user is a minor, keep the plan age-appropriate
and encourage involving a parent/guardian or qualified
professional for individualized guidance.

State that this is general wellness information,
not medical advice.
"""

    return generate_text(
        prompt,
        purpose="workout"
    )