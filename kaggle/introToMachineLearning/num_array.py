import datetime
import random

# === Tools ===
def search_web(query):
    return f"Simulated search result for: {query}"

def summarize_text(text):
    return f"Summary: {text[:50]}..."

def set_reminder(task, time):
    return f"Reminder set for '{task}' at {time}"

# === Agent Memory & Thought ===
class TaskAgent:
    def __init__(self):
        self.memory = []

    def think(self, goal):
        print(f"\n🧠 Thinking about: {goal}")
        if "search" in goal.lower():
            return self.use_tool("search", goal)
        elif "summarize" in goal.lower():
            sample_text = "This is a long article that needs to be summarized."
            return self.use_tool("summarize", sample_text)
        elif "reminder" in goal.lower():
            time = datetime.datetime.now() + datetime.timedelta(minutes=1)
            return self.use_tool("reminder", goal, time)
        else:
            return f"🤔 I don't know how to handle '{goal}' yet."

    def use_tool(self, tool_name, *args):
        print(f"🛠️ Using tool: {tool_name}")
        if tool_name == "search":
            result = search_web(args[0])
        elif tool_name == "summarize":
            result = summarize_text(args[0])
        elif tool_name == "reminder":
            result = set_reminder(args[0], args[1])
        else:
            result = "Unknown tool."
        self.memory.append((tool_name, args, result))
        return result

    def reflect(self):
        print("\n📚 Memory Log:")
        for i, (tool, args, result) in enumerate(self.memory):
            print(f"{i+1}. Tool: {tool}, Args: {args}, Result: {result}")

# === Main Loop ===
if __name__ == "__main__":
    agent = TaskAgent()
    goals = [
        "Search the weather in Boston",
        "Summarize this article about AI",
        "Set a reminder to call John",
        "Plan my workout"
    ]

    for goal in goals:
        result = agent.think(goal)
        print(f"✅ Result: {result}")

    agent.reflect()

