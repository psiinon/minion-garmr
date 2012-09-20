# A simple Template plugin

from plugin import MinionPlugin

class TemplatePlugin(MinionPlugin):


	default = {
		"template" : {
			"target" : { "type" : "url", "is_list" : True, "required" : True}
		},
		"safechecks" : { "type" : "bool", "value" : True}
	}

	def __init__(self):
		MinionPlugin.__init__(self, TemplatePlugin.default)

		self.state = "PENDING"

		self.messages = {
        	"PENDING" : "Plugin is pending execution.",
        	"WAITING" : "Execution is suspending, waiting for RESUME.",
        	"RUNNING" : "Execution is in progress.",
        	"COMPLETE" : "Execution is finished.",
        	"CANCELLED" : "Execution was cancelled.",
        	"FAILED" : "Execution failed."
		}
		self.allow_states = {
        	"PENDING" : ["START"],
        	"WAITING" : ["RESUME", "TERMINATE"],
        	"RUNNING" : ["SUSPEND", "TERMINATE"],
        	"COMPLETE" : [],
        	"CANCELLED" : [],
        	"FAILED" : []
        }


	def do_validate(config):
		return True

	def do_validate_key(key, value):
		return True

	def do_status(self):
		return self.create_status(True, self.messages[self.state], self.state)

	def do_start(self):
		self.state = "RUNNING"
		return self.create_status(True, self.messages[self.state], self.state)

	def do_suspend(self):
		self.state = "WAITING"
		return self.create_status(True, self.messages[self.state], self.state)

	def do_resume(self):
		self.state = "RUNNING"
		return self.create_status(True, self.messages[self.state], self.state)

	def do_terminate(self):
		self.state = "CANCELLED"
		return self.create_status(True, self.messages[self.state], self.state)

	def do_get_states(self):
		return self.allow_states[self.state]



