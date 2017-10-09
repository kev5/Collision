"""this is the main part of the assignment"""

# Copyright 2017 Keval_Khara kevalk@bu.edu
# Copyright 2017 Donato_Kava dkava@bu.edu
# Copyright 2017 Harish_NS harishns@bu.edu

import unittest
import subprocess

AUTHORS = ['kevalk@bu.edu', 'dkava@bu.edu', 'harishns@bu.edu']

PROGRAM_TO_TEST = "test_program.py"

def runprogram(program, args, inputstr):
    coll_run = subprocess.run(
        [program, *args],
        input=inputstr.encode(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)

    ret_code = coll_run.returncode
    program_output = coll_run.stdout.decode()
    program_errors = coll_run.stderr.decode()
    return (ret_code, program_output, program_errors)


class CollisionTestCase(unittest.TestCase):
    
    #checking if there are no errors for single input
    def test_one(self):
        strin = "one 20 10 -2 1"
        correct_out = "3\none 14 13 -2 1\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["3"],strin)
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")
    
    #checking if there are no errors for multiple inputs
    def test_mult_part_basic(self):
        strin = "one 20 10 -2 1\ntwo 0 0 -1 -1"
        correct_out = "3\none 14 13 -2 1\ntwo -3 -3 -1 -1\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["3"],strin)
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")        

    #checking the final values after the time of collision
    def test_post_collision(self):
        strin="one 0 0 0 0\ntwo 12 0 -2 0"
        correct_out="2\none -2 0 -2 0\ntwo 10 0 0 0\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["2"],strin)
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")

        # str1=strin[8:11]
        # str2=strin[21:29]
        # v1=[int(i) for i in str1.split()]
        # v2=[int(i) for i in str2.split()]

        # str3=strin[4:7]
        # str4=string[15:21]
        # x1=[int(i) for i in str3.split()]
        # x2=[int(i) for i in str4.split()]

    
    #checking if the program gives an error when a character passed as time constraint
    def test_input_letter(self):
        strin = "one 20 10 -2 1"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["a"],strin)
        self.assertEqual(rc,2)

    #checking if the program gives an error when no time contraint given
    def test_input_space(self):
        strin = "one 20 10 -2 1"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,[""],strin)
        self.assertEqual(rc,2) 
    
    #checking if extra characters have been entered in the input
    def test_extra(self):
        strin = "one 20 10 -2 1 1"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["3"],strin)
        self.assertEqual(rc,1)

    def test_programname(self):
        self.assertTrue(PROGRAM_TO_TEST.startswith("col"),"wrong program name")

def main():
    "show how to use runprogram"

    print(runprogram('./test_program.py', ["4", "56", "test"], "my input"))
    unittest.main()

if __name__ == '__main__':
    main()
