import os
import json
from time import sleep
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kaha hai bhai")

client = Groq(api_key=my_api_key)

MODEL = "openai/gpt-oss-20b"


# -----------------------------
# Your actual Python tools
# -----------------------------

def get_product_price(product: str):
    """
    Get the price of a product.
    """
    if product == "iPhone 17":
        return 1000
    elif product == "iPhone 15":
        return 500
    else:
        return 0


def calculator(expression: str):
    """
    Calculate an arithmetic expression.
    """
    try:
        # Demo only. Don't use eval() with untrusted input.
        return eval(expression, {"__builtins__": {}}, {})
    except Exception:
        return "calc error!"


tools_map = {
    "get_product_price": get_product_price,
    "calculator": calculator
}


# -----------------------------
# Tool schemas
# -----------------------------

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_product_price",
            "description": "Get the price of a product.",
            "parameters": {
                "type": "object",
                "properties": {
                    "product": {
                        "type": "string",
                        "description": "Name of the product"
                    }
                },
                "required": ["product"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Calculate an arithmetic expression.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "Arithmetic expression such as 5000 - 1000"
                    }
                },
                "required": ["expression"]
            }
        }
    }
]


system_prompt = """
You are a shopping assistant.

You have access to these tools:

1. get_product_price(product)
2. calculator(expression)

Use the tools whenever necessary.

For example:
- To find an iPhone price, use get_product_price.
- To subtract the price from a budget, use calculator.

Do not invent tool results.

After receiving tool results, give the user the final answer.
"""


def run_agent(question):

    messages = [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": question
        }
    ]

    for step in range(5):

        print("\n------------------")
        print("STEP", step + 1)
        print("------------------")

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=tools,
            tool_choice="auto",
            parallel_tool_calls=False,
            temperature=0
        )

        assistant_message = response.choices[0].message

        print("Assistant:", assistant_message.content)

        # Add assistant response to conversation
        messages.append(assistant_message)

        # -----------------------------
        # Check for native tool calls
        # -----------------------------

        if assistant_message.tool_calls:

            for tool_call in assistant_message.tool_calls:

                tool_name = tool_call.function.name

                arguments = json.loads(
                    tool_call.function.arguments
                )

                print("Tool:", tool_name)
                print("Arguments:", arguments)

                if tool_name in tools_map:

                    tool_function = tools_map[tool_name]

                    observation = tool_function(**arguments)

                else:
                    observation = "Tool not found"

                print("Observation:", observation)

                # Send tool result back
                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": str(observation)
                    }
                )

            sleep(1)
            continue

        # -----------------------------
        # No tool call = final answer
        # -----------------------------

        print("\nFINAL:", assistant_message.content)
        break


prompt = """
I have 5000 rupees.
What is the price of an iPhone 17?
And how much money will I have left?
"""

run_agent(prompt)