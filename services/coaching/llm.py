from services.config.workout_config import PROMPT


class LLMCoach:
    def __init__(self, client):
        self.client = client
        self.history = []
        self.system_prompt = PROMPT

    def give_feedback(self, event, issue):
        prompt = f"Event: {event}"

        if issue:
            prompt += f"Form Issue: {issue}"

        messages = [
            {
                "role": "system",
                "content": self.system_prompt
            },
            *self.history[-10: ],
            {
                "role": "user",
                "content": prompt
            }
        ]

        response = self.client.chat.completions.create(
            model="nvidia/nemotron-3-ultra-550b-a55b:free",
            messages=messages,
            temperature=0.4
        )

        text = response.choise[0].message.content.strip()

        self.history.append({
            "role": "assistant",
            "content": text
        })

        return text