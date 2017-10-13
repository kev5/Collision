# Copyright 2017 Harish N Sathishchandra harishns@bu.edu
# Copyright 2017 Keval Khara kevalk@bu.edu
# Copyright 2017 Donato Kava dkava@bu.edu
import unittest
import subprocess

AUTHORS = ['harishns@bu.edu', 'kevalk@bu.edu', 'dkava@bu.edu']

PROGRAM_TO_TEST = "test_program.py"

def runprogram(program, args, inputstr):
    coll_run = subprocess.run(
        [program, *args],timeout=1,
        input=inputstr.encode(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)

    ret_code = coll_run.returncode
    program_output = coll_run.stdout.decode()
    program_errors = coll_run.stderr.decode()
    return (ret_code, program_output, program_errors)


class CollisionTestCase(unittest.TestCase):
    
    #checking if there are no errors for two inputs
    def test_two(self):
        strin = "one 1 0 1 0\ntwo 200 200 1 1"
        correct_out = "1.26\none 2.26 0 1 0\ntwo 201.26 201.26 1 1\n4.5\none 5.5 0 1 0\ntwo 204.5 204.5 1 1\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["4.5","1.26","-4.5"],strin)
        try:
            self.assertEqual(rc,0)
            self.assertEqual(errs,"")
            if out == "1.26\none 2.26 0 1 0\ntwo 201.26 201.26 1 1\n4.5\none 5.5 0 1 0\ntwo 204.5 204.5 1 1\n":
                self.assertEqual(out,correct_out)
            elif out == "1.2600\none 2.26 0 1 0\ntwo 201.26 201.26 1 1\n4.5000\none 5.5 0 1 0\ntwo 204.5 204.5 1 1\n":
                out = correct_out
                self.assertEqual(out,correct_out)
            else:
                self.assertEqual(out,correct_out)
        except subprocess.TimeoutExpired:
            out = "1"
            correct_out = "2"
            self.assertEqual(out,correct_out)
     
    #checking if there are no errors for single input  
    def test_one(self):
        strin = "one 1 0 1 0"
        correct_out = "1.26\none 2.26 0 1 0\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["1.26"],strin)
        self.assertEqual(rc,0)
        self.assertEqual(errs,"")
        if out == "1.26\none 2.26 0 1 0\n":
            self.assertEqual(out,correct_out)
        elif out == "1.2600\none 2.26 0 1 0\n":
            out = correct_out
            self.assertEqual(out,correct_out)
        else:
            self.assertEqual(out,correct_out)
   
    #checking if there are no errors for multiple inputs
    def test_mult_part_basic(self):
        strin = "one 20 10 -2 1\ntwo 0 0 -1 -1"
        correct_out = "3\none 14 13 -2 1\ntwo -3 -3 -1 -1\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["3"],strin)
        try:
            self.assertEqual(rc,0)
            self.assertEqual(errs,"")
            if out == "3\none 14 13 -2 1\ntwo -3 -3 -1 -1\n":
                self.assertEqual(out,correct_out)
            elif out == "3.0000\none 14 13 -2 1\ntwo -3 -3 -1 -1\n":
                out = correct_out
                self.assertEqual(out,correct_out)
            else:
                self.assertEqual(out,correct_out)
        except subprocess.TimeoutExpired:
            out = "1"
            correct_out = "2"
            self.assertEqual(out,correct_out)

    #checking if a character as time input gives error
    def test_input_letter(self):
        strin = "one 20 10 -2 1"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["a"],strin)
        self.assertEqual(rc,2)

    #checking if a space as time input gives error    
    def test_input_test_space(self):
        strin = "one 20 10 -2 1"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,[" "],strin)
        self.assertEqual(rc,2) 
   
   #checking if a character as input gives error
    def test_particle_test_extra(self):
        strin = "one 20 10 -2 a"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["1"],strin)
        self.assertEqual(rc,1)

    #checking if the positions after collision are correct (only x axis)  
    def test_pos_after_collision_x(self):
        strin = "one 0 0 1 0\ntwo 12 0 -1 0"
        correct_out = "2\none 0 0 -1 0\ntwo 12 0 1 0\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["2"],strin)
        try:
            self.assertEqual(rc,0)
            self.assertEqual(errs,"")
            if out == "2\none 0 0 -1 0\ntwo 12 0 1 0\n":
                self.assertEqual(out,correct_out)
            elif out == "2.0000\none 0 0 -1 0\ntwo 12 0 1 0\n":
                out = correct_out
                self.assertEqual(out,correct_out)
            else:
                self.assertEqual(out,correct_out)
        except subprocess.TimeoutExpired:
            out = "1"
            correct_out = "2"
            self.assertEqual(out,correct_out)
    
    #position 0
    def test_pos_0(self):
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,[""],"")
        try:
            self.assertEqual(rc,2)
            self.assertEqual(errs,"")
        except subprocess.TimeoutExpired:
            self.assertEqual(rc,2)
            self.assertEqual(errs,"")
    
    #checking the position of still particle    
    def test_pos_after_collision(self):
        strin = "one 3 0 0 0"
        correct_out = "0\none 3 0 0 0\n3\none 3 0 0 0\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["0","3"],strin)
        try:
            self.assertEqual(rc,0)
            self.assertEqual(errs,"")
            if out == "0\none 3 0 0 0\n3\none 3 0 0 0\n":
                self.assertEqual(out,correct_out)
            elif out == "0.0000\none 3 0 0 0\n3.0000\none 3 0 0 0\n":
                out = correct_out
                self.assertEqual(out,correct_out)
            else:
                self.assertEqual(out,correct_out)
        except subprocess.TimeoutExpired:
            out = "1"
            correct_out = "2"
            self.assertEqual(out,correct_out)

    #checking if the positions after collision are correct
    def test_pos_after_collision_x_y(self):
        strin = "one 2 2 1 1\ntwo 12 10 -1 -1"
        correct_out = "2\none 1.76 2.32 -1.24 -0.68\ntwo 12.24 9.68 1.24 0.68\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["2"],strin)
        try:
            self.assertEqual(rc,0)
            self.assertEqual(errs,"")
            if out == "2\none 1.76 2.32 -1.24 -0.68\ntwo 12.24 9.68 1.24 0.68\n":
                self.assertEqual(out,correct_out)
            elif out == "2.0000\none 1.76 2.32 -1.24 -0.68\ntwo 12.24 9.68 1.24 0.68\n":
                out = correct_out
                self.assertEqual(out,correct_out)
            else:
                self.assertEqual(out,correct_out)
        except subprocess.TimeoutExpired:
            out = "1"
            correct_out = "2"
            self.assertEqual(out,correct_out)

    #checking the positions after collision of 3 particles
    def test_pos_after_collision_3_part(self):
        strin = "one 1 0 3 0\ntwo 15 0 -1 0\nthree 27 0 1 0"
        correct_out = "1\none 4 0 3 0\ntwo 14 0 -1 0\nthree 28 0 1 0\n4\none 1 0 -1 0\ntwo 21 0 1 0\nthree 33 0 3 0\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["4","1"],strin)
        try:
            self.assertEqual(rc,0)
            self.assertEqual(errs,"")
            if out == "1\none 4 0 3 0\ntwo 14 0 -1 0\nthree 28 0 1 0\n4\none 1 0 -1 0\ntwo 21 0 1 0\nthree 33 0 3 0\n":
                self.assertEqual(out,correct_out)
            elif out == "1.0000\none 4 0 3 0\ntwo 14 0 -1 0\nthree 28 0 1 0\n4.0000\none 1 0 -1 0\ntwo 21 0 1 0\nthree 33 0 3 0\n":
                out = correct_out
                self.assertEqual(out,correct_out)
            else:
                self.assertEqual(out,correct_out)
        except subprocess.TimeoutExpired:
            out = "1"
            correct_out = "2"
            self.assertEqual(out,correct_out)
    
    #checking 2 collisions
    def test_collision_then_Anothercollision_fixed(self):
        strin = "one 0 0 1 0\ntwo 12 0 -1 0\nthree 24 0 0 0"
        correct_out = "6\none -4 0 -1 0\ntwo 14 0 0 0\nthree 26 0 1 0\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["6"],strin)
        try:
            self.assertEqual(rc,0)
            self.assertEqual(errs,"")
            if out == "6\none -4 0 -1 0\ntwo 14 0 0 0\nthree 26 0 1 0\n":
                self.assertEqual(out,correct_out)
            elif out == "6.0000\none -4 0 -1 0\ntwo 14 0 0 0\nthree 26 0 1 0\n":
                out = correct_out
                self.assertEqual(out,correct_out)
            else:
                self.assertEqual(out,correct_out)
        except subprocess.TimeoutExpired:
            out = "1"
            correct_out = "2"
            self.assertEqual(out,correct_out)
      
    #big value of time as input  
    def test_big_time(self):
        strin = "one 0 0 1 0"
        correct_out = "100000\none 100000 0 1 0\n100001\none 100001 0 1 0\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["100000","100001"],strin)
        try:
            self.assertEqual(rc,0)
            self.assertEqual(errs,"") 
            if out == "100000\none 100000 0 1 0\n100001\none 100001 0 1 0\n":
                self.assertEqual(out,correct_out)
            elif out == "100000.0000\none 100000 0 1 0\n100001.0000\none 100001 0 1 0\n":
                out = correct_out
                self.assertEqual(out,correct_out)
            else:
                self.assertEqual(out,correct_out)
        except subprocess.TimeoutExpired:
            out = "1"
            correct_out = "2"
            self.assertEqual(out,correct_out)
         
    #checking the precision   
    def test_precision(self):
        strin = "one 1.00000121 0 1.00000121 0"
        correct_out = "3.25\none 4.2500051 0 1.0000012 0\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["3.25"],strin)
        try:
            self.assertEqual(rc,0)
            self.assertEqual(errs,"") 
            if out == "3.25\none 4.2500051 0 1.0000012 0\n":
                self.assertEqual(out,correct_out)
            elif out == "3.2500\none 4.2500051 0 1.0000012 0\n":
                out = correct_out
                self.assertEqual(out,correct_out)
            else:
                self.assertEqual(out,correct_out)
        except subprocess.TimeoutExpired:
            out = "1"
            correct_out = "2"
            self.assertEqual(out,correct_out)
         
    #checking the angular collision  
    def test_angular(self):
        strin = "one 8 0 0 0\ntwo -1.93 8.07 1 -1"
        correct_out = "2\none 8.0107338 -0.0082192519 1.1130814 -0.85232263\ntwo 0.059266158 6.0782193 -0.11308137 -0.14767737\n1000\none 1118.8659 -850.62621 1.1130814 -0.85232263\ntwo -112.79594 -141.30379 -0.11308137 -0.14767737\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["2","1000"],strin)
        self.assertEqual(rc,0)
        if out == "2\none 8.0107338 -0.0082192519 1.1130814 -0.85232263\ntwo 0.059266158 6.0782193 -0.11308137 -0.14767737\n1000\none 1118.8659 -850.62621 1.1130814 -0.85232263\ntwo -112.79594 -141.30379 -0.11308137 -0.14767737\n":
            self.assertEqual(out,correct_out)
        elif out == "2.0000\none 8.0107338 -0.0082192519 1.1130814 -0.85232263\ntwo 0.059266158 6.0782193 -0.11308137 -0.14767737\n1000.0000\none 1118.8659 -850.62621 1.1130814 -0.85232263\ntwo -112.79594 -141.30379 -0.11308137 -0.14767737\n":
            out = correct_out
            self.assertEqual(out,correct_out)
        else:
            self.assertEqual(out,correct_out)
       
    #giving 11 particles as input         
    def test_eleven(self):
        strin = "one 10 0 1 0\ntwo 21 0 0 0\nthree 32 0 0 0\nfour 47 0 -1 0\nfive 0 0 0 0\nsix 0 11 0 -1\nseven 0 -11 0 1\neight 0 -22 0 2\nnine 100 100 1 1\nten 111 111 1 1\neleven 200 200 1 1"
        correct_out = "1\none 11 0 1 0\ntwo 21 0 0 0\nthree 32 0 0 0\nfour 46 0 -1 0\nfive 0 0 0 0\nsix 0 10 0 -1\nseven 0 -10 0 1\neight 0 -20 0 2\nnine 101 101 1 1\nten 112 112 1 1\neleven 201 201 1 1\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["1"],strin)
        try:
            self.assertEqual(rc,0)
            self.assertEqual(errs,"") 
            if out == "1\none 11 0 1 0\ntwo 21 0 0 0\nthree 32 0 0 0\nfour 46 0 -1 0\nfive 0 0 0 0\nsix 0 10 0 -1\nseven 0 -10 0 1\neight 0 -20 0 2\nnine 101 101 1 1\nten 112 112 1 1\neleven 201 201 1 1\n":
                self.assertEqual(out,correct_out)
            elif out == "1.0000\none 11 0 1 0\ntwo 21 0 0 0\nthree 32 0 0 0\nfour 46 0 -1 0\nfive 0 0 0 0\nsix 0 10 0 -1\nseven 0 -10 0 1\neight 0 -20 0 2\nnine 101 101 1 1\nten 112 112 1 1\neleven 201 201 1 1\n":
                out = correct_out
                self.assertEqual(out,correct_out)
            else:
                self.assertEqual(out,correct_out)
        except subprocess.TimeoutExpired:
            out = "1"
            correct_out = "2"
            self.assertEqual(out,correct_out)
     
    #complicated input values           
    def test_complex(self):
        strin="2MU133 -34.94 -69.13 0.468 -0.900\n0WI913 -43.08 92.12 -0.811 -0.958\n6UP738  2.97 -66.25 -0.077 0.074\n1IA244 72.94 -86.02 -0.665 -0.283\n8RT773 -32.25 -2.63 -0.797 0.628\n0HV350 -73.97 24.21 0.960 -0.870\n0DU118 -82.09 44.95 0.661 -0.343\n4FA522 -18.20 72.32 0.734 -0.990\n1WR684 31.71 68.89 -0.509 -0.706\n7SW673 41.29 42.68 0.549 -0.012"
        correct_out = "10\n2MU133 -30.26 -78.13 0.468 -0.9\n0WI913 -51.19 82.54 -0.811 -0.958\n6UP738 2.2 -65.51 -0.077 0.074\n1IA244 66.29 -88.85 -0.665 -0.283\n8RT773 -40.22 3.65 -0.797 0.628\n0HV350 -64.37 15.51 0.96 -0.87\n0DU118 -75.48 41.52 0.661 -0.343\n4FA522 -10.86 62.42 0.734 -0.99\n1WR684 26.62 61.83 -0.509 -0.706\n7SW673 46.78 42.56 0.549 -0.012\n50\n2MU133 -11.54 -114.13 0.468 -0.9\n0WI913 -83.63 44.22 -0.811 -0.958\n6UP738 -0.88 -62.55 -0.077 0.074\n1IA244 39.69 -100.17 -0.665 -0.283\n8RT773 -16.981282 29.905421 0.92840971 0.66354266\n0HV350 -81.088718 -20.425421 -0.76540971 -0.90554266\n0DU118 -49.04 27.8 0.661 -0.343\n4FA522 8.2965691 14.806549 0.1031531 -1.4854472\n1WR684 16.463431 41.603451 0.1218469 -0.21055284\n7SW673 68.74 42.08 0.549 -0.012\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["10", "50"],strin)
        try:
            self.assertEqual(rc,0)
            self.assertEqual(errs,"") 
            if out == "10\n2MU133 -30.26 -78.13 0.468 -0.9\n0WI913 -51.19 82.54 -0.811 -0.958\n6UP738 2.2 -65.51 -0.077 0.074\n1IA244 66.29 -88.85 -0.665 -0.283\n8RT773 -40.22 3.65 -0.797 0.628\n0HV350 -64.37 15.51 0.96 -0.87\n0DU118 -75.48 41.52 0.661 -0.343\n4FA522 -10.86 62.42 0.734 -0.99\n1WR684 26.62 61.83 -0.509 -0.706\n7SW673 46.78 42.56 0.549 -0.012\n50\n2MU133 -11.54 -114.13 0.468 -0.9\n0WI913 -83.63 44.22 -0.811 -0.958\n6UP738 -0.88 -62.55 -0.077 0.074\n1IA244 39.69 -100.17 -0.665 -0.283\n8RT773 -16.981282 29.905421 0.92840971 0.66354266\n0HV350 -81.088718 -20.425421 -0.76540971 -0.90554266\n0DU118 -49.04 27.8 0.661 -0.343\n4FA522 8.2965691 14.806549 0.1031531 -1.4854472\n1WR684 16.463431 41.603451 0.1218469 -0.21055284\n7SW673 68.74 42.08 0.549 -0.012\n":
                self.assertEqual(out,correct_out)
            elif out == "10.0000\n2MU133 -30.26 -78.13 0.468 -0.9\n0WI913 -51.19 82.54 -0.811 -0.958\n6UP738 2.2 -65.51 -0.077 0.074\n1IA244 66.29 -88.85 -0.665 -0.283\n8RT773 -40.22 3.65 -0.797 0.628\n0HV350 -64.37 15.51 0.96 -0.87\n0DU118 -75.48 41.52 0.661 -0.343\n4FA522 -10.86 62.42 0.734 -0.99\n1WR684 26.62 61.83 -0.509 -0.706\n7SW673 46.78 42.56 0.549 -0.012\n50.0000\n2MU133 -11.54 -114.13 0.468 -0.9\n0WI913 -83.63 44.22 -0.811 -0.958\n6UP738 -0.88 -62.55 -0.077 0.074\n1IA244 39.69 -100.17 -0.665 -0.283\n8RT773 -16.981282 29.905421 0.92840971 0.66354266\n0HV350 -81.088718 -20.425421 -0.76540971 -0.90554266\n0DU118 -49.04 27.8 0.661 -0.343\n4FA522 8.2965691 14.806549 0.1031531 -1.4854472\n1WR684 16.463431 41.603451 0.1218469 -0.21055284\n7SW673 68.74 42.08 0.549 -0.012\n":
                out = correct_out
                self.assertEqual(out,correct_out)
            else:
                self.assertEqual(out,correct_out)
        except subprocess.TimeoutExpired:
            out = "1"
            correct_out = "2"
            self.assertEqual(out,correct_out) 

    #4 particles collision
    def test_four_3(self):
        strin = "one 0 0 0 0\ntwo 11 0 -1 0\nthree 0 11 0 -1\nfour -11 0 1 0"
        correct_out = "1\none 0 0 0 0\ntwo 10 0 -1 0\nthree 0 10 0 -1\nfour -10 0 1 0\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["1"],strin)
        try:
            self.assertEqual(rc,0)
            self.assertEqual(errs,"") 
            if out == "1\none 0 0 0 0\ntwo 10 0 -1 0\nthree 0 10 0 -1\nfour -10 0 1 0\n":
                self.assertEqual(out,correct_out)
            elif out == "1.0000\none 0 0 0 0\ntwo 10 0 -1 0\nthree 0 10 0 -1\nfour -10 0 1 0\n":
                out = correct_out
                self.assertEqual(out,correct_out)
            else:
                self.assertEqual(out,correct_out)
        except subprocess.TimeoutExpired:
            out = "1"
            correct_out = "2"
            self.assertEqual(out,correct_out)
            
    #giving 2 particles the same ID
    def test_double_id(self):
        strin = "one 1 0 1 0\none 20 0 -1 0"
        correct_out = "1\none 2 0 1 0\none 19 0 -1 0\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["1"],strin)
        try:
            self.assertEqual(rc,0)
            self.assertEqual(errs,"") 
            if out == "1\none 2 0 1 0\none 19 0 -1 0\n":
                self.assertEqual(out,correct_out)
            elif out == "1.0000\none 2 0 1 0\none 19 0 -1 0\n":
                out = correct_out
                self.assertEqual(out,correct_out)
            else:
                self.assertEqual(out,correct_out)
        except subprocess.TimeoutExpired:
            out = "1"
            correct_out = "2"
            self.assertEqual(out,correct_out)
      
    #empty input               
    def test_empty(self):
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,[""],"")
        try:
            self.assertEqual(rc,2)
            self.assertEqual(errs,"") 
            self.assertEqual(out,"")
        except subprocess.TimeoutExpired:
            out = "1"
            correct_out = "2"
            self.assertEqual(out,correct_out)
        
    def test_programname(self):
        self.assertTrue(PROGRAM_TO_TEST.startswith("col"),"wrong program name")

def main():
    "show how to use runprogram"
    print(runprogram('./test_program.py', ["4", "56", "test"], "my input"))
    unittest.main()

if __name__ == '__main__':
    main()
