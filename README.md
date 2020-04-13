# Toy-Problems
Create a repo, with the README.md initialized on GitHub. Name the repo as toy-problems. Add your mentor to this repo as a collaborator. Any practice problems that you practice can be part of this repo.
Now create a branch lru-cache in the toy-problems repo. Start developing python code for the LRU cache problem.
Begin by creating a python class. The class should be a constructor to initialize the properties of the LRU object. Think about what properties are required. Then complete the constructor.
This is a good time to commit and the commit message could be to “add constructor for LRU”.
Next, think about what public methods should be provided to anyone who is using your LRU object.
I can think of 3 methods, put, get and get_cache (not really required but this is useful for testing as you will see below).
Think about the method signatures and then create blank methods. Don’t complete the method logic yet.
To keep the program from failing with syntax errors, you could write a pass python statement after the method signature.
Another good time to commit and I’ll let you decide the commit message.
Next step is to write a class for testing the LRU object.
So, a general convention is to write LRUTest. In this test class you will import LRU, set up test cases for all the public methods to ensure that they work as expected.
Writing the test cases before completing the logic for the put, get and get_cache methods. This is part of the test first development strategy.
In the main method, create an object of LRU, and design test cases to verify the correctness of put, get and get_cache methods. Verify for all the test cases if the return values match with the expected results using assert.
If your test program returns with no errors then your tests have passed otherwise you will see the error messages.
At this stage, as there is no logic in LRU, your test cases will fail. Your strategy now is to write the logic so that the test cases pass.