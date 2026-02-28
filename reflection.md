# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").


The game looked simple enough when I first ran it. 4 bugs I found where the following.

1. The game consistently tells me I should guess lower even when I pick the lower bound for each difficulty. 
2. Attempts left shows -1 instead of 0 when I run out of attempts to guess. This is only true when show hint is selected. 
3. When I press new game it does not refresh the session, the UI changes but I can't guess unless I refresh the page. 
4. I am able to select numbers out of range, there should be a warning that I am out of range instead of executing. 
5. It sometimes tells me to go higher even though I am inputting a number bigger then the top end of the range, so there seems to be a disconnect between the UI and game logic. 



2 Issues I am selecting to fix are the following. 
1. The UI logic not connected to the game logic
  - Adding in bounds for lower and upper guesses without executing
  - Fixing the hint logic to proper tell the user go lower or higher 
  - Fixing the inconsistecy between the show hint selected which is issue 2
2. Refreshing the game when I click New Game

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).


LLM of choice: Claude

BugFix 1: check_int not returning the right message
AI was able to succesfully find the bug on where the messages was backwards. When it should say go higher the function was returning go lower and vice versa. When I had it make unit tests, it went overboard and stated testing edge cases that are duplicated logic of the other tests. In the eyes of AI these are legit edge cases that could happen, however if the function is written the correct way you it should not be treated as edge cases. So we refactored the function to ensure those edge cases does not exist as an input. Such as entering out of bounds. 

BugFix 2: Difficulty selection issue
When selecting difficulty the range still stays the same even though from looking a the logic from get_range_for_difficulty it should change. One mistake the LLM made is that after I made the comment which function to look at it only considered that function and did not see how it is used in app.py for the actual error. While the helper funciton is correct the usecase is wrong and that is where the bug was. I prompted it to look for it by tracing the useage of the function and plan a fix. 



---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

I decided to test if a bug was really fix by first writing the unit tests for it and then validating it on the UI with the propper flow and what I expected. I repeated this for all bugs. I even did it in parrell by having cladue run the unit tests while I validated on the UI and then came back to read the terminal message. 

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

The code needs to check if the secret exists before generating a new one and overiding it. So we added if the secret is not in the state already then we generate a new one. 

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.


I liked using plan mode to review the thought process before having the LLM make changes to my codebase. It helps me understand the changes much better and results in a faster approval process.