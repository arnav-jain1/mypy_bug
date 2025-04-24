from mypy.types import LiteralType
from mypy.plugin import Plugin

def type_add(ctx, *args):
    lhs = ctx.type
    rhs = ctx.arg_types[0][0]
    print(lhs, rhs)
    ret = lhs.value + rhs.value
    ctx.api.fail("test", ctx.context)
    return LiteralType(ret, fallback=ctx.api.named_generic_type('builtins.int', []))

class TestPlugin(Plugin):

    def get_method_hook(self, fullname):
        if fullname == 'builtins.int.__add__':
            return type_add
        return None

def plugin(version: str):
    return TestPlugin
