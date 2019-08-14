#!/usr/local/bin/python3

# Imports
import codepost
from helpers import parse_test_output, find_function_definition

# Set some required variables
course_name = '<COURSE NAME>'
course_period = '<COURSE PERIOD>'
assignment_name = '<ASSIGNMENT NAME>'

test_output_file = 'tests.txt'
student_code_file = 'homework.py'

codepost.configure_api_key(api_key='<YOUR API KEY>')

###################################################################################################

# try to find course
course_list = codepost.course.list_available(name=course_name, period=course_period)
if len(course_list) == 0:
    raise Exception("Couldn't find course with name %s and period %s" % (course_name, course_period))
this_course = course_list[0]

# try to find assignment
this_assignment = this_course.assignments.by_name(name=assignment_name)
if this_assignment is None:
    raise Exception("ERROR: couldn't find assignment with name %s in specified course" % (assignment_name))

# retrieve list of assignment's submissions
submissions = this_assignment.list_submissions()

# loop through submissions
for submission in submissions:

    # get files corresponding to this submission
    test_file = submission.files.by_name(name=test_output_file)
    student_code = submission.files.by_name(name=student_code_file)

    if (test_file is not None) and (student_code is not None):

        # the 'code' of the test output file is the test output
        tests_by_function = parse_test_output(test_file.code)

        # loop over the functions which were tested at least once
        for function_name in tests_by_function.keys():

            # use helper function to figure out where the function corresponding to function_name
            # was defined
            where_to_place = find_function_definition(function_name, student_code.code)

            if where_to_place is not None:

                test_text = ("  \n").join(tests_by_function[function_name])
                test_text_escaped = test_text.replace('[', '`[').replace(']', ']`')

                # construct codePost comment
                comment = {
                  'text': test_text_escaped,
                  'file': student_code.id,
                  'pointDelta': 0,
                  'rubricComment': None,
                  **where_to_place,
                }

                # post the comment to codePost
                codepost.comment.create(**comment)


