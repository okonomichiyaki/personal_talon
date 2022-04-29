from talon import Context, actions

ctx = Context()
ctx.matches = r"""
mode: user.java
mode: user.auto_lang
and code.language: java
"""
ctx.tags = ["user.code_operators", "user.code_generic"]


@ctx.action_class("user")
class UserActions:
    pass
