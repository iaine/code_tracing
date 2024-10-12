'''
Class to use inspect to trace code names and types
'''
import time
import inspect


class code_trace():

    def __init__(self) -> None:
        self.traces = []

    def variable_name(self, var):
        '''Get the variable name'''
        current_frame = inspect.currentframe()
        caller_frame = inspect.getouterframes(current_frame)[1]
        local_vars = caller_frame.frame.f_locals

        for name, value in local_vars.items():
            if value is var:
                self._add_trace(name, type(var), var)
                

    def _add_trace(self, _name, _type, _data) -> None:
        self.traces.append({"name":_name, "type": _type, "data": _data})

    def _write_file(self):
        to_write = ';'.join(self.traces)
        filename = int(time.time()) + ".txt"
        fh = open(filename,"w")
        fh.write(to_write)
        fh.close()