from pecan import rest, expose


class RootController(rest.RestController):

    @expose("json")
    def get(self):
        return "root Controller"
