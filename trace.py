import inspect

class code_trace():

    def variable_name(var):
        current_frame = inspect.currentframe()
        caller_frame = inspect.getouterframes(current_frame)[1]
        local_vars = caller_frame.frame.f_locals

        for name, value in local_vars.items():
            if value is var:
                return name