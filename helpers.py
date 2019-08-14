###################################################################################################
# Helper functions used to help programatically place comments on submissions via the codePost API
###################################################################################################

import re

def parse_test_output(text):
  """
  Input: contents of an automated test script with tests of the form shown in the example
  tests.txt file in this repo

  Output: key-value map in which
    - key = function name
    - value = list of strings corresponds to tests run on that function.
  """

  # indicates start of test output
  regexp = re.compile(r'Test \d')

  LINES_IN_TEST = 6
  tests = {}
  linesSearched = 0

  lines_of_output = text.split('\n')

  while linesSearched < len(lines_of_output):
    line = lines_of_output[linesSearched]

    # does this line correspond to the start of a test?
    if regexp.search(line):

      # Capture the contents of this test
      test = "  \n".join(lines_of_output[linesSearched:linesSearched+LINES_IN_TEST])

      # what function does this test correspond to?
      # function specified on line 1 of the test output
      functionName = re.sub(r'Function: ', '', lines_of_output[linesSearched+1])

      # store in value array with function name as key
      if functionName in tests:
        tests[functionName].append(test)
      else:
        tests[functionName] = [test]

      # we just captured the whole test
      linesSearched += LINES_IN_TEST
    else:
      # continue scanning
      linesSearched += 1

  return tests

def find_function_definition(function_name, code):
  """
  Search student code for the definition of a function named function_name.
  If found, return where the function definition starts and ends (line and char).
  Else, return None.
  """
  lines = code.split('\n')

  # search for a Python function definition
  stringToFind = 'def %s' % (function_name)

  for index, line in enumerate(lines):
    startChar = line.find(stringToFind)

    # if we found the string corresponding to the right function definition
    if startChar > -1:
      return {
        'startChar': startChar,
        'endChar' : startChar + len(stringToFind),
        'startLine': index,
        'endLine': index,
      }

  # couldn't find the function definition
  return None

###################################################################################################