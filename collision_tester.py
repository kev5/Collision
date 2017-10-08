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
    "empty class - write this"
    def test_one(self):
        strin = "one 20 10 -2 1"
        correct_out = "3\none 14 13 -2 1\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["3"],strin)
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")
    
    def test_mult_part_basic(self):
        strin = "one 20 10 -2 1\ntwo 0 0 -1 -1"
        correct_out = "3\none 14 13 -2 1\ntwo -3 -3 -1 -1\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["3"],strin)
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")        
    
#    def test_mult_col(self):  #fails 1, 7, 27
#        strin = "one 20 10 -2 1\ntwo 0 0 3 3"
#        correct_out = "3\none 14 13 -2 1\ntwo 9 9 3 3x\n"
#        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["3"],strin)
#        self.assertEqual(rc,0)
#        self.assertEqual(out,correct_out)
#        self.assertEqual(errs,"")        
    
    def input_test_letter(self):
        strin = "one 20 10 -2 1"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["a"],strin)
        self.assertEqual(rc,2)

    def input_test_space(self):
        strin = "one 20 10 -2 1"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,[""],strin)
        self.assertEqual(rc,2) 
    
    def partical_test_extra(self):
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

