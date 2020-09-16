# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    def testAboveBoundsA(self): 
        self.assertEqual(classifyTriangle(201,4,5),'InvalidInput','201 (a) is above input threshold')

    def testAboveBoundsB(self): 
        self.assertEqual(classifyTriangle(3,201,5),'InvalidInput','201 (b) is above input threshold')
    
    def testAboveBoundsC(self): 
        self.assertEqual(classifyTriangle(3,4,201),'InvalidInput','201 (c) is above input threshold')
    
    def testUpBoundsA(self): 
        self.assertNotEqual(classifyTriangle(200,4,5),'InvalidInput','200 (a) is valid input')

    def testUpBoundsB(self): 
        self.assertNotEqual(classifyTriangle(3,200,5),'InvalidInput','200 (b) is valid input')
    
    def testUpBoundsC(self): 
        self.assertNotEqual(classifyTriangle(3,4,200),'InvalidInput','200 (c) is valid input')
    
    def testDownBoundsA(self): 
        self.assertEqual(classifyTriangle(0,4,5),'InvalidInput','0 (a) is below input threshold')

    def testDownBoundsB(self): 
        self.assertEqual(classifyTriangle(3,0,5),'InvalidInput','0 (b) is below input threshold')
    
    def testDownBoundsC(self): 
        self.assertEqual(classifyTriangle(3,4,0),'InvalidInput','0 (c) is below input threshold')
    
    def testBelowBoundsA(self): 
        self.assertEqual(classifyTriangle(-1,4,5),'InvalidInput','-1 (a) is below input threshold')

    def testBelowBoundsB(self): 
        self.assertEqual(classifyTriangle(3,-1,5),'InvalidInput','-1 (b) is below input threshold')
    
    def testBelowBoundsC(self): 
        self.assertEqual(classifyTriangle(3,4,-1),'InvalidInput','-1 (c) is below input threshold')
    
    def testNotIntA(self): 
        self.assertEqual(classifyTriangle("a",4,5),'InvalidInput','"a" (a) is not an integer')

    def testNotIntB(self): 
        self.assertEqual(classifyTriangle(3,"a",5),'InvalidInput','"a" (b) is not an integer')
    
    def testNotIntC(self): 
        self.assertEqual(classifyTriangle(3,4,"a"),'InvalidInput','"a" (c) is not an integer')
    
    def testNotTriangleA(self): 
        self.assertEqual(classifyTriangle(150,4,5),'NotATriangle','150,4,5 is not a valid triangle')

    def testNotTriangleB(self): 
        self.assertEqual(classifyTriangle(5,150,4),'NotATriangle','5,150,4 is not a valid triangle')

    def testNotTriangleC(self): 
        self.assertEqual(classifyTriangle(4,5,150),'NotATriangle','4,5,150 is not a valid triangle')
    
    def testNotTriangleThresholdA(self): 
        self.assertEqual(classifyTriangle(9,4,5),'NotATriangle','9,4,5 is not a valid triangle')

    def testNotTriangleThresholdB(self): 
        self.assertEqual(classifyTriangle(5,9,4),'NotATriangle','5,9,4 is not a valid triangle')

    def testNotTriangleThresholdC(self): 
        self.assertEqual(classifyTriangle(4,5,9),'NotATriangle','4,5,9 is not a valid triangle')
    
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def testRightTriangleC(self): 
        self.assertEqual(classifyTriangle(4,5,3),'Right','4,5,3 is a Right triangle')
    
    def testScaleneTriangles(self): 
        self.assertEqual(classifyTriangle(3,4,6),'Scalene','3,4,6 is a Scalene triangle')
    
    def testIsoscelesA(self): 
        self.assertEqual(classifyTriangle(5,4,4),'Isosceles','5,4,4 is an Isosceles triangle')

    def testIsoscelesB(self): 
        self.assertEqual(classifyTriangle(4,5,4),'Isosceles','4,5,4 is an Isosceles triangle')

    def testIsoscelesC(self): 
        self.assertEqual(classifyTriangle(4,4,5),'Isosceles','4,4,5 is an Isosceles triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

