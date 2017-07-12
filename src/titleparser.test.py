import unittest
import titleparser

class TestTitleParser(unittest.TestCase):
    def test_isHash(self):
        self.assertTrue(titleparser.isHash('#'))
        self.assertFalse(titleparser.isHash(' '))

    def test_isSpace(self):
        self.assertTrue(titleparser.isSpace(' '))
        self.assertFalse(titleparser.isSpace('#'))

    def test_inc(self):
        self.assertEquals(titleparser.inc(1), 2)
        self.assertEquals(titleparser.inc(0), 1)
        self.assertEquals(titleparser.inc(-1), 0)

    def test_getIntentLevel(self):
        i = 0
        self.assertEquals(titleparser.getIntentLevel(i,'## test'), 2)
        self.assertEquals(titleparser.getIntentLevel(i,'# test'), 1)
        self.assertEquals(titleparser.getIntentLevel(i,'test'), 0)

    def test_removeHash(self):
        res = 'test'
        self.assertEquals(titleparser.removeHash('## test'), res)
        self.assertEquals(titleparser.removeHash('# test'), res)
        self.assertEquals(titleparser.removeHash('test'), res)

if __name__ == '__main__':
    unittest.main()