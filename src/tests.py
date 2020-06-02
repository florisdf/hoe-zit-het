"""Script with unit tests for Hoe Zit Het?"""
import unittest
from subprocess import Popen, PIPE


class TestCase(unittest.TestCase):
    """
    General test case for Hoe Zit Het?
    """
    def test_no_unwanted_newline_after_mute(self):
        """
        Check if there are no %-mute shortcodes at the end of a line
        This will result in an unwanted newline character after the muted text
        """
        process = Popen(['grep', '-rl', '{{% mute "[^"]*" %}}$', 'content/lessen'], stdout=PIPE)
        (output, _) = process.communicate()

        out = output.decode('utf-8')
        msg = ('Unwanted newline characters at mute '
               'shortcode in\n' + out)
        self.assertEqual(out, '', msg=msg)

if __name__ == '__main__':
    unittest.main()
