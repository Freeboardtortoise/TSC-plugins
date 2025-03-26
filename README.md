# plugins documentation

## TSC.console

### basic code
#must use in the server
import TSC.server()
import TSC.plugins.console
TSC.plugins.console.init()

### how to make a command line thing

TSC.plugins.console.console_thing(TSC.server.get_connections())
