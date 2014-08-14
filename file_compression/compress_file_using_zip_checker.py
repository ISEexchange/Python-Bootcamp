#!/usr/bin/python

from cStringIO import StringIO
import sys
import subprocess
import compress_file_using_zip
import os
sys.path.append("/home/scroller/python_bootcamp/admin")
import compress_file_using_zip_admin


class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        sys.stdout = self._stdout

FILE_TO_ZIP = 'MatchingEngine.log'

# Call the user's function and capture the output in 'output'
with Capturing() as output:
    captured_return_val = compress_file_using_zip.compress_file_using_zip('.', FILE_TO_ZIP)
if output[-1] == "":
    output.pop()

# Call the correct-known-output function and capture the output in 'expected_output'
with Capturing() as expected_output:
    expected_return_val = compress_file_using_zip_admin.compress_file_using_zip('.', FILE_TO_ZIP)
if expected_output[-1] == "":
    expected_output.pop()

print "\n****** Verify String In File Checker ******"
print "****** Let's see how you've done %s ******\n" % os.environ['USER']
i_output = [ "    "+str(x) for x in output ]
print "This is what your function printed (adding 4-space indent):\n%s\n" % "\n".join(i_output)
# expected_output = [ "    "+str(x) for x in expected_output ]
# print "EXPECTED OUTPUT:\n%s\n" % "\n".join(expected_output)


#Use this variable to keep track of pass/fail
passed = True

# Check that the lengths of the expected and captured output match
if len(expected_output) != len(output):
    print ("1.\nError: Your function's output is not of the expected length. "
           "Expected %s lines, only captured %s lines.\n" %
           (len(expected_output), len(output)))
    passed = False
else:
    print ("1.\nPassed: Your function's output produced the correct number of lines. "
           "Expected %s lines, captured %s lines.\n" %
           (len(expected_output), len(output)))

# Analyze the expected and captured outputs line by line
print "2.\nAnalyzing your output, line by line"
for index in range(1, len(expected_output)):
    try:
        if expected_output[index] != output[index]:
            print "Failed Match:\n    Expected:  %s\n    Captured:  %s" % (expected_output[index], output[index])
        else:
            print "Passed Match:\n    Expected:  %s\n    Captured:  %s" % (expected_output[index], output[index])
    except IndexError:
        print "List Index Error. Perhaps you haven't captured enough output"

# Check the return values
print "\n3.\nNow checking for the correct return value"
if expected_return_val == captured_return_val:
    print "Passed: Captured return value matches expected return value:\n    %s == %s" % (captured_return_val, expected_return_val)
else:
    print "Failed: Captured return value does NOT match expected return value:\n    %s != %s" % (captured_return_val, expected_return_val)

# Check for zipfile existance
print "\n4.\nChecking the current directory for the generated zipfile"
file_list = os.listdir(".")
if FILE_TO_ZIP+'.zip' in file_list:
    print "Passed: Found the zipfile '%s'" % FILE_TO_ZIP+'.zip'
else:
    print "Failed: Did not find the zipfile '%s'" % FILE_TO_ZIP+'.zip'
    passed = False

# Compare the file sizes
print "\n5.\nJust to be sure, comparing the file sizes"
uncompressed_file_size = int(os.path.getsize(FILE_TO_ZIP))
compressed_file_size   = int(os.path.getsize(FILE_TO_ZIP+'.zip'))
if compressed_file_size < uncompressed_file_size:
    print "Passed: The zip file size is smaller than the uncompressed file"
else:
    print "Failed: The zip file size is not smaller than the uncompressed file"
    passed = False

# Final output
if passed:
    print "\nFantastic! Everything works as expected!\n"
else:
    print "\nHm, something wasn't quite right with your function. Try again\n"

