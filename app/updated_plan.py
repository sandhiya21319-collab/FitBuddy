from .ai_service import generate_text


def update_workout_plan(
    original_plan,
    feedback,
    age=None,
    goal=None,
    intensity=None,
):

    prompt = f"""
Revise the following FitBuddy 7-day workout plan
using the user's feedback.

Goal:
{goal or "not provided"}

Intensity:
{intensity or "not provided"}

Age:
{age or "not provided"}

User Feedback:
{feedback}


Original Plan:
{original_plan}


Return a complete replacement 7-day plan.

Do not return only a list of changes.

Preserve useful parts of the original plan.

Incorporate reasonable feedback.

Include recovery.

Avoid dangerous or extreme exercise.

Do not provide medical treatment.

If the user is under 18, keep recommendations
age-appropriate and encourage parent/guardian or
qualified-professional involvement.

State that this is general wellness information,
not medical advice.
"""

    return generate_text(
        prompt,
        purpose="update"
    )