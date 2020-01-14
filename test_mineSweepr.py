import unittest
import io
import sys
from mineSweeper import MineSweeper

class test_MineSweeper(unittest.TestCase):
    def setUp(self):
        #given - given for all tests.
        self.game = MineSweeper()
        self.game.createField(3, 3)

    def test_createField(self):
        #given - setUp

        #when
        field= self.game.field

        #then
        self.assertEqual( field , [['.','.','.'],['.','.','.'],['.','.','.']])

    def test_layMine(self):
        #given - setUp

        #when
        self.game.layMine(0,0)

        #then
        self.assertEqual(self.game.field, [['*', '.', '.'], ['.', '.', '.'], ['.', '.', '.']])



    def test_printField(self):
        #given - setUp and capture output methods:
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        #when
        self.game.printField()

        #then
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(),'". . ."\n". . ."\n". . ."\n')



    def test_play_hit_mine(self):
        #given - setUp
        self.game.layMine(0, 0)

        #when
        self.game.play(0,0)

        #then
        self.assertEqual(self.game.fieldToPrint, [['*', '.', '.'], ['.', '.', '.'], ['.', '.', '.']])



    def test_play_hit_near_mine(self):
        #given - setUp
        self.game.layMine(0, 0)

        #when
        self.game.play(0, 2)

        #then
        self.assertEqual(self.game.fieldToPrint, [['*', '1', '+'], ['1', '1', '+'], ['+', '+', '+']])


    def test_status_PLAYING(self):
        #given - setUp
        self.game.layMine(0, 0)
        self.game.layMine(1, 1)

        #when
        self.game.play(2,2)


        #then
        self.assertEqual(self.game.status() , "PLAYING")

    def test_status_LOST(self):
        # given - setUp
        self.game.layMine(0, 0)
        self.game.layMine(1, 1)

        #when
        self.game.play(1,1)

        #then
        self.assertEqual(self.game.status(), "LOST")

    def test_status_WIN(self):
        # given - setUp
        self.game.layMine(0, 1)
        self.game.layMine(1, 0)
        self.game.layMine(2, 1)
        self.game.layMine(1, 2)

        #when
        self.game.play(0,0)
        self.game.play(1, 1)
        self.game.play(2, 2)
        self.game.play(0, 2)
        self.game.play(2, 0)

        #then
        self.assertEqual(self.game.status(), "WIN")






if __name__ == '__main__':
    unittest.main()

