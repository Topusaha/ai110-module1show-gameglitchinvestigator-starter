## Guide for Students

Step 1
Have AI look through the codebase the understand the core logic one layer at a time and starting at the core logic. Undestand what the 3 helper methods are doing and how they fit together and in what order to understand the game before moving forward

Step 2
Go through the application to see bugs and jot down in the format action, result, expected result. 

Step 3
Have Ai be in plan mode and have feed it your bugs to have it trace the codebase, also give it instructions on how to trace as well if you know or think you know where the bug is. 

Step 4
Review plana and fix

Step 5
Write unit tests with the same format of action and expected results by feeding that to your LLM.

Step 6
Verify on the UI your expected results is true and all unit tests are passing.