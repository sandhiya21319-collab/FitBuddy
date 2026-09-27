from .ai_service import generate_text


def generate_nutrition_tip_with_flash(
    goal,
    age=None,
):

    prompt = f"""
Give one concise, practical nutrition or recovery
tip for a person whose fitness goal is:

Goal: {goal}

Age: {
    age if age is not None
    else "not provided"
}


Focus on:

- Balanced meals
- Hydration
- Sleep
- Recovery
- Sustainable habits


Do not prescribe:

- Calorie restriction
- Fasting
- Supplements
- Weight-loss targets


If the person is under 18, avoid dieting advice
and emphasize balanced nutrition and support from
a parent/guardian or qualified professional.

Keep the response under 100 words.

State that this is general wellness information.
"""

    return generate_text(
        prompt,
        purpose="nutrition"
    )