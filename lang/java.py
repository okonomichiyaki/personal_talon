from talon import Context, Module, actions, settings

ctx = Context()
ctx.matches = r"""
tag: user.java
os: mac
and app.bundle: com.jetbrains.intellij.ce
"""
ctx.tags = ["user.code_operators", "user.code_generic"]


@ctx.action_class("user")
class UserActions:
 
    def code_state_if():
        actions.user.insert_between("if (", ") {")

    def code_state_else_if():
        actions.user.insert_between(" else if (", ") {")

    def code_state_else():
        actions.insert(" else {\n")
