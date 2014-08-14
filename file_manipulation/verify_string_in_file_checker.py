#!/usr/bin/python

from cStringIO import StringIO
import sys
import subprocess

sys.path.append(sys.argv[1])


def f():
    print "askl;fjasdkljfasljkdfasdklj"
    print "234234234234234"

class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        sys.stdout = self._stdout

with Capturing() as output:
    command = ["python", sys.argv[1]]
    captured = subprocess.Popen(command, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True).communicate()[0]
    print captured

if output[-1] == "":
    output.pop()

print "\n******Verify String In File Checker******\n"
#print "This is what your function printed:\n%s\n" % output

expected_output = [
    '        <add key="LogLevel" value="Error"/>',
    '        <section name="eventFormatterSettings" type="ISE.Library.EnterpriseLogging.EventSinks.FormatterConfigHandler, ISE.Library.EnterpriseLogging.EventSinks" />',
    '        <section name="ISE.Library.EnterpriseLogging" type = "System.Configuration.NameValueSectionHandler"/>',
    '        <section name="ISE.Library.Configuration" type="System.Configuration.NameValueSectionHandler" />',
    '        <formatterInfo name="eventLogFormatter" type="ISE.Library.EnterpriseLogging.EventSinks.EventLogFormatter, ISE.Library.EnterpriseLogging.EventSinks"/>',
    '    <ISE.Library.EnterpriseLogging>',
    '    </ISE.Library.EnterpriseLogging>',
    '    <ISE.Library.Configuration>',
    '    </ISE.Library.Configuration>',
    '        <add key = "startupDelay" value = "0"/>',
    '        <add key="instrumentationConfigFile" value="D:\ise\eif\EnterpriseInstrumentation.config" />',
    '        <add key="AlternateLoggingClass" value="ISE.LoggingBlockWrapper.LoggingBlockWrapper,ISE.LoggingBlockWrapper"/>',
    '        <add key="useCommLogger" value = "true"/>',
    '        <add key="synchronousCommLogger" value="true"/>',
    '        <add key="logRejectsToCommLogger" value="true"/>',
    '        <add key="logRejectsToLog" value="true"/>',
    '    <!-- <add key="loggingDirectory" value="d:\ise\log"/> -->',
    '        <add key="LogLevel" value="Error"/>',
    '        <add key="ApplicationName" value="IORS.BSI.ORA-3-PAT"/>',
    '            <add key="UserId" value="iors_gts_pat_gts14" />',
    '            <add key="Pwd" value="iors_gts_pat_gts14" />',
    '            <add key="InitialCatalog" value="iors_gts_pat_gts14" />',
    '            <add key="DataSource" value="DC-SQL01\SQM1,59897" />',
    '        <add key="InstanceName" value="IORS.BSI.ORA-3-PAT" />',
    '        <add key="Provider" value="ActiveMQ" />',
    '        <add key="Url" value="tcp://tc-pat221:61616" />'
]

if len(expected_output) != len(output):
    print "Error: Your function's output is not of the expected length. Expected %s lines, only captured %s lines.\n" % (len(expected_output), len(output))
else:
    print "Passed: Your function's output produced the correct number of lines. Expected %s lines, captured %s lines.\n" % (len(expected_output), len(output))

print "Analyzing your output, line by line\n"
for index in range(len(expected_output)):
    try:
        if expected_output[index] != output[index]:
            print "Failed Match:\n    Expected:  %s\n    Captured:  %s" % (expected_output[index], output[index])
        else:
            print "Passed Match:\n    Expected:  %s\n    Captured:  %s" % (expected_output[index], output[index])
    except IndexError:
        print "List Index Error. Perhaps you haven't captured enough output"
