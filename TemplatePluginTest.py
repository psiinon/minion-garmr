# Simple test cases for the TemplatePlugin

import json
import os
import plugin
from TemplatePlugin import TemplatePlugin

plugin = TemplatePlugin()

def check_result(result, expected):
	if (result.get("status") == expected):
		print "\tPassed."
	else:
		print "\tFailed - expected ", expected, " got ", result

print "Get status"
check_result(plugin.status(), "PENDING");

# print "Set value url..."
# print plugin.setValue("url", "http://localhost:8080")

print "Start"
plugin.start()
check_result(plugin.status(), "RUNNING");

print "Suspend"
plugin.suspend()
check_result(plugin.status(), "WAITING");

print "Resume"
plugin.resume()
check_result(plugin.status(), "RUNNING");

print "Terminate"
plugin.terminate()
check_result(plugin.status(), "CANCELLED");

