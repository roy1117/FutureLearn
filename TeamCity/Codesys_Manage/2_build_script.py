import scriptengine

project = projects.open(r"C:\Users\a00533064\Desktop\CodeSys\CICD\Auto_Build.project", primary = True)
application = project.active_application
application.generate_code()
messages = system.get_messages("97f48d64-a2a3-4856-b640-75c046e37ea9")
print(messages)