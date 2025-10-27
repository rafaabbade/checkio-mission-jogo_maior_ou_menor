"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        
    {
        "input": [103, [1000, 1, 500, 200, 100, 110, 105, 103]],
        "answer": ["menor", "maior", "menor", "menor", "maior", "menor", "menor", "correto"]
    },
    {
        "input": [10000, [10000]],
        "answer": ["correto"]
    },
    {
        "input": [-2, [0, -1, -2]],
        "answer": ["menor", "menor", "correto"]
    }

    ]
}
